#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

import TC
import TCBase
from TCBaseLabel import MpLabel


class Test(TCBase.Base):

	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="ACCELERROMETER TEST", tc=TC.TCSSAccellerometer)
		self.parent = parent
		self.InitUI()
		self.InitTimer()
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.SetBackgroundColour('black')
		self.Show()

	def InitDevice(self):
		try:
			print ("Device Init %s" %self.title)
			self.device.acc_start()
		except:
			print "Unexpected error"

	def Finalize(self):
		try:
			print ("Device Finalize %s" %self.title)
			self.device.acc_stop()
		except:
			print "Unexpected error"

	def InitUI(self):
		self.lbl_x = MpLabel(self.panel, -1, "x = 0.0", (120, 80))
		self.lbl_y = MpLabel(self.panel, -1, "y = 0.0", (120, 130))
		self.lbl_z = MpLabel(self.panel, -1, "z = 0.0", (120, 180))

	def InitTimer(self):
		self.timer = wx.Timer(self)
		self.timer.Start(self.timegap)
		self.Bind(wx.EVT_TIMER, self.OnTimer)

	def OnTimer(self, event):
		data = "0:0:0"
		length = 0
		try:
			data = self.device.acc_get_data()
		except:
			print ("%s: acc_get_data err" %self.title)

		list = data.split(",")

		length = len(list)

		if length != 0:
			x, y, z = list[0].split(":")
			if abs(float(x)) > 8.5 :
				self.lbl_x.SetForegroundColour((255,0,0))
			else : 
				self.lbl_x.SetForegroundColour((255,255,255))

			if abs(float(y)) > 8.5 :
				self.lbl_y.SetForegroundColour((255,0,0))
			else : 
				self.lbl_y.SetForegroundColour((255,255,255))

			if abs(float(z)) > 8.5 :
				self.lbl_z.SetForegroundColour((255,0,0))
			else : 
				self.lbl_z.SetForegroundColour((255,255,255))
				
			
			self.lbl_x.SetLabel("x = %s" %x)
			self.lbl_y.SetLabel("y = %s" %y)
			self.lbl_z.SetLabel("z = %s" %z)

	def GoNextTest(self):
		print "GoNextTest"
		self.Close()
		
if __name__ == '__main__':
	app = wx.App()
	Test(None, title='')
	app.MainLoop()