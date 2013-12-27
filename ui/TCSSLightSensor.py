#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

import TC
import TCBase
from TCBaseLabel import MpLabel


class Test(TCBase.Base):

	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="LIGHT SENSOR TEST", tc=TC.TCSSLightSensor)
		self.parent = parent
		self.luxes = ""
		self.InitUI()
		self.InitTimer()
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.SetBackgroundColour('black')
		self.Show()

	def InitDevice(self):
		try:
			print ("Device Init %s" %self.title)
			self.device.light_start()
		except:
			print "Unexpected error"

	def Finalize(self):
		try:
			print ("Device Finalize %s" %self.title)
			self.device.light_stop()
		except:
			print "Unexpected error"

	def InitUI(self):
		self.lblLSensor = MpLabel(self.panel, -1, "", (120, 50))
		self.lblGuide   = MpLabel(self.panel, -1, "Try to hide and reveal a light sensor above", (120, 120))


	def InitTimer(self):
		self.timer = wx.Timer(self)
		self.timer.Start(self.timegap)
		self.Bind(wx.EVT_TIMER, self.OnTimer)

	def OnTimer(self, event):

		data = self.GetLightSeonsorData()

		if data == "":
			return
		else:
			self.luxes = data 
			self.lblLSensor.SetLabel("VALUE: %s luxes" %self.luxes)

	def GoNextTest(self):
		print "GoNextTest"
		self.Close()

	#device wrapper 
	def GetLightSeonsorData(self):
		try:
			return self.device.light_get_data()
		except:
			self.handleError("Error occured during light_get_data")

		
if __name__ == '__main__':
	app = wx.App()
	Test(None, title='')
	app.MainLoop()