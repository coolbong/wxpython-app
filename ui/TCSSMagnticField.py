#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

import TC
import TCBase
from TCBaseLabel import MpLabel


class Test(TCBase.Base):

	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="MAGNETIC FIELD TEST", tc=TC.TCSSMagnticField)
		self.parent = parent
		self.InitUI()
		self.InitTimer()
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.SetBackgroundColour('black')
		self.Show()

	def InitDevice(self):
		try:
			print ("Device Init %s" %self.title)
			self.device.mag_start()
		except:
			print "Unexpected error"

	def Finalize(self):
		try:
			self.device.mag_stop()
			print ("Device Finalize %s" %self.title)
		except:
			print "Unexpected error"

	def InitUI(self):
		self.lbl_x = MpLabel(self.panel, -1, "x = 0.0", (120, 80))
		self.lbl_y = MpLabel(self.panel, -1, "y = 0.0", (120, 130))
		self.lbl_z = MpLabel(self.panel, -1, "z = 0.0", (120, 180))
		self.lbl_a = MpLabel(self.panel, -1, "z = 0.0", (120, 230))


	def InitTimer(self):
		self.timer = wx.Timer(self)
		self.timer.Start(200)
		self.Bind(wx.EVT_TIMER, self.OnTimer)

	def OnTimer(self, event):
		data = "0:0:0"
		try:
			data = self.device.mag_get_data()
			print ("[magnetic]: hal_interface return data: %s" %data)
		except:
			print ("%s: mag_get_data err" %self.title)

		try:
			acc_list = data.split(",")
			size = len(acc_list)
			print ("[magnetic]: data len: %d" %size)
			if size > 1:
				x, y, z, a = acc_list[size-1].split(":")
			else:
				x, y, z, a = acc_list[0].split(":")
		except:
			print "[magnetic]: parsing error"


		self.lbl_x.SetLabel("x = %s" %x)
		self.lbl_y.SetLabel("y = %s" %y)
		self.lbl_z.SetLabel("z = %s" %z)
		self.lbl_a.SetLabel("accuracy = %s" %a)


	def GoNextTest(self):
		print "GoNextTest"
		self.Close()
		
if __name__ == '__main__':
	app = wx.App()
	Test(None, title='')
	app.MainLoop()