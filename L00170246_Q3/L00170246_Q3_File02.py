"""
#
# File          :   L00170167_Q2_File_1.py
# Created       :   21.11.2021
# Author        :   Pierce O'Neill
# Version       :   1.0.0
# Licensing     :   (C) 2021 Pierce O'Neill LYIT
#                   Available under GNU Public License (GPL)
# Description   :   Question 3 - Create an SSH Connection to the VM
#
"""
import paramiko


def ssh_connection():

    try:
        ip = "172.16.88.129"
        user_name="l00170246".rstrip("\n")
        user_password="Wms0Fri2021!".rstrip("\n")
        # Create the SSH connection to the VM›
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(ip, username=user_name, password=user_password)
        print("Connected to: ", ip)  # Output connected status

    except paramiko.BadAuthenticationType as e:

        print(e)

        sys.exit(1)


if __name__ == '__main__':


    ssh_connection()