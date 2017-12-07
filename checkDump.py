import os
import sys
import findFile
import findReason
from cfg import *

def checkDump(log_path, platform):
	# read ramdump path from cfg.ini
	thisPath = os.path.split(os.path.realpath(__file__))[0]
	lpPath = os.path.split(thisPath)[0]
	cfg = configFile()
	cf = cfg.cp
	
	keyword = cf.get("module", platform)
	print keyword

	# find all files we need
	logs = findFile.extractFind("syslog", log_path)
	for log in logs:
		print log
		result = findReason.findReason(log, keyword, os.path.join(os.path.dirname(log), keyword))


# main
'''
if len(sys.argv) < 3 or len(sys.argv) > 4:
	print "Usage: \tcheckDump vmlinux_path dump_log_path [MSM_platform]"
else:
	# get input from sys.argv
	if len(sys.argv) > 3:
		pf = sys.argv[3]
	else:
		pf = ""

	checkDump(sys.argv[1], sys.argv[2], pf)
'''
