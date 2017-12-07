import os
import cfg

'''
reasons = [
	"Kernel panic",
	"Watchdog bark",
	"Unable to handle kernel paging request",
	]
'''

def findReason(filename, keyword, outfile):
	result = ""

	c = cfg.configFile()
	cf = c.cp
	#keys = cf.get("Reason", "Keywords")
	#print keys
	#reasons = keys.split(';')
	#print reasons
	print "=================="
	print "Finding keyword..."
	f = open(filename, "r")
	if outfile != None:
		o = open(outfile, "w")
	else:
		o = None
		
	for l in f.readlines():
		if keyword in l:
			print l
			if o != None:
				o.write(l);
			
	f.close()
	if o != None:
		o.close()
	
	print "That's all I can find..."
	
	return result
	
