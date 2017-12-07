import os
import fnmatch
import cfg
import compressTool

def findFile(filename):
    results = []
    for file in os.listdir("."):
        if fnmatch.fnmatch(file, filename):
            #print "found "+file
            results.append(file)
    return results

def findFilePath(filename, rootdir):
	result = []
	#print rootdir
	for root, subFolders, files in os.walk(rootdir):
		#print root, subFolders, files
		for f in files:  
			if fnmatch.fnmatch(f, filename):  
				result.append(os.path.join(root, f)) 
	return result 

def findPkg(filenames, rootdir):
	#print filenames, rootdir
	result = []
	for root, subFolders, files in os.walk(rootdir):
		#print root, subFolders, files
		for f in files:
			for filename in filenames:  
				if fnmatch.fnmatch(f, filename):  
					result.append(os.path.join(root, f)) 
	return result 

def findOneFile(filename, rootdir):
	files = findFilePath(filename, rootdir)
	if len(files) == 1:
		return os.path.dirname(files[0])
	elif len(files) == 0:
		return None
	else:
		return "multi"

def findAllFile(filename, rootdir):
	files = findFilePath(filename, rootdir)
	return files

def extractFind(filename, rootdir):
	result = []
	c = cfg.configFile()
	cf = c.cp

	toolName = cf.get("Tool", "Name")
	FileTypes = cf.get("Tool", "FileTypes")

	pkgTypes = FileTypes.split(';')
	# find archive and extract
	decompressed_files = []
	pkgs = findPkg(pkgTypes, rootdir)
	need_extract_files = [x for x in pkgs if x not in decompressed_files] + [x for x in decompressed_files if x not in pkgs]
	if need_extract_files != []:
		print "found pkgs need extract:"
		print need_extract_files

		if len(need_extract_files) == 0:
			#print "pkgs not found"
			return None
		else:
			#print need_extract_files
			for p in need_extract_files:
				arch = compressTool.extractFile(p, toolName)
				if arch.extractFile() == 0:
					decompressed_files.append(p)
					files = findAllFile(filename, rootdir)
					if files == None:
						pass
					else:
						for file in files:
							result.append(file)
				else:
					print "ERR: %s format err" % p
					pass
	return result
	