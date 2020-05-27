from netmiko import ConnectHandler
from getpass import getpass

filename=input("Device list filename?\n")

with open(filename) as f:
    devicenames = f.read().splitlines()

username=input("Enter your SSH username: ")
password=getpass()
