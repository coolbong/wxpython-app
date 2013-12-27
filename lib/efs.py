import os.path
import sys
sys.path.append('./lib/')
sys.path.append("./native/")

try:
	import mptest as device
except ImportError as exc:
	import dummy as device
	print sys.stderr.write("Error: fail to import device module".format(exc))



MMCBLK_ID_RAWAREA = 0
MMCBLK_ID_PARAM = 1
MMCBLK_ID_MISC = 2
MMCBLK_ID_EFS = 3
MMCBLK_ID_EXT_ALL = 4
MMCBLK_ID_BOOT = 5
MMCBLK_ID_RECOVERY = 6
MMCBLK_ID_LOGO = 7
MMCBLK_ID_CACHE = 8
MMCBLK_ID_SYSTEM = 9
MMCBLK_ID_USERDATA = 10
MMCBLK_ID_ITEM_MAX = 11


FS_T_VFAT = 0
FS_T_EXT4 = 1
FS_TYPE_MAX = 2


MOUNT_PATH = "/factory"
MOUNT_PATH2 = "/cache"
FILE_BT_ADDR = "bluetooth/bt_addr"
FILE_WIFI_ADDR = "wifi_addr"
FILE_SN_NUM = "serial_number"
FILE_TSP_TYPE = "tsp_type"


FILE_CACHE_SN = "SN&MAC.txt"

#public
def NeedFormat():
	ret = False
	if Mount() == False:
		print "mmcblkMount failed"
		return True


	if _FileExist(MOUNT_PATH + "/" + FILE_TSP_TYPE):
		ret =  False
	else:
		ret =  True

	return ret

#not use plz remove
def Format():
	ret = _Format(MMCBLK_ID_EFS, FS_T_EXT4)
	if ret == 0:
		return True
	else:
		return False

def FormatEfs():
	if MountEfs() == False:
		ret = _Format(MMCBLK_ID_EFS, FS_T_EXT4)
		if ret == 0:
			return True
		else:
			return False
	else:
		print "FormatEfs already mounted"

def FormatCache():
	if MountCache() == False:
		ret = _Format(MMCBLK_ID_CACHE, FS_T_VFAT)
		if ret == 0:
			return True
		else:
			return False
	else:
		print "ForamtCache aleary mounted"

#not use plz remove
def Mount():
	if MountCheck() == False:
		ret = _Mount(MMCBLK_ID_EFS, FS_T_EXT4, MOUNT_PATH)
		if ret == 0:
			return True
		else:
			return False
	else:
		return True

def MountEfs():
	if MountCheckEfs() == False:
		ret = _Mount(MMCBLK_ID_EFS, FS_T_EXT4, MOUNT_PATH)
		if ret == 0:
			return True
		else:
			return False
	else:
		return True

def MountCache():
	if MountCheckCache() == False:
		ret = _Mount(MMCBLK_ID_CACHE, FS_T_VFAT, MOUNT_PATH2)
		if ret == 0:
			return True
		else:
			return False
	else:
		return True

#not use plz remove
def MountCheck():
	print "MountCheck"
	ret = _MountCheck(MOUNT_PATH)
	print ret
	if ret == 0:
		return True
	else:
		return False 

def MountCheckEfs():
	print "MountCheck"
	ret = _MountCheck(MOUNT_PATH)
	print ret
	if ret == 0:
		return True
	else:
		return False 

def MountCheckCache():
	print "MountCheck"
	ret = _MountCheck(MOUNT_PATH2)
	print ret
	if ret == 0:
		return True
	else:
		return False 


def EfsWrite(path, param):
	print ("path: %s, param: %s" %(path, param))
	ret = _EfsWrite(path, param)
	if ret >= 0:
		return True
	else:
		return False

def WriteBT2EFS(param):
	print "WriteBT2EFS: %s" %param
	if MountCheck() == False:
		Mount()

	return EfsWrite(MOUNT_PATH + "/" + FILE_BT_ADDR, param)

def WriteSN2EFS(param):
	print "WriteSN2EFS: %s" %param
	Mount()

	return EfsWrite(MOUNT_PATH + "/" + FILE_SN_NUM, param)

def WriteTsp2EFS(param):
	print "WriteTsp2EFS: %s" %param
	Mount()

	return EfsWrite(MOUNT_PATH + "/" + FILE_TSP_TYPE, param)	

def WriteWIFI2EFS(param):
	print "WriteWIFI2EFS: %s" %param
	Mount()

	return EfsWrite(MOUNT_PATH + "/" + FILE_WIFI_ADDR, param)

def CheckBTFile():
	Mount()
	if _FileExist(MOUNT_PATH + "/" + FILE_BT_ADDR):
		return True
	else:
		return False

def CheckSNFile():
	Mount()
	if _FileExist(MOUNT_PATH + "/" + FILE_SN_NUM):
		return True
	else:
		return False

def CheckTspFile():
	Mount()
	if _FileExist(MOUNT_PATH + "/" + FILE_TSP_TYPE):
		return True
	else:
		return False

def CheckWifiFile():
	Mount()
	if _FileExist(MOUNT_PATH + "/" + FILE_WIFI_ADDR):
		return True
	else:
		return False

def ReadBT():
	if CheckBTFile():
		return ReadFile(MOUNT_PATH + "/" + FILE_BT_ADDR)
	else:
		return None


def ReadSN():
	if CheckSNFile():
		return ReadFile(MOUNT_PATH + "/" + FILE_SN_NUM)
	else:
		return None

def ReadTsp():
	if CheckTspFile():
		return ReadFile(MOUNT_PATH + "/" + FILE_TSP_TYPE)
	else:
		return None

def ReadWifi():
	if CheckWifiFile():
		return ReadFile(MOUNT_PATH + "/" + FILE_WIFI_ADDR)
	else:
		return None

def ReadFile(path):
	return None
	#with open(path, 'rU') as file:
	#	datalines = (line.rstrip('\r\n') for line in file)
	#	for line in datalines:
	#		return line

def CheckSNFile():
	MountCache()
	if _FileExist(MOUNT_PATH2 + "/" + FILE_CACHE_SN):
		return True
	else:
		return False

def ReadSNFile():
	print CheckSNFile()
	if CheckSNFile():
		return ReadCacheFile(MOUNT_PATH2 + "/" + FILE_CACHE_SN)
	else:
		return None

def ReadCacheFile(path):
	#CheckSNFile()
	#read
	print path
	lines = []
	with open(path) as data:
		datalines = (line.rstrip('\r\n') for line in data)
		for line in datalines:
			lines.append(line)
		return lines

			


#pivate 
def _FileExist(path):
	return os.path.exists(path)

def handleError(msg):
	print msg

def _Format(blk_no, fs_type):
	try:
		return device.mmcblkFormat(blk_no, fs_type)
	except:
		handleError("Error occured during mmcblkFormat")

def _EfsWrite(efs_path, param_data):
	try:
		#ret = device.efsWrite(efs_path, param_data)
		print ("_EfsWrite: %s" %ret)
		#return ret

		return 1
	except:
		handleError("Error occured during efsWrite")

def _MountCheck(path):
	#try:
	return device.mountCheck(path)
		#extern int mountCheck(char *mountpoint);
	#except:
	#	handleError("Error occured during mountCheck")
	#	raise Exception("mountCheck failed ")

def _Mount(blk_no, fs_type, mountpoint):
	try:
		return device.mmcblkMount(blk_no, fs_type, mountpoint)
	except:
		handleError("Error occured during mmcblkMount")
		raise Exception("mmcblkMount failed ")
