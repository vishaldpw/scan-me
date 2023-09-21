'''
---> Description
This Microbot is used to check the health of switch Fabric if the remote command output is null, then the health of the switch is perfect.

---> INPUTS
	All inpputs are coming from the Master Bot.
	  1.ssh_paramiko = Remote Connection Object
	  2.Date = today's date
	  3.log_path = path to create the log file

--> OUTPUT
		a. Success:
			1. True
			2. Result

		b. Failed:
			1. False
			2. Result

--> Pre Requisite
	1. Python version 3.5 should be installed on the RAS/Jump server.
	2. Paramiko module for remote connection should be installed on the RAS/Jump server.
	3. Service account should have permissions to execute the command

--> EXAMPLE
	python3 HealthcheckForSwitchFabrics.py
	
--> NOTES
Script Name    : HealthcheckForSwitchFabrics.py
Script Version : 1.0
Modules Used   : LMB32_write_logs
Python Version : 3.6
Developed By   : Oindrila Dey(oindrila.dey@capgemini.com)
Organization   : Capgemini
'''
import LMB32_write_logs

def HealthcheckForSwitchFabrics(ssh_paramiko,date, log_path):
	try:
		remote_command = "Switchshow | grep Laser"
		#remote_command = "hostname"
		stdin, stdout, stderr = ssh_paramiko.exec_command(remote_command)
		output = stdout.read().decode()
		if output == '':
			HealthcheckResult = "No output found, No further action require."
			return True,HealthcheckResult
		else:
			return False,output

		##### Exception Handling ######################################
	except Exception as err:
		print("error is: ", err)
		LMB32_write_logs.write_log(str(err), date, log_path, "Error")
		return False,str(err)

