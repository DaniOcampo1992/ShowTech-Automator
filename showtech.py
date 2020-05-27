from netmiko import ConnectHandler  #Used to SSH connect into devices
from getpass import getpass         #Hides the password input

filename=input("Device list filename?\n")

while(True):
    try:
        with open(filename) as f:
            devicenames = f.read().splitlines()
            break
    except(FileNotFoundError):
        print("The filename specified does not exist.\n")
        filename=input("Device list filename?\n")


print(devicenames)  #Only for debugging purposes
username=input("Enter your SSH username: ")

while(True):
    password1=getpass()
    print("Enter your password again: ")
    password2=getpass()
    if (password1!=password2):
        print("Passwords does not match, type again: ")
        continue
    break

print(password1+" "+password2)  #Only for debugging purposes

for device in devicenames:
    print("Connecting to device "+device)
    network_device = {
        'device_type': 'cisco_ios',
        'ip': device,
        'username': username,
        'password': password1,
        "port": 8181,
    }
    net_connect = ConnectHandler(**network_device)      #Analize where to put the try for exception handling
    #net_connect.send_command("terminal lenght 0")
    output = net_connect.send_command_timing("show tech-support")       #show run only for testing
    saveoutput =  open("outputs/showtech-"+device+".txt", "w")
    saveoutput.write(output)
    saveoutput.write("\n")
    saveoutput.close