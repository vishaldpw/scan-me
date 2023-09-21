'''
-->Description
	This Microbot is used for taking the SSH session to all the Remote servers.
	
			
-->Inputs
			1. host_name = the server ip
			2. os_user = user name to connect to the server
			3. os_passwd = password to connect to the server.

-->Output
			1. Success: True, ssh connection object

			2. Failed: False, connection failed message
	
--> Pre Requisite
	1. Python version 3.6 should be installed on the RAS/Jump server.
	2. Paramiko module for remote connection should be installed on the RAS/jump server.
	3. User should have privilages for executing commands for above mentioned microbots on the target server..

--> EXAMPLE
	python3 RemoteConnect.py
	
--> NOTES
Script Name    : RemoteConnect.py
Script Version : 1.0
Modules Used   : os,paramiko
Python Version : 3.6
Developed By   : Oindrila Dey(oindrila.dey@capgemini.com)
Organization   : Capgemini

'''

import os
import paramiko
def remoteConnect(host_name,os_user,os_passwd):
	try:
		ssh_paramiko = paramiko.SSHClient()
		ssh_paramiko.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_paramiko.connect(host_name, username=os_user, password=os_passwd)
		remoteConnectReturnResult = ssh_paramiko
		return True,remoteConnectReturnResult
	except Exception as e:
		remoteConnectReturnResult=e
		return False,remoteConnectReturnResult
