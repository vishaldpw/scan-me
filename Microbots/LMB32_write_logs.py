############################ Write_logs ##################################
'''
Developer: Daksh Goyal
Inputs: 1.msg - message to be printed in logs.
        2.date
        3.logpath
        4.type - Type of logs eg. INFO,DEBUG,WARNING,ERROR etc.
Output: Log file will be created at the given path.
Description: To write the Microbot and Routine Logs.
'''
###################################################################################
import datetime
import sys
import os
import time


###################################################################################
def dateTime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


###################################################################################

######################### function to write the Log file ##########################
def write_file(msg, logpath, type):
    try:
        with open(logpath, 'a') as file:
            file.write("[log]: {} {}: {}\n".format(dateTime(), type, msg))
            return True
    except Exception:
        t, err = sys.exc_info()[:2]
        print(err)
        return False


####################################################################################

#### function to check the logpath for MB and then call the write_file function ####
def write_log(msg, date, logpath, type):
	try:
		if os.path.exists(logpath):
			logFolder = os.path.join(logpath, date + "_Logs")
			msg = msg.replace("\n", " ")
			if os.path.exists(logFolder):
				microBotLogFile = os.path.join(logFolder, date + "_Logs.log")
			else:
				cmd = "mkdir " + '"' + logFolder + '"'
				os.popen(cmd)
				time.sleep(1)
				microBotLogFile = os.path.join(logFolder, date + "_Logs.log")
			write_file(msg, microBotLogFile, type)
		else:
			cmd1 = "mkdir " + '"' + logpath + '"'
			os.popen(cmd1)
			time.sleep(1)
			logFolder = os.path.join(logpath, date + "_Logs")
			msg = msg.replace("\n", " ")
			if os.path.exists(logFolder):
				microBotLogFile = os.path.join(logFolder, date + "_Logs.log")
			else:
				cmd = "mkdir " + '"' + logFolder + '"'
				# print(cmd)
				os.popen(cmd)
				time.sleep(1)
				microBotLogFile = os.path.join(logFolder, date + "_Logs.log")
			write_file(msg, microBotLogFile, type)
	except Exception:
		t, err = sys.exc_info()[:2]
		print(err)
		return False