#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from threading import Thread
#import threading
import wx

from wx.lib.pubsub import Publisher

import sys
sys.path.append('./ui/')
sys.path.append('./lib/')
sys.path.append("./native/")

import csvexport as csv

import efs
import param
import shell

try:
	import mptest as device
except ImportError as exc:
	import dummy as device
	print sys.stderr.write("Error: fail to import device module".format(exc))





#TC Constans
import TC


#UIBase
from TCBaseLabel import MpLabel
from TCBaseDialog import MpDialog

#Basic
import TCDisplay
import TCTouch
import TCButton
import TCAudio
import TCEarPhone
import TCMIC
import TCCamera
import TCStorage
import TCBarcode
import TCCPU
import TCAging
import TCTSPConfig
import TCUMS


#RF
import TCRFGps
import TCRFWifiScan
import TCRFBtScan

#Sensor
import TCSSLightSensor
import TCSSAccellerometer
import TCSSMagnticField


class MPTest(wx.Frame):

	def __init__(self, parent, title):
		super(MPTest, self).__init__(parent, title=title, size=(1280, 800))

		self.tc_list = {}
		self.Init()
		self.InitUI()
		self.InitPublisher()
		self.Centre()
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.Show()

	def InitPublisher(self):
		Publisher().subscribe(self.OnReciveResult, ("MPTest.result"))
		Publisher().subscribe(self.OnStatusUpdate, ("status.update"))
		#csv.result()

	def OnReciveResult(self, msg):
		#print(msg)
		#print(msg.data[0])
		#print(msg.data[1])
		result, tc = msg.data

		if result == "Close":
			self.OnTestCaseClosed(msg.data)
		else:
			csv.testcase_result(csv.MPTEST_ASM, msg.data)
			self.OnChangeBtn(msg.data)

	def Init(self):
		efs.FormatEfs()
		efs.FormatCache()
		
		efs.MountEfs()
		efs.MountCache()

		csv.init()


	def InitUI(self):

		self.Bind(wx.EVT_CLOSE, self.OnClose)

		panel = wx.Panel(self, -1)
		panel.SetBackgroundColour(wx.BLACK)
		panel.SetAutoLayout(True)

		#button font
		btnFont = wx.Font(17, wx.DECORATIVE, wx.NORMAL, wx.BOLD)

		hbox = wx.BoxSizer(wx.HORIZONTAL)


		leftpanel = wx.Panel(panel, -1)
		rightpanel = wx.Panel(panel, -1)
		leftpanel.SetBackgroundColour(wx.BLACK)
		leftpanel.SetForegroundColour(wx.WHITE)
		rightpanel.SetBackgroundColour(wx.BLACK)
		rightpanel.SetForegroundColour(wx.WHITE)


		vbox1 = wx.BoxSizer(wx.VERTICAL)

		vbox1.Add((-1, 20))

		self.lb_type 	= wx.StaticText(leftpanel, label="TSP Type: %s" %self.GetTspType())
		self.lb_battery 	= wx.StaticText(leftpanel, label="Battery Value: %s" % self.GetBatteryVoltage())

		lb_basictest = wx.StaticText(leftpanel, label="BASIC Test")

		vbox1.Add(self.lb_type, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox1.Add(self.lb_battery, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox1.Add(lb_basictest, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		#btn
		#vbtnBox = wx.BoxSizer(wx.VERTICAL)
		#gridSizer = wx.GridSizer(5, 2, 5, 5)
		gridSizer = wx.GridSizer(4, 2, 5, 5)

		self.btnTCDisplay 	= wx.Button(leftpanel, id=TC.TCDisplay,label="DISPLAY TEST")
		self.btnTCTouch 		= wx.Button(leftpanel, id=TC.TCTouch, label='TOUCH TEST')
		self.btnTCButton 	= wx.Button(leftpanel, id=TC.TCButton, label='BUTTON TEST')
		self.btnTCAudio 		= wx.Button(leftpanel, id=TC.TCAudio, label='AUDIO TEST')
		self.btnTCEarPhone 	= wx.Button(leftpanel, id=TC.TCEarPhone, label='EARPHONE TEST')
		self.btnTCMic 		= wx.Button(leftpanel, id=TC.TCMIC, label='MIC TEST')
		self.btnTCCamera		= wx.Button(leftpanel, id=TC.TCCamera, label='CAMERA TEST')
		self.btnTCStoreage 	= wx.Button(leftpanel, id=TC.TCStorage, label='STORAGE TEST')
		self.btnTCBarcode 	= wx.Button(leftpanel, id=TC.TCBarcode, label='BARCODE TEST')
		self.btnTCCPU 		= wx.Button(leftpanel, id=TC.TCCPU, label='CPU STRESS TEST')
		#self.btnTCAging		= wx.Button(leftpanel, id=TC.TCAging, label="AGING TEST")

		self.btnTCDisplay.SetFont(btnFont)
		self.btnTCTouch.SetFont(btnFont)
		self.btnTCButton.SetFont(btnFont)
		self.btnTCAudio.SetFont(btnFont)
		self.btnTCEarPhone.SetFont(btnFont)
		self.btnTCMic.SetFont(btnFont)
		self.btnTCCamera.SetFont(btnFont)
		self.btnTCStoreage.SetFont(btnFont)
		self.btnTCBarcode.SetFont(btnFont)
		self.btnTCCPU.SetFont(btnFont)
		#self.btnTCAging.SetFont(btnFont)

		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnTCDisplay)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnTCTouch)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnTCButton)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnTCAudio)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnTCEarPhone)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnTCMic)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnTCCamera)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnTCStoreage)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnTCBarcode)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnTCCPU)
		#self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnTCAging)
		

		gridSizer.AddMany([
			(self.btnTCDisplay, 0, wx.EXPAND), 	(self.btnTCTouch, 0, wx.EXPAND),
			(self.btnTCButton, 0, wx.EXPAND), 	(self.btnTCEarPhone, 0, wx.EXPAND),
			(self.btnTCMic, 0, wx.EXPAND), 		(self.btnTCCamera, 0, wx.EXPAND),
			(self.btnTCStoreage, 0, wx.EXPAND), 	(self.btnTCAudio, 0, wx.EXPAND),
			#(self.btnTCBarcode, 0, wx.EXPAND), 	(self.btnTCCPU, 0, wx.EXPAND),	#(self.btnTCAging, 0, wx.EXPAND),
			])

		vbox1.Add(gridSizer, proportion=1, flag=wx.EXPAND)
		vbox1.Add((-1, 20))
		vbox1.Add(wx.StaticLine(leftpanel), 0, wx.EXPAND)

		#RFTest
		lb_rftest =  wx.StaticText(leftpanel, label="RF & SENSOR TEST")
		vbox1.Add(lb_rftest, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		#gridSizer2 = wx.GridSizer(3, 2, 3, 3)
		gridSizer2 = wx.GridSizer(4, 2, 3, 3)

		self.btnLightSensor 	= wx.Button(leftpanel, TC.TCSSLightSensor, label="LIGHT SENSOR TEST")
		self.btnAcceler 		= wx.Button(leftpanel, TC.TCSSAccellerometer,  label="ACCELEROMETER TEST")
		self.btnMagnetic 	= wx.Button(leftpanel, TC.TCSSMagnticField,  label="MAGNETIC FIELD TEST")
		self.btnTCGPS 		= wx.Button(leftpanel, TC.TCRFGps,  label="GPS TEST")
		#self.btnTCWifi 		= wx.Button(leftpanel, TC.TCRFWifi,  label="Wi-Fi TEST")
		#self.btnTCBluetooth 	= wx.Button(leftpanel, TC.TCRFBluetooth,  label="BLUETOOTH TEST")
		self.btnTCWifiScan 	= wx.Button(leftpanel, TC.TCRFWifiScan,  label="Wi-Fi SCAN TEST")
		self.btnTCBTScan 	= wx.Button(leftpanel, TC.TCRFBtScan,  label="BT SCAN TEST")

		#set font
		self.btnLightSensor.SetFont(btnFont)
		self.btnAcceler.SetFont(btnFont)
		self.btnMagnetic.SetFont(btnFont)
		self.btnTCGPS.SetFont(btnFont)
		#self.btnTCWifi.SetFont(btnFont)
		#self.btnTCBluetooth.SetFont(btnFont)
		self.btnTCWifiScan.SetFont(btnFont)
		self.btnTCBTScan.SetFont(btnFont)

		#bind event
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnLightSensor)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnAcceler)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnMagnetic)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnTCGPS)
		#self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnTCWifi)
		#self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnTCBluetooth)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnTCWifiScan)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnTCBTScan)

		gridSizer2.AddMany([
			(self.btnLightSensor, 0, wx.EXPAND), 
			(self.btnMagnetic, 0, wx.EXPAND),
			(self.btnTCWifiScan, 0, wx.EXPAND),
			(self.btnTCBTScan, 0, wx.EXPAND),

			(self.btnTCGPS, 0, wx.EXPAND),
			(self.btnAcceler, 0, wx.EXPAND),
			#(self.btnTCWifi, 0, wx.EXPAND),
			#(self.btnTCBluetooth, 0, wx.EXPAND),

			(self.btnTCBarcode, 0, wx.EXPAND),
			(self.btnTCCPU, 0, wx.EXPAND)
			])
		vbox1.Add(gridSizer2, proportion=1, flag=wx.EXPAND)
		vbox1.Add((-1, 20))

		leftpanel.SetSizer(vbox1)

		## Right panel start
		rightpanel.SetAutoLayout(True)

		status_x_pos = 15
		status_y_pos = 120
		status_lbl_gap = 25

		wx.StaticBox(rightpanel, label='STATUS', pos=(status_x_pos-10, status_y_pos-25), size=(340, 155))
		self.lbl_gps 		= MpLabel(rightpanel, -1,label="GPS:", pos=(status_x_pos, status_y_pos))
		self.lbl_accel 		= MpLabel(rightpanel, -1,label="ACCELEROMETER:", pos=(status_x_pos, status_y_pos + (1 * status_lbl_gap)))
		self.lbl_magnetic	= MpLabel(rightpanel, -1,label="MAGNETIC FIELD SENSOR:", pos=(status_x_pos, status_y_pos + (2 * status_lbl_gap)))
		self.lbl_lsensor 	= MpLabel(rightpanel, -1,label="L-SENSOR:", pos=(status_x_pos, status_y_pos + (3 * status_lbl_gap)))
		self.lbl_efs 		= MpLabel(rightpanel, -1,label="EFS:", pos=(status_x_pos, status_y_pos + (4 *status_lbl_gap)))

		self.lbl_gps.SetFontSize(MpLabel.MEDIUM)
		self.lbl_accel.SetFontSize(MpLabel.MEDIUM)
		self.lbl_magnetic.SetFontSize(MpLabel.MEDIUM)
		self.lbl_lsensor.SetFontSize(MpLabel.MEDIUM)
		self.lbl_efs.SetFontSize(MpLabel.MEDIUM)
		

		#sp button area (tsp config, power off)
		sp_btn_width = 180
		sp_btn_height = 80
		sp_x_pos = 15
		sp_y_pos = 400 - (sp_btn_height/2)
		
		self.btnPower 		= wx.Button(rightpanel, id=TC.TCFuncPower, label="Power", pos=(sp_x_pos, sp_y_pos), size=(sp_btn_width, sp_btn_height))
		self.btnTpsConfig 	= wx.Button(rightpanel, id=TC.TCFuncTSPConfig, label="TSP Config", pos=(sp_x_pos + 200, sp_y_pos), size=(sp_btn_width, sp_btn_height))

		self.btnPower.SetFont(btnFont)
		self.btnTpsConfig.SetFont(btnFont)

		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnPower)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnTpsConfig)


		#function area
		function_x_pos = 15
		function_x2_pos = 215
		function_y_pos = 450
		function_btn_width = 180

		function_btn_y_pos = function_y_pos + 20

		wx.StaticBox(rightpanel, label='Function', pos=(5, function_y_pos), size=(400, 200))

		#self.btnFactoryReset 	= wx.Button(rightpanel, id=TC.TCFuncFactoryReset, label="FORMAT\nSTORAGE", size=(sp_btn_width, sp_btn_height), pos=(function_x2_pos, function_btn_y_pos))
		self.btnFactoryReset 	= wx.Button(rightpanel, id=TC.TCFuncFactoryReset, label="FORMAT\nSTORAGE", size=(sp_btn_width, sp_btn_height), pos=(function_x_pos, function_btn_y_pos+ (10 + sp_btn_height)))
		#self.btnEfsWrite 		= wx.Button(rightpanel, id=TC.TCFuncEfsWrite, label="EFS WRITE", size=(sp_btn_width, sp_btn_height), pos=(function_x_pos, function_btn_y_pos + (10 + sp_btn_height)))
		self.btnSleep 			= wx.Button(rightpanel, id=TC.TCFuncSleep, label="SLEEP", size=(sp_btn_width, sp_btn_height), pos=(function_x2_pos, function_btn_y_pos + (10 + sp_btn_height)))

		#self.btnUmsEnable 		= wx.Button(rightpanel, id=TC.TCFuncUmsEnable, label="UMS ENABLE", size=(sp_btn_width, sp_btn_height), pos=(function_x_pos, function_btn_y_pos + 2 * (10 + sp_btn_height)))
		#self.btnReleaseUpdate	= wx.Button(rightpanel, id=TC.TCFuncRelease, label="RELEASE\n UPDATE", size=(sp_btn_width, sp_btn_height), pos=(function_x2_pos, function_btn_y_pos + 2 * (10 + sp_btn_height)))

		release_bt_width = 380
		release_bt_height = 60

		self.btnUmsEnable	 	= wx.Button(rightpanel, id=TC.TCFuncUmsEnable, label="UMS ENABLE", size=(release_bt_width, release_bt_height), pos=(function_x_pos, 660))
		self.btnReleaseUpdate	= wx.Button(rightpanel, id=TC.TCFuncRelease, label="RELEASE UPDATE", size=(release_bt_width, release_bt_height), pos=(function_x_pos, 730))

		self.btnFactoryReset.SetFont(btnFont)
		#self.btnEfsWrite.SetFont(btnFont)
		self.btnSleep.SetFont(btnFont)
		self.btnUmsEnable.SetFont(btnFont)
		self.btnReleaseUpdate.SetFont(btnFont)

		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnFactoryReset)
		#self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnEfsWrite)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnSleep)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnUmsEnable)
		self.Bind(wx.EVT_BUTTON, self.OnTestBtnClicked, self.btnReleaseUpdate)

		hbox.Add((20, -1))
		hbox.Add(leftpanel, 6, wx.EXPAND)
		hbox.Add((20, -1))
		hbox.Add(rightpanel, 3, wx.EXPAND)
		hbox.Add((20, -1))

		panel.SetSizer(hbox)

		#status check
		self.timer = wx.CallLater(1000, self.OnLoaded)

	def SendPass(self, tc):
		msg = ["True", tc]
		Publisher().sendMessage(("MPTest.result"), msg)
	
	def SendFail(self, tc):
		msg = ["False", tc]
		Publisher().sendMessage(("MPTest.result"), msg)

	def OnLoaded(self, *args, **kw):
		print "Status Checking"
		Thread(target=self.OnDevice).start()
		StatusThread()
		self.InitTimer()

	def InitTimer(self):
		self.timer = wx.Timer(self)
		self.timer.Start(1000)
		self.Bind(wx.EVT_TIMER, self.OnTimer)

	def OnTimer(self, evt):
		self.lb_battery.SetLabel("Battery Value: %s" % self.GetBatteryVoltage())
		
		if self.on_off == True:
			self.ToggleLED(0)
			self.on_off = False
		else:
			self.ToggleLED(1)
			self.on_off = True

	
	def OnStatusUpdate(self, msg):
		print msg
		tc, result = msg.data
		if tc == TC.TCSTGps:
			if result:
				self.lbl_gps.SetLabel("GPS: TRUE")
				self.lbl_gps.SetFontColor(True)
				self.SendPass(TC.TCSTGps)
			else:
				self.lbl_gps.SetLabel("GPS: FALSE")
				self.lbl_gps.SetFontColor(False)
				self.SendFail(TC.TCSTGps)

		if tc == TC.TCSTAcc:
			if result:
				self.lbl_accel.SetLabel("ACCELEROMETER: TRUE")
				self.lbl_accel.SetFontColor(True)
				self.SendPass(TC.TCSTAcc)
			else:
				self.lbl_accel.SetLabel("ACCELEROMETER: FALSE")
				self.lbl_accel.SetFontColor(False)
				self.SendFail(TC.TCSTAcc)

		if tc == TC.TCSTMag:
			if result:
				self.lbl_magnetic.SetLabel("MAGNETIC FIELD SENSOR: TRUE")
				self.lbl_magnetic.SetFontColor(True)
				self.SendPass(TC.TCSTMag)
			else:
				self.lbl_magnetic.SetLabel("MAGNETIC FIELD SENSOR: FALSE")
				self.lbl_magnetic.SetFontColor(False)
				self.SendFail(TC.TCSTMag)

		if tc == TC.TCSTLig:
			if result:
				self.lbl_lsensor.SetLabel("L-SENSOR: TRUE")
				self.lbl_lsensor.SetFontColor(True)
				self.SendPass(TC.TCSTLig)
			else:
				self.lbl_lsensor.SetLabel("L-SENSOR: FALSE")
				self.lbl_lsensor.SetFontColor(False)
				self.SendFail(TC.TCSTLig)

		if tc == TC.TCSTEfs:
			if result:
				self.lbl_efs.SetLabel("EFS: TRUE")
				self.lbl_efs.SetFontColor(True)
				self.SendPass(TC.TCSTEfs)
			else:
				self.lbl_efs.SetLabel("EFS: FALSE")
				self.lbl_efs.SetFontColor(False)
				self.SendFail(TC.TCSTEfs)
		

	def OnTestBtnClicked(self, evt):
		id = evt.GetEventObject().GetId()
		
		if id == TC.TCDisplay:
			if self.tc_list.has_key(TC.TCDisplay) == False:
				self.tc_list[TC.TCDisplay] = TCDisplay.Test(parent=self, title="")
			

		elif id == TC.TCTouch:
			if self.tc_list.has_key(TC.TCTouch) == False:
				self.tc_list[TC.TCTouch] = TCTouch.Test(parent=self, title="")
		elif id == TC.TCButton:
			if self.tc_list.has_key(TC.TCButton) == False:
				self.tc_list[TC.TCButton] = TCButton.Test(parent=self, title="")
		elif id == TC.TCAudio:
			if self.tc_list.has_key(TC.TCAudio) == False:
				self.tc_list[TC.TCAudio] = TCAudio.Test(parent=self, title="")
		elif id == TC.TCEarPhone:
			if self.tc_list.has_key(TC.TCEarPhone) == False:
				self.tc_list[TC.TCEarPhone] = TCEarPhone.Test(parent=self, title="")
		elif id == TC.TCMIC:
			if self.tc_list.has_key(TC.TCMIC) == False:
				self.tc_list[TC.TCMIC] = TCMIC.Test(parent=self, title="")
		elif id == TC.TCCamera:
			if self.tc_list.has_key(TC.TCCamera) == False:
				self.tc_list[TC.TCCamera] = TCCamera.Test(parent=self, title="")
		elif id == TC.TCStorage:
			if self.tc_list.has_key(TC.TCStorage) == False:
				self.tc_list[TC.TCStorage] = TCStorage.Test(parent=self, title="")
		elif id == TC.TCBarcode:
			if self.tc_list.has_key(TC.TCBarcode) == False:
				self.tc_list[TC.TCBarcode] = TCBarcode.Test(parent=self, title="")
		elif id == TC.TCCPU:
			if self.tc_list.has_key(TC.TCCPU) == False:
				self.tc_list[TC.TCCPU] = TCCPU.Test(parent=self, title="")
		elif id == TC.TCAging:
			if self.tc_list.has_key(TC.TCAging) == False:
				self.tc_list[TC.TCAging] = TCAging.Test(parent=self, title="")

		#RF
		elif id == TC.TCRFGps:
			if self.tc_list.has_key(TC.TCRFGps) == False:
				self.tc_list[TC.TCRFGps] = TCRFGps.Test(parent=self, title="")
		elif id == TC.TCRFWifi:
			#if self.tc_list.has_key(TC.TCRFWifi) == False:
			#self.tc_list[TC.TCRFWifi] = TCRFWifi.Test(parent=self, title="")
			print id
		elif id == TC.TCRFBluetooth:
			#if self.tc_list.has_key(TC.TCRFBluetooth) == False:
			#self.tc_list[TC.TCRFBluetooth] = TCRFBluetooth.Test(parent=self, title="")
			print id
		elif id == TC.TCRFWifiScan:
			if self.tc_list.has_key(TC.TCRFWifiScan) == False:
				self.tc_list[TC.TCRFWifiScan] = TCRFWifiScan.Test(parent=self, title="")
		elif id == TC.TCRFBtScan:
			if self.tc_list.has_key(TC.TCRFBtScan) == False:
				self.tc_list[TC.TCRFBtScan] = TCRFBtScan.Test(parent=self, title="")
		#Sensor
		elif id == TC.TCSSLightSensor:
			if self.tc_list.has_key(TC.TCSSLightSensor) == False:
				self.tc_list[TC.TCSSLightSensor] = TCSSLightSensor.Test(parent=self, title="")
		elif id == TC.TCSSAccellerometer:
			if self.tc_list.has_key(TC.TCSSAccellerometer) == False:
				self.tc_list[TC.TCSSAccellerometer] = TCSSAccellerometer.Test(parent=self, title="")
		elif id == TC.TCSSMagnticField:
			if self.tc_list.has_key(TC.TCSSMagnticField) == False:
				self.tc_list[TC.TCSSMagnticField] = TCSSMagnticField.Test(parent=self, title="")

		#function
		elif id == TC.TCFuncPower:
			#print id
			self.Quit()
		elif id == TC.TCFuncTSPConfig:
			if self.tc_list.has_key(TC.TCFuncTSPConfig) == False:
				self.tc_list[TC.TCFuncTSPConfig] = TCTSPConfig.Test(parent=self, title="")
		elif id == TC.TCFuncFactoryReset:
			print id
			self.OnFormatStorage()
		elif id == TC.TCFuncEfsWrite:
			print id
			self.OnEfsWriteButton()
		elif id == TC.TCFuncSleep:
			self.Sleep()
			#print id
			#self.NotYet()
		elif id == TC.TCFuncUmsEnable:
			if self.tc_list.has_key(TC.TCFuncUmsEnable) == False:
				self.tc_list[TC.TCFuncUmsEnable] = TCUMS.Test(parent=self, title="")
		elif id == TC.TCFuncRelease:
			print id
			#self.NotYet()
			self.OnReleaseUpdate()
		elif id == TC.TCFuncResultReport:
			print id
			self.NotYet()
		else:
			print btnId

	def Quit(self):
		dial = MpDialog(self, 'Are you sure to quit?', self.OnDialogQuit)
		dial.ShowModal()
		
	def OnDialogQuit(self, evt):
		if evt.GetId() == wx.ID_OK:
			print "MP Test will be close"
			self.Close()
			shell.systemoff()

	def OnFormatStorage(self):
		dial = MpDialog(self, "Wanna format?", self.OnDialFormatStorage)
		dial.ShowModal()

	def OnDialFormatStorage(self, evt):
		if evt.GetId() == wx.ID_OK:
			shell.umount_cache()
			efs._Format(efs.MMCBLK_ID_CACHE, efs.FS_T_VFAT)
			efs.MountCache()

	def NotYet(self):
		dial = MpDialog(self, 'Not Yet !!', self.OnDialogNotYet)
		dial.ShowModal()
	
	def OnDialogNotYet(self, evt):
		if evt.GetId() == wx.ID_OK:
			print "Dialog Not Yet"

	def OnReleaseUpdate(self):
		#dial = MpDialog(self, 'UMS 영역을 활성화 하시겠습니까?', self.OnDialUMSEnable)
		#dial.ShowModal()
		dial = MpDialog(None, '릴리즈 업데이트를 진행하시겠습니까??', self.OnDialReleaseUpdate)
		dial.ShowModal()

	#not use
	def OnDialUMSEnable(self, evt):
		if evt.GetId() == wx.ID_OK:
			#self.EnableUMS()
			dial = MpDialog(None, '릴리즈 업데이트를 진행하시겠습니까??', self.OnDialReleaseUpdate)
			dial.ShowModal()
		


	def OnDialReleaseUpdate(self, evt):
		if evt.GetId() == wx.ID_OK:
			print "Recovey mode"
			device.releaseUpdate("/cache", "recovery.img", "recovery.img.md5", "ITP-E410WP_SKP01.0.5.1_NOUTC_WIPEOUT.zip")
		


	def CheckParamData(self):
		result = []
		result.append(param.ReadParamSN())
		result.append(param.ReadParamWIFI())
		result.append(param.ReadParamBT())
		result.append(param.ReadParamTSP())

		if None in result or "" in result:
			print result
			return False
		else:
			return True

	def CheckEFSData(self):
		result = []
		#result.append(efs.ReadBT())
		#result.append(efs.ReadSN())
		#result.append(efs.ReadTsp())
		#result.append(efs.ReadWifi())
		
		if None in result or "" in result:
			print result
			return False
		else:
			return True


	def OnEfsWriteButton(self):
		if self.CheckParamData() == False:
			dial = MpDialog(self, "PARAM 영역에 올바른 데이터가 들어있지 않습니다. \nBAR CODE 화면으로 이동하여 올바른 데이터를 입력하시겠습니까?", self.OnDialogEfsWrite)
			dial.ShowModal()
		else:
			print "hello"

	def OnDialogEfsWrite(self, evt):
		if evt.GetId() == wx.ID_OK:
			if self.tc_list.has_key(TC.TCBarcode) == False:
				self.tc_list[TC.TCBarcode] = TCBarcode.Test(parent=self, title="")


	#Testcase Result Listener
	def OnChangeBtn(self, msg):
		#flag = msg[0]
		#id = msg[1]

		strFlag, id = msg
		if strFlag == "True":
			flag = True
		else:
			flag = False
		button = None

		if id == TC.TCDisplay:
			button = self.btnTCDisplay
		elif id == TC.TCTouch:
			button = self.btnTCTouch
		elif id == TC.TCButton:
			button = self.btnTCButton
		elif id == TC.TCAudio:
			button = self.btnTCAudio
		elif id == TC.TCEarPhone:
			button = self.btnTCEarPhone
		elif id == TC.TCMIC:
			button = self.btnTCMic
		elif id == TC.TCCamera:
			button = self.btnTCCamera
		elif id == TC.TCStorage:
			button = self.btnTCStoreage
		elif id == TC.TCBarcode:
			button = self.btnTCBarcode
		elif id == TC.TCCPU:
			button = self.btnTCCPU
		elif id == TC.TCAging:
			button = self.btnTCAging
		elif id == TC.TCRFGps:
			button = self.btnTCGPS
		elif id == TC.TCRFWifiScan:
			button = self.btnTCWifiScan
		elif id == TC.TCRFBtScan:
			button = self.btnTCBTScan
		elif id == TC.TCSSLightSensor:
			button = self.btnLightSensor
		elif id == TC.TCSSAccellerometer:
			button = self.btnAcceler
		elif id == TC.TCSSMagnticField:
			button = self.btnMagnetic

		if button == None:
			return

		if flag == True:
			button.SetForegroundColour(wx.BLUE)
		elif flag == False:
			button.SetForegroundColour(wx.RED)

	def OnTestCaseClosed(self, msg):
		#print msg
		strFlag, tc_id = msg
		if tc_id == TC.TCFuncTSPConfig:
			self.lb_type.SetLabel("TSP Type: %s" %self.GetTspType())

		if self.tc_list.has_key(tc_id):
			#print "deleted id: %s" %tc_id
			del self.tc_list[tc_id]

	def handleError(self, msg):
		dial = MpDialog(None, msg, self.OnDialogHandleError)
		dial.ShowModal()

	def OnDialogHandleError(self, evt):
		 if evt.GetId() == wx.ID_OK:
			self.Destroy()

	def OnDevice(self):
		result = self.EnableBlueTooth()
		print "bluetooth enable returned %d" %result
		result = self.InitLED()
		self.on_off = True
		print "JigLed init returned %d" %result


	
	#device wrapper
	def EnableBlueTooth(self):
		try:
			device.bt_disable()
			return device.bt_enable()
		except:
			self.handleError("Error occured during bt_enable")

	def InitLED(self):
		try:
			return device.initJigLed()
		except:
			self.handleError("Error occured during initJigLed")

	def ToggleLED(self, on_off):
		try:
			return device.toggleJigLed(on_off)
		except:
			self.handleError("Error occured during toggleJigLed")		

	def EnableUMS(self):
		try:
			return device.umsEnable()
		except:
			self.handleError("Error occured during umsEnable")

	def DisableUMS(self):
		try:
			return device.umsDisable()
		except:
			self.handleError("Error occured during usmDisable")
		


	def GetTspType(self):
		try:
			#return "Unknown"
			ret = device.paramRead(10)
			if ret == "A":
				return "HEESUNG"
			elif ret == "B":
				return "LGIT"
			else:
				return "Unknown"
		except:
			self.handleError("Error occured during tsp type")

	def GetBatteryVoltage(self):
		try:
			return device.battery_get_voltage()
		except:
			self.handleError("Error occured during lcd_off")


	def Sleep(self):
		try:
			device.lcd_off()
		except:
			self.handleError("Error occured during lcd_off")

	def PowerOff(self):
		try:
			device.power_off()
		except:
			self.handleError("Error occured during power_off")

	def Finalize(self):
		try:
			device.bt_disable()
		except:
			print "bt_diable error"

		try:
			device.cpu_stress_end()
		except:
			print "cpu_end error"

		#unmount  cache, factory
		shell.umount_efs()
		shell.umount_cache()

	def OnClose(self, evt):
		self.Finalize()
		self.Destroy()

