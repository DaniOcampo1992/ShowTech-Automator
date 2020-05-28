"""
Remaining tasks:
- Specify SSH port in devices file, or use default if there is none.
- Exception handling on net_connect
"""


from netmiko import ConnectHandler  #Used to SSH connect into devices
from getpass import getpass         #Hides the password input
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

filename=input("Device list filename?\n")

while(True):
    try:
        with open(filename) as f:
            devicenames = f.read().splitlines()
            break
    except(FileNotFoundError):
        print("The filename specified does not exist.\n")
        filename=input("Device list filename?\n")

devicelist = {}
for item in devicenames:
    if "," in item:             #This should be eventually changed to a proper indexing, not more of 1 comma per item
        devicedata = item.split(",")
    else:
        devicedata[0] = item
        devicedata[1] = 22
    devicedict = {
        "name": devicedata[0],
        "port": devicedata[1]
    }
    devicelist[item] = devicedict

username=input("Enter your SSH username: ")

while(True):
    password1=getpass()
    print("Enter your password again: ")
    password2=getpass()
    if (password1!=password2):
        print("Passwords does not match, type again: ")
        continue
    break

for items,device in devicelist.items():
    print("Connecting to device "+device["name"])
    network_device = {
        "device_type": "cisco_ios",
        "ip": device["name"],
        "username": username,
        "password": password1,
        "port": device["port"],
    }
    
    try:
        net_connect = ConnectHandler(**network_device)
        output = net_connect.send_command_timing("show tech-support",delay_factor=100)       #show run only for testing
        saveoutput =  open("outputs/showtech-"+device["name"]+".txt", "w")
        saveoutput.write(output)
        saveoutput.write("\n")
        saveoutput.close
        print("Output saved at outputs/showtech-"+device["name"]+".txt")
    except (AuthenticationException):
        print ("Cannot authenticate on "+device["name"]+". Bad username and password maybe?")
        continue
    except (NetMikoTimeoutException):
        print ("Timeout to device "+device["name"])
        continue
    except (EOFError):
        print ("End of file error on device "+device["name"])
        continue
    except (SSHException):
        print ("SSH error. Is SSH enabled on "+device["name"]+"?")
        continue
    except Exception as unknown_error:
        print ("Unknown error: "+unknown_error)
        continue
