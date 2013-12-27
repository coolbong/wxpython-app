#!/usr/bin/python
import random

#TBD random data

#accelerometer
def acc_start():
	print "dummy acc_start"

def acc_end():
	print "dummy acc_end"

def acc_get_data():
	x = random.randrange(-10.0, 10.0)
	y = random.randrange(-10.0, 10.0)
	z = random.randrange(-10.0, 10.0)
	return ("%f:%f:%f" %(x,y,z))

def acc_check():
	print "dummy acc_check"
	return 1

#magnetic
def mag_start():
	print "dummy mag_start"

def mag_end():
	print "dummy mag_end"

def mag_get_data():
	return "10.0:20.0:30.0:10.0,40.0:50.0:60.0:22.0"

def mag_check():
	print "dummy mag_check"
	return 1

#l-sensor
def light_start():
	print "dummy light_start"

def light_stop():
	print "dummy light_stop"

def light_get_data():
	return random.randrange(0, 101)
	#return ""
def light_check():
	print "dummy light_check"
	return 1


#button
def key_start():
	print "dummy key_start"

def key_get():
	val = random.sample([0, 115, 0, 114, 0, 116, 0], 1)
	return  val[0]

def key_end():
	print "dummy key_end"


#gps
def gps_check():
	print "dummy gps_check"
	return 1
	
def gps_start():
	print "dummy gps_start"
	return 1;

def gps_sync_data():
	print "dummy gps_sync_data"

def gps_get_status():
	return 1

def gps_get_TimeOfFirstFix():
	return 26.0

def gps_get_MaxPRM():
	return 31.0

def gps_get_MaxSNRv():
	return 49.0

def gps_get_Speed():
	return 0.0

def gps_get_NumOfSVCS():
	return 12.0

def gps_get_Accuracy():
	return 5.0

def gps_get_Longitude():
	return random.randrange(0.0, 34.0)

def gps_get_Latitude():
	return random.randrange(50, 127)

def gps_get_Altitude():
	return random.randrange(0, 115)

def gps_end():
	print "dummy gps_end"


#wifi scan

def wifi_start():
	print "dummy wifi_start"
	return 3

wifi_status = 0
def wifi_status():
	# 0: None 1: Started Scan 2: Finished
	return 2

def wifi_get_count():
	return 3

def wifi_get_ap_name(nIndex):
	return ("ap_name(%d)" %nIndex)
	#return "dummy wifi_get_ap_name"

def wifi_get_ap_dBm(nIndex):
	return nIndex + random.randrange(50, 127)
	#return "dummy wifi_get_ap_dBm"

#bluetooth scan
def bt_enable():
	print "dummy bt_enable"
	return 1


def bt_start():
	print "dummy bt_start"
	return 5

def bt_disable():
	print "dummy bt_disable"
	return 0

bt_status = 0
def bt_status():
	# 0: None 1: Started Scan 2: Finished
	return  2

def bt_get_count():
	return 5

def bt_get_bdaddr(nIndex):
	mac = []
	for i in range(6):
		mac.append('{0:02X}'.format(random.randrange(0, 255)))
	return ":".join(mac)

	#return "00:11:YY:ZZ"

def bt_get_name(nIndex):
	return ("mybt(%d)" %nIndex)


#carmera
def cameraInit():
	print "dummy cameraInit"

def statusCheck():
	print "dummy statusCheck"
	return 3

def statusUpdate(status):
	print ("dummy statusUpdate %s" %status)
	return 1


#battery
def battery_get_voltage():
	print ("dummy battery_get_voltage")
	return "3.87V"

#lcd_off
def lcd_off():
	print "lcd_off"
	return 0

#storage
def storage_size():
	print ("dummy storage_size")
	return 16

def storage_test():
	print ("dummy storage_size")
	return 1

#power off
def power_off():
	return 1


#cpu
cpu_stress = 0
def cpu_stress_start():
	global cpu_stress
	cpu_stress = 0
	print "dummy cpu_stress_start"

def cpu_get():
	global cpu_stress

	print "cpu_get"
	if cpu_stress < 100:
		cpu_stress += 10

	#ret = ("%d%" %cpu_stress)
	#ret =  ("%s%%" %cpu_stress) 
	return cpu_stress
	#print "dummy cpu_get %s" %cpu_stress
	#return "100%"

