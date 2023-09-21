'''
-->Description
	This masterbot is used to check the health of switch Fabric and write the report in the log file. 
	If the remote command output is null, then the health of the switch is perfect.
	The following bots are used :
			1. RemoteConnect = This Microbot is used for taking the SSH session to all the Remote servers.
			2. HealthcheckForSwitchFabrics = This Microbot will perform the health check of the switch.
			3. LMB32_write_logs = To write the Microbot and Routine Logs.
			
			
-->Inputs
			1. Two inventory file path where Hostname and creds are present.
			

-->Output
			1. Success: Success output will be written in the log file based on date.

			2. Failed: Failure output will be written in the log file based on date.
	
--> Pre Requisite
	1. Python version 3.6 should be installed on the RAS/Jump server.
	2. Paramiko module for remote connection should be installed on the RAS/jump server.
	3. User should have privilages for executing commands for above mentioned microbots on the target server..

--> EXAMPLE
	python3 HealthcheckForSwitchFabricsMASTERbot.py
	
--> NOTES
Script Name    : HealthcheckForSwitchFabricsMASTERbot.py
Script Version : 1.0
Modules Used   : os,sys,paramiko,datetime,getpass
Python Version : 3.6
Developed By   : Oindrila Dey(oindrila.dey@capgemini.com)
Organization   : Capgemini

'''
import os,sys
import time
import datetime
import getpass as getpass
import paramiko

# coding=utf-8

#Fetch today's date
current_date = datetime.datetime.now().date()
#print(current_date)
formatted_date = current_date.strftime("%Y_%b_%d") # Format the date as "YYYY_MM_DD"
print("Today's Date:", formatted_date)

#open and read the two inventory file, one is for Hostname and other is for creds
import csv
target_servers = []
file_path = 'C:/Users/oindey/Desktop/Ansible/pythonFiles/ADC2023-5888_withTwoInventoryFile/server.csv'
#file_path = '/root/Oindrila/ADC2023-5888/server.csv'
with open (file_path, 'r', encoding='utf-8-sig') as csvfile:
	csv_reader = csv.DictReader(csvfile)
	for row in csv_reader:
		target_servers.append(row)
#print(target_servers)

'''
target_creds = []
cred_file_path = 'C:/Users/oindey/Desktop/Ansible/pythonFiles/ADC2023-5888/creds.csv'
#cred_file_path = '/root/Oindrila/ADC2023-5888/creds.csv'
with open (cred_file_path, 'r', encoding='utf-8-sig') as Cred_csvfile:
	cred_csv_reader = csv.reader(Cred_csvfile)
	for row in cred_csv_reader:
		target_creds.append(row)
#print(target_creds[-1])'''

#read the encrypted data for the creds
from cryptography.fernet import Fernet

# Load the encryption key (The same key used for encryption)
key = b'_LREkXLq1baabFYPLNR6QkPB5SgCvi87uXJSg3ZPbbM='
fernet = Fernet(key)
encrypted_file = 'C:/Users/oindey/Desktop/Ansible/pythonFiles/ADC2023-5888_withTwoInventoryFile/encrypted_file.txt'
# Read the encrypted data from the file
with open(encrypted_file, 'rb') as file:
    encrypted_data = file.read()
#print(encrypted_data)
# Decrypt the data
decrypted_data = fernet.decrypt(encrypted_data)
#print(decrypted_data)
data_str = decrypted_data.decode().strip().split('\r\n')
username, password = data_str[1].split(',')
#print(username)
#print(password)


#To create all the sub-director
log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Logs")
log_file_path = os.path.join(log_path, formatted_date + "_logs", formatted_date + "_logs.log")
microbot_path_name = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Microbots")
sys.path.append(microbot_path_name)


import LMB32_write_logs
import RemoteConnect
import HealthcheckForSwitchFabrics
try:
	for server in target_servers: #script should run for each server present in the inventory
	#print(server)
	
		######### This Micro Bot is used to Connect to the Remote server
		print("Taking the remote connection of ",server["hostname"])
		LMB32_write_logs.write_log("Trying to take the remote connection for {} server".format(server["hostname"]),formatted_date,log_path,"Info")
		remote_connect = RemoteConnect.remoteConnect(server["hostname"],username,password) #target_creds[-1][-1]
		if(remote_connect[0] == False):
			LMB32_write_logs.write_log("Unable to Connect to remote server {}".format(server["hostname"]),formatted_date,log_path,"Error")
			print("Unable to Connect to remote server")
		else:
			print("Remote connection taken successfully")	
			ssh_paramiko = remote_connect[1]
			LMB32_write_logs.write_log("Successfully taken remote connection: {}".format(server["hostname"]),formatted_date,log_path,"Info")
			######### This Micro Bot is used to fetch the health check status
			print("Started Execution Of HealthcheckForSwitchFabrics Bot")
			LMB32_write_logs.write_log("Started Execution Of HealthcheckForSwitchFabrics Bot", formatted_date, log_path, "Info")
			Healthcheck_Result = HealthcheckForSwitchFabrics.HealthcheckForSwitchFabrics(ssh_paramiko,formatted_date, log_path)
			if(Healthcheck_Result[0] == False):
				LMB32_write_logs.write_log("Error found, the error is: {}".format(Healthcheck_Result[1]),formatted_date, log_path, "Error")
			else:
				LMB32_write_logs.write_log("No issue found. {}".format(Healthcheck_Result[1]),formatted_date, log_path, "INFO")	
				LMB32_write_logs.write_log("Health check Script executed successfully for '{}' server".format(server["hostname"]),formatted_date,log_path,"Info")
			print("Health check Script executed successfully, kindly check log for detailed output")
	LMB32_write_logs.write_log("Script Ended",formatted_date,log_path,"Info")		
		
except Exception as e:
	print(e)
	LMB32_write_logs.write_log("Exception in Fabric Switch Health Check", str(e), formatted_date, log_path, "Error")


print("this is the end")
