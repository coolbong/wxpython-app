from collections import OrderedDict
import csv

#assm_dic = {}
assm_dic = OrderedDict()
assm_dic['TEST'] 				= 'ASSEMBLY'
assm_dic['SERIAL'] 				= 'NULL'
assm_dic['STATUS_GPS'] 			= "NT"
assm_dic['STATUS_ACCELEROMETER'] = "NT"
assm_dic['STATUS_MAGNETIC'] 		= "NT"
assm_dic['STATUS_LIGHT'] 		= "NT"
assm_dic['STATUS_EFS'] 			= "NT"
assm_dic['DISP_TEST'] 			= "NT"
assm_dic['TOUCH_TEST'] 			= "NT"
assm_dic['BUTTON_TEST'] 			= "NT"
assm_dic['AUDIO_TEST'] 			= "NT"
assm_dic['EARPHONE_TEST'] 		= "NT"
assm_dic['MIC_TEST'] 			= "NT"
assm_dic['CAMERA_TEST'] 			= "NT"
assm_dic['STORAGE_TEST'] 		= "NT"
assm_dic['LIGHT_TEST'] 			= "NT"
assm_dic['ACCELEROMETER_TEST'] 	= "NT"
assm_dic['MAGNETIC_TEST'] 		= "NT"
assm_dic['GPS_TEST'] 			= "NT"
assm_dic['WIFISCAN_TEST'] 		= "NT"
assm_dic['BTSCAN_TEST'] 			= "NT"
assm_dic['BARCODE_BT_MAC'] 		= "NT"
assm_dic['BARCODE_WIFI_MAC'] 		= "NT"
assm_dic['BARCODE_DEVICE_SN'] 	= "NT"
assm_dic['AGING_TEST'] 			= "NT"

pcb_dic = OrderedDict()
pcb_dic['TEST'] 					= 'PCB'
pcb_dic['SERIAL'] 				= 'NULL'
pcb_dic['STATUS_GPS'] 			= "NT"
pcb_dic['STATUS_ACCELEROMETER'] 	= "NT"
pcb_dic['STATUS_MAGNETIC'] 		= "NT"
pcb_dic['STATUS_LIGHT'] 			= "NT"
pcb_dic['STATUS_EFS'] 			= "NT"
pcb_dic['DISP_TEST'] 			= "NT"
pcb_dic['TOUCH_TEST'] 			= "NT"
pcb_dic['BUTTON_TEST'] 			= "NT"
pcb_dic['AUDIO_TEST'] 			= "NT"
pcb_dic['EARPHONE_TEST'] 		= "NT"
pcb_dic['MIC_TEST'] 				= "NT"
pcb_dic['CAMERA_TEST'] 			= "NT"
pcb_dic['STORAGE_TEST'] 			= "NT"
pcb_dic['LIGHT_TEST'] 			= "NT"
pcb_dic['ACCELEROMETER_TEST'] 	= "NT"
pcb_dic['MAGNETIC_TEST'] 		= "NT"
pcb_dic['GPS_TEST'] 				= "NT"
pcb_dic['WIFISCAN_TEST'] 		= "NT"
pcb_dic['BTSCAN_TEST'] 			= "NT"
pcb_dic['BARCODE_BT_MAC'] 		= "NT"
pcb_dic['BARCODE_WIFI_MAC'] 		= "NT"
pcb_dic['BARCODE_DEVICE_SN'] 		= "NT"
pcb_dic['AGING_TEST'] 			= "NT"

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




with open('test.csv', 'wb') as file:
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




read_dic = OrderedDict()

with open("./20131213_test_result.csv", 'r') as file:
	reader = csv.reader(file)

	list_lines = []
	for line in reader:
		list_lines.append(line)

	i = 0
	for item in list_lines[0]:
		read_dic[item] = [list_lines[1][i], list_lines[2][i]]
		i += 1

	print read_dic
	
	#print list_lines
	#data[line['name']).append(int(line['miles']))

