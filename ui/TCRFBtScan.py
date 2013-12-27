#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

import TC
import TCBase
import TCBaseLabel

BT_STATUS_NONE = 0
BT_STATUS_START_SCAN = 1
BT_STATUS_FINISHED = 2

class Test(TCBase.Base):

	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="BT SCAN TEST", tc=TC.TCRFBtScan)
		self.parent = parent
		self.lbl_list = {}
		self.InitUI()
		self.InitTimer()
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.SetBackgroundColour('black')
		self.Show()

	def InitDevice(self):
		print ("Device Init %s" %self.title)
		self.StartBTScan()


	def Finalize(self):
		try:
			print ("Device Finalize %s" %self.title)
			#self.device.bt_disable()
		except:
			print "Unexpected error"


	def InitUI(self):
		#self.panel = wx.Panel(self, -1)
		self.panel.SetBackgroundColour(wx.BLACK)
		pos_x_1 = 100
		pos_x_2 = 640

		self.lblGuide = TCBaseLabel.MpLabel(self.panel, -1, 'Scanning...', (pos_x_1, 45))
		lbl_bt_name 	= TCBaseLabel.MpLabel(self.panel, -1, '[DEVICE]', (pos_x_1, 80))
		lbl_bt_macaddr  = TCBaseLabel.MpLabel(self.panel, -1, '[MAC]', (pos_x_2, 80))

		for i in range(10):
			lbl_name = TCBaseLabel.MpLabel(self.panel, -1, '', (pos_x_1, 130+50 * i))
			lbl_mac = TCBaseLabel.MpLabel(self.panel, -1, '', (pos_x_2, 130+50 * i))
			self.lbl_list[i] = [lbl_name, lbl_mac]


	def GoNextTest(self):
		print "GoNextTest"
		self.Close()

	def InitTimer(self):
		self.timer = wx.Timer(self)
		self.timer.Start(self.timegap + 500)
		self.Bind(wx.EVT_TIMER, self.OnTimer)

	def OnTimer(self, event):
		bt_name = None
		bt_addr = None
		
		bt_status = self.GetBTStatus()

		if bt_status != BT_STATUS_FINISHED:
			return

		self.lblGuide.SetLabel("")
		
		self.cnt = self.GetBtScanCount()
		
		
		if self.cnt > 0:
			for i in range(self.cnt):
				bt_name = self.GetBTName(i)
				bt_addr = self.GetBTAddr(i)
				lbl_name, lbl_mac = self.lbl_list[i]
				lbl_name.SetLabel(bt_name)
				lbl_mac.SetLabel(bt_addr)
		
		self.timer.Stop()
		del self.timer


	#device wrapper
	def StartBTScan(self):
		try:
			return self.device.bt_start()
		except:
			self.handleError("Error occured during bt_start")

	def GetBTStatus(self):
		try:
			return self.device.bt_status()
		except:
			self.handleError("Error occured during bt_status")

	def GetBtScanCount(self):
		try:
			return self.device.bt_get_count()
		except:
			self.handleError("Error occured during bt_get_count")

	def GetBTName(self, idx):
		try:
			return self.device.bt_get_name(idx)
		except:
			self.handleError("Error occured during bt_get_name")

	def GetBTAddr(self, idx):
		try:
			return self.device.bt_get_bdaddr(idx)
		except:
			self.handleError("Error occured during bt_get_bdaddr")

		
if __name__ == '__main__':
	app = wx.App()
	Test(None, title='Wi-Fi SCAN TEST')
	app.MainLoop()