class StatusThread(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.start()    # start the thread

	#----------------------------------------------------------------------
	def run(self):
		time.sleep(0.2)
		wx.CallAfter(self.reportStatus, TC.TCSTGps, self.CheckGps())
		time.sleep(0.2)
		wx.CallAfter(self.reportStatus, TC.TCSTAcc, self.CheckAccelerometer())
		time.sleep(0.2)
		wx.CallAfter(self.reportStatus, TC.TCSTMag, self.CheckMagnetic())
		time.sleep(0.2)
		wx.CallAfter(self.reportStatus, TC.TCSTLig, self.CheckLightSensor())
		time.sleep(0.2)
		wx.CallAfter(self.reportStatus, TC.TCSTEfs, self.CheckEfs())
		time.sleep(0.2)
		#wx.CallAfter(Publisher().sendMessage, "status.update", "Thread finished!")

	#----------------------------------------------------------------------
	def reportStatus(self, testname, result):
		msg = [testname, result]
		Publisher().sendMessage("status.update", msg)


	def CheckGps(self):
		try:
			if device.gps_check() == 1:
				return True
			else:
				return False
		except:
			self.handleError("Error occured during gps_check")

	def CheckAccelerometer(self):
		try:
			if device.acc_check() == 1:
				return True
			else:
				return False
		except:
			self.handleError("Error occured during acc_check")

	def CheckMagnetic(self):
		try:
			if device.mag_check() == 1:
				return True
			else:
				return False
		except:
			self.handleError("Error occured during mag_check")
	
	def CheckLightSensor(self):
		try:
			if device.light_check() == 1:
				return True
			else:
				return False
		except:
			self.handleError("Error occured during light_check")


	def CheckEfs(self):
		try:
			result = []
			#result.append(efs.ReadBT())
			#result.append(efs.ReadSN())
			#result.append(efs.ReadTsp())
			#result.append(efs.ReadWifi())

			result.append(efs.MountCheckEfs())
			result.append(efs.MountCheckCache())

			print result
			if False in result:
				return False
			else:
				return True

		except:
			self.handleError("Error occured during efs")


if __name__ == '__main__':
	app = wx.App()
	MPTest(None, title='MPTest')
	app.MainLoop()