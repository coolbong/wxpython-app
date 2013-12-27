import csv
import os.path
from collections import OrderedDict
from wx.lib.pubsub import Publisher

import sys
sys.path.append('./ui/')

import TC



dic = OrderedDict()
dic['TEST'] 					= ['ASSEMBLY' , 'PCB']
dic['SERIAL'] 				= ['NULL', 'NULL']
dic['STATUS_GPS'] 			= ["NT", 'NT']
dic['STATUS_ACCELEROMETER'] 	= ["NT", 'NT']
dic['STATUS_MAGNETIC'] 		= ["NT", 'NT']
dic['STATUS_LIGHT'] 			= ["NT", 'NT']
dic['STATUS_EFS'] 			= ["NT", 'NT']
dic['DISP_TEST'] 			= ["NT", 'NT']
dic['TOUCH_TEST'] 			= ["NT", 'NT']
dic['BUTTON_TEST'] 			= ["NT", 'NT']
dic['AUDIO_TEST'] 			= ["NT", 'NT']
dic['EARPHONE_TEST'] 		= ["NT", 'NT']
dic['MIC_TEST'] 				= ["NT", 'NT']
dic['CAMERA_TEST'] 			= ["NT", 'NT']
dic['STORAGE_TEST'] 			= ["NT", 'NT']
dic['LIGHT_TEST'] 			= ["NT", 'NT']
dic['ACCELEROMETER_TEST'] 	= ["NT", 'NT']
dic['MAGNETIC_TEST'] 		= ["NT", 'NT']
dic['GPS_TEST'] 				= ["NT", 'NT']
dic['WIFISCAN_TEST'] 		= ["NT", 'NT']
dic['BTSCAN_TEST'] 			= ["NT", 'NT']
dic['BARCODE_BT_MAC'] 		= ["NT", 'NT']
dic['BARCODE_WIFI_MAC'] 		= ["NT", 'NT']
dic['BARCODE_DEVICE_SN'] 	= ["NT", 'NT']
dic['AGING_TEST'] 			= ["NT", 'NT']
dic['CPU_TEST'] 				= ["NT", 'NT']


file_name = 'mptest_test_result.csv'

def write_file():
	global dic
	global file_name
	with open(file_name, 'wb') as file:
	
		w = csv.writer(file)
		w.writerow(dic.keys())
		values = dic.values()

		list_asm = []
		list_pcb = []

		for value in values:
			list_asm.append(value[0])
			list_pcb.append(value[1])
		w.writerow(list_asm)
		w.writerow(list_pcb)
	file.close()


def file_exist():
	global file_name
	return os.path.exists(file_name)


def read_file():
	global dic
	global file_name

	if file_exist() == False:
		write_file()
		return

	with open(file_name, 'r') as file:
		
		reader = csv.reader(file)

		list_lines = []
		for line in reader:
			list_lines.append(line)

		i = 0
		for item in list_lines[0]:
			dic[item] = [list_lines[1][i], list_lines[2][i]]
			i += 1
	file.close()

tc_name = {
	TC.TCDisplay: "DISP_TEST",
	TC.TCTouch: "TOUCH_TEST",

	TC.TCButton	: "BUTTON_TEST",
	TC.TCAudio: "AUDIO_TEST",
	TC.TCEarPhone: "EARPHONE_TEST",
	TC.TCMIC: "MIC_TEST",
	TC.TCCamera	: "CAMERA_TEST",
	TC.TCStorage: "STORAGE_TEST",
	#TC.TCBarcode: "DISP_TEST",
	TC.TCBarcodeBTMac : "BARCODE_BT_MAC",
	TC.TCBarcodeWifiMac: "BARCODE_WIFI_MAC",
	TC.TCBarcodeSN: "BARCODE_DEVICE_SN",
	TC.TCCPU: "CPU_TEST",
	#TC.TCAging: "AGING_TEST",

	TC.TCRFGps: "GPS_TEST",
	#TC.TCRFWifi: "DISP_TEST",
	#TC.TCRFBluetooth: "DISP_TEST",
	TC.TCRFWifiScan	: "WIFISCAN_TEST",
	TC.TCRFBtScan: "BTSCAN_TEST",

	TC.TCSSLightSensor: "LIGHT_TEST",
	TC.TCSSAccellerometer: "ACCELEROMETER_TEST",
	TC.TCSSMagnticField: "MAGNETIC_TEST",

	TC.TCSTGps: "STATUS_GPS",
	TC.TCSTAcc: "STATUS_ACCELEROMETER",
	TC.TCSTMag: "STATUS_MAGNETIC",
	TC.TCSTLig: "STATUS_LIGHT",
	TC.TCSTEfs: "STATUS_EFS",
	TC.TCSerialNumber: "SERIAL"
}


def tcid_to_tcname(id):
	global list
	#print list

	return tc_name[id]
	


MPTEST_ASM = 0
MPTEST_PCB = 1

def testcase_result(test, msg):
	global dic

	#print msg
	result, tc = msg

	tcname = tcid_to_tcname(tc)

	if tcname == None:
		print "%d is unexist test" %tc
		return
	else:
		values = dic[tcname]
		if result == "True":
			values[test] = "PASS"
		else:
			values[test] = "FAIL"
		#elif result == "False":
		#	values[test] = "FAIL"
		#else:
		#	values[test] = result
	write_file()

def SetSerialNumer(test, sn):
	global dic

	values = dic['SERIAL']
	values[test] = sn
	write_file()

	
def init():
	read_file()


