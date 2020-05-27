from netmiko import ConnectHandler
from getpass import getpass

filename=input("Device list filename?\n")

with open(filename) as f:
    commands_to_send = f.read().splitlines()

username=input("Enter your SSH username: ")
password=getpass()
