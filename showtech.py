from netmiko import ConnectHandler  #Used to SSH connect into devices
from getpass import getpass         #

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