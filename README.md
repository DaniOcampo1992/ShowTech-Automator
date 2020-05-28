# ShowTech-Automator

Simple script to save the show tech command output of any number of Cisco IOS devices in separate text files per device.

Dependencies:
- Netmiko

Operability conditions:
- The host running the script must have network reachability to all destination devices.
- All destination devices must have SSH enabled, with permissions to accept connections from the host running the script.
- All destination devices must share the same SSH username and password.

Usage:
- Create a simple text file listing the domain name or IP addresses of the destination devices, one per line. By default, the script attempts to connect using TCP port 22. If a device on the list use a different SSH port, specify it next to the address separated by a coma (,).
Example:
192.168.4.1
homerouter.com,8181
10.40.5.1,4545
neighborsrouter.com

- Run showtech.py.
- Specify the name of the previously created text file.
- The script will prompt to type the username and password. The password must be typed twice to prevent typos.
- The show tech files will be generated at the output folder.

Recommended reading about how Netmiko's send_command works:
- https://pynet.twb-tech.com/blog/automation/netmiko-what-is-done.html
