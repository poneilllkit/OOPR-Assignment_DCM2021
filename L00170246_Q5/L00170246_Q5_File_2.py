"""
#
# File          :   L00170246_Q5_File02.py
# Created       :   24.11.2021
# Author        :   Pierce O'Neill
# Version       :   1.0.0
# Licensing     :   (C) 2021 Pierce O'Neill LYIT
#                   Available under GNU Public License (GPL)
# Description   :   Question 6 -Manipulate/Complete code
#
"""
----------------------------------------------------

''' Sockets code to carry out a port scan '''
''' Modified from:  Network Examples 1 by Ruth Lennon, LYIT'''

import socket
import subprocess
import sys
from datetime import datetime


def port_scan():
    """
    This function will carry out a port scan on a virtual machine
    """
    # Clear the screen  #use clear if running in  *nix

    # Ask for input
    remoteserver = input("Enter a remote host to scan: ")
    remoteserverip = socket.gethostbyname(remoteserver)
    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host", remoteserverip)
    print("-" * 60)

    # Check what time the scan started
    t1 = datetime.now()
    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)
    # We also put in some error handling for catching errors
    try:
        # try 1, 1025 if you have time
        for port in range(21, 81):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteserverip, port))
            if port == 22:  # Return SSH if Port 22 open
                print(f"SSH:{port} is open     ")
            elif port == 80:  # Return HTTP if Port 80 open
                print(f"HTTP:{port} is open     ")
            elif result == 0:
                print("Port {}:    Open".format(port))
                sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()
    except socket.error:
›        print("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()
    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1
    # Printing the information to screen
    print('Scanning Completed in: ', total)


if __name__ == '__main__':

    port_scan()



# Import required modules
import paramiko
import sys


# Define function for ssh connection and run commands
def ssh_connection():
    """
    This function will connect to VM via SSH and run some commands
    """
    try:
        ip = "172.16.88.129"
        user_name = "l00170246".rstrip("\n")
        user_password = "Wms0Fri2021!".rstrip("\n")

        # Create the SSH connection to the VM
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(ip, username=user_name, password=user_password)

        # Commands to create the folder structure
        ssh.exec_command("mkdir Labs\n")
        ssh.exec_command("mkdir Labs/lab1\n")
        ssh.exec_command("mkdir Labs/lab2\n")

        # Output the directory listing to show folders created
        com = "ls ./Labs\n"  # Command variable
        stdin, stdout, stderr = ssh.exec_command(com)  # Run command
        output = ''  # Set output variable to empty
        for line in stdout.readlines():  # Populate with results of the command
            output += line
        if output:
            print("Folders structure created:\n" + output)  # Print the out directory structure
        else:
            print("There was no output for this command")  # Error check if command returns nothing

        # Command to find file last access time
        stdin, stdout, stderr = ssh.exec_command("ls -l --time=atime\n")
        output = ''  # Set output variable to empty
        for line in stdout.readlines():  # Populate with results of the command
            output += line
        if output:
            print("Apt update:\n" + output)  # Print the out directory structure
        else:
            print("There was no output for this command")  # Error check if command returns nothing

        # Commands to update app repositories
        stdin, stdout, stderr = ssh.exec_command("echo l00092017 | sudo -S apt-get update\n")
        output = ''  # Set output variable to empty
        for line in stdout.readlines():  # Populate with results of the command
            output += line
        if output:
            print("Apt update:\n" + output)  # Print the out directory structure
        else:
            print("There was no output for this command")  # Error check if command returns nothing

        stdin, stdout, stderr = ssh.exec_command("echo l00092017 | sudo -S apt-get install -y curl\n")
        output = ''
        for line in stdout.readlines():
            output += line
        if output:
            print("Curl Installed:\n" + output)
        else:
            print("There was no output for this command")  # Error check if command returns nothing

    except paramiko.AuthenticationException:
        print("Authentication Error")
        sys.exit(1)


# Run the function
if __name__ == '__main__':
    """
	This is the main function
	This will call the ssh_connection function to set a folder structure and install curl on remote VM
	Parameters: none
	returns: none

    """
    ssh_connection()