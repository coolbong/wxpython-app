import os.path
import sys
sys.path.append('./lib/')
sys.path.append("./native/")

try:
	import mptest as device
except ImportError as exc:
	import dummy as device
	print sys.stderr.write("Error: fail to import device module".format(exc))


PARAM_INFO_SERIAL_NUM 	= 0
PARAM_INFO_WIFI_MAC 		= 1
PARAM_INFO_BT_ADDRESS 	= 2
PARAM_INFO_ACC_OFFSET 	= 3
PARAM_INFO_MAG_OFFSET 	= 4
PARAM_INFO_GYRO_OFFSET 	= 5
PARAM_INFO_WV_KEYBOX 	= 6
PARAM_INFO_RESERVED01 	= 7
PARAM_INFO_RESERVED02 	= 8
PARAM_INFO_RESERVED03 	= 9
PARAM_INFO_TSP_TYPE 		= 10

def handleError(msg):
	print msg

def ReadParam(param_type):
	try:
		return device.paramRead(param_type)
	except:
		handleError("Read Param")
		return None

def ReadParamSN():
	return ReadParam(PARAM_INFO_SERIAL_NUM)


def ReadParamWIFI():
	return ReadParam(PARAM_INFO_WIFI_MAC)

def ReadParamBT():
	return ReadParam(PARAM_INFO_BT_ADDRESS)

def ReadParamTSP():
	return ReadParam(PARAM_INFO_TSP_TYPE)