def cpu_stress_end():
	global cpu_stress
	cpu_stress = 0
	print "dummy cpu_stress_end"


#earphone
def earjack_check():
	# 0 / 1
	return 0

#sound
def sound_play_start():
	print "dummy sound_play_start"
def sound_play_stop():
	print "dummy sound_play_stop"
def sound_play_status():
	#0 : stoped , 1 : playing
	print "dummy sound_play_status"
	return 0

#speaker	
def sound_speaker_left_on():
	print "dummy sound_speaker_left_on"
def sound_speaker_right_on():
	print "dummy sound_speaker_right_on"
def sound_speaker_both_on():
	print "dummy sound_speaker_both_on"
def sound_speaker_both_off():
	print "dummy sound_speaker_both_off"

#earjack
def sound_earjack_is_connedted():
	print "dummy sound_earjack_is_connedted"
def sound_earjack_left_on():
	print "dummy sound_earjack_left_on"
def sound_earjack_right_on():
	print "dummy sound_earjack_right_on"
def sound_earjack_both_on():
	print "dummy sound_earjack_both_on"
def sound_earjack_both_off():
	print "dummy sound_earjack_both_off"

#record
def record_start():
	print "dummy record_start"
def record_stop():
	print "dummy record_stop"
def record_play_start():
	print "dummy record_play_start"
def record_play_stop():
	print "dummy record_play_stop"	


#param
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

arr_param = [
	"TSH7AUDN00014A", #[PARAM_INFO_SERIAL_NUM, ""], 
	"5C:51:4F:74:EE:B0", #[PARAM_INFO_WIFI_MAC, ""], 
	"00:1F:4F:F6:24:E3", #[PARAM_INFO_BT_ADDRESS, "00:1F:4F:F6:24:E3"], 
	"", #[PARAM_INFO_ACC_OFFSET, ""], 
	"", #[PARAM_INFO_MAG_OFFSET, ""], 
	"", #[PARAM_INFO_GYRO_OFFSET, ""], 
	"", #[PARAM_INFO_WV_KEYBOX, ""]
	"", #[PARAM_INFO_RESERVED01, ""]
	"", #[PARAM_INFO_RESERVED02, ""]
	"", #[PARAM_INFO_RESERVED03, ""]
	"", #[PARAM_INFO_TSP_TYPE, ""]
]

def paramClear(pid):
	#input: int id
	#outpu: int
	print ("dummy paramClear: %d" %pid)
	arr_param[pid] = ""
	return 1

def paramRead(pid):
	#input: int id, char *buf 
	#outpu: char*
	
	print ("dummy paramRead: %s %s" %(pid, arr_param[pid]))
	return arr_param[pid]

	#return "hello world"

def paramWrite(pid, buf):

	arr_param[pid] = buf
	print ("dummy paramWrite: %d %s" %(pid, buf))
	return 1

def mmcblkFormat(blk_no, fs_type):
	#input:int blk_no, int fs_type
	#output int
	print "dummy mmcblkFormat %s ,%s" %(blk_no, fs_type)
	#extern int mmcblkFormat(int blk_no, int fs_type);
	return 0

def efsWrite(efs_path, param_data):
	print "dummy efsWrite %s, %s" %(efs_path, param_data)
	#extern int efsWrite(char *efs_path, char *param_data);
	return 0

def mountCheck(mountpoint):
	#extern int mountCheck(char *mountpoint);
	print "dummy mountCheck"
	return 0

def mmcblkMount(blk_no, fs_type, mountpoint):
	#extern int mmcblkMount(int blk_no, int fs_type, char *mountpoint);
	print "dummy mmcblkMount"
	return 0


def systemReboot(reboot_reason):
	print "dummy systemReboot %s" %reboot_reason
	return 1

def releaseUpdate(ums_dir, recovery_file, md5_file, package_file):
	print "dummy releaseUpdate"
	return 1


def umsEnable():
	print "dummy umsEnable"
	return 1

def umsDisable():
	print "dummy umsDisable"
	return 1	

def usbState():
	print "dummy usbState"
	return 1

def initJigLed():
	print "dummy initJigLed"
	return 1

def toggleJigLed(on_off):
	#print "dummy initJigLed %d" %on_off
	return 1
