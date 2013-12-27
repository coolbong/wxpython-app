#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

import TC
import TCBase
import TCBaseLabel


WIFI_STATUS_NONE = 0
WIFI_STATUS_START_SCAN = 1
WIFI_STATUS_FINISHED = 2

class Test(TCBase.Base):

	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="Wi-Fi SCAN TEST", tc=TC.TCRFWifiScan)
		self.parent = parent
		self.lbl_list = {}
		self.InitUI()
		self.InitTimer()
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.SetBackgroundColour('black')
		self.Show()

	def InitDevice(self):
		print ("Device Init %s" %self.title)
		self.StartWifiScan()


	def Finalize(self):
		try:
			print ("Device Finalize %s" %self.title)
			#self.device.wifi_end()
		except:
			print "Unexpected error"


	def InitUI(self):
		pos_x_1 = 100
		pos_x_2 = 640

		self.lblGuide = TCBaseLabel.MpLabel(self.panel, -1, 'Scanning...', (pos_x_1, 45))
		lbl_wifi_ssid 	= TCBaseLabel.MpLabel(self.panel, -1, '[SSID]', (pos_x_1, 80))
		lbl_wifi_dBm  	= TCBaseLabel.MpLabel(self.panel, -1, '[dBm]', (pos_x_2, 80))

		for i in range(10):
			lbl_ssid = TCBaseLabel.MpLabel(self.panel, -1, '', (pos_x_1, 130+50 * i))
			lbl_dBm = TCBaseLabel.MpLabel(self.panel, -1, '', (pos_x_2, 130+50 * i))
			self.lbl_list[i] = [lbl_ssid, lbl_dBm]

	def GoNextTest(self):
		print "GoNextTest"
		self.Close()

	def InitTimer(self):
		self.timer = wx.Timer(self)
		self.timer.Start(self.timegap + 500)
		self.Bind(wx.EVT_TIMER, self.OnTimer)

	def OnTimer(self, event):
		ap_name = None
		ap_dBm = None
		
		wifi_status = self.GetWifiStatus()

		if wifi_status != WIFI_STATUS_FINISHED:
			return 

		self.lblGuide.SetLabel("")

		self.cnt = self.GetWifiScanCount()
		
		if self.cnt > 0:
			for i in range(self.cnt):
				print ("i : %d" %i)
				ap_name = self.GetWifiAPName(i)
				ap_dBm  = self.GetWifidBm(i)
				lbl_ssid, lbl_dBm = self.lbl_list[i]
				lbl_ssid.SetLabel(ap_name)
				lbl_dBm.SetLabel(str(ap_dBm))

		self.timer.Stop()
		del self.timer

	#device wrapper
	def StartWifiScan(self):
		try:
			return self.device.wifi_start()
		except:
			self.handleError("Error occured during wifi_start")

	def GetWifiStatus(self):
		try:
			return self.device.wifi_status()
		except:
			self.handleError("Error occured during wifi_status")

	def GetWifiScanCount(self):
		try:
			return self.device.wifi_get_count()
		except:
			self.handleError("Error occured during wifi_get_count")

	def GetWifiAPName(self, idx):
		try:
			return self.device.wifi_get_ap_name(idx)
		except:
			self.handleError("Error occured during wifi_get_ap_name")

	def GetWifidBm(self, idx):
		try:
			return self.device.wifi_get_ap_dBm(idx)
		except:
			self.handleError("Error occured during wifi_get_ap_dBm")

		
if __name__ == '__main__':
	app = wx.App()
	Test(None, title='')
	app.MainLoop()