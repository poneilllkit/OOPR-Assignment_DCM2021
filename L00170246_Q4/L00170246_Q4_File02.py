"""
#
# File          :   L00170246_Q4_File02.py
# Created       :   21.11.2021
# Author        :   Pierce O'Neill
# Version       :   1.0.0
# Licensing     :   (C) 2021 Pierce O'Neill LYIT
#                   Available under GNU Public License (GPL)
# Description   :   Question 3 - Create an SSH Connection to the VM
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
