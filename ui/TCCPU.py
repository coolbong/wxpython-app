#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

import TC
import TCBase
import TCBaseLabel

class Test(TCBase.Base):

	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="CPU STRESS TEST", tc=TC.TCCPU)
		self.InitUI()
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.Show()

	def InitDevice(self):
		print ("Device Init %s" %self.title)
		self.CpuStart()
		print ("Device Init %s CPU Start returned" %self.title)


	def Finalize(self):
		print ("Device Finalize %s" %self.title)
		self.CpuEnd()

	def InitUI(self):
		self.time = 0
		self.lblSec 		= TCBaseLabel.MpLabel(self.panel, -1, '', (80, 80))
		self.lblPercent 	= TCBaseLabel.MpLabel(self.panel, -1, '', (80, 130))
		
		self.InitTimer()

	def InitTimer(self):
		print ("%s : Timer Init" %self.title)
		self.timer = wx.Timer(self)
		self.timer.Start(2000)
		self.Bind(wx.EVT_TIMER, self.OnTimer)

	def OnTimer(self, event):

		self.time += 2000

		ret = self.CpuGet()
		print ("%s : OnTimer" %ret)
		sec = self.time / 1000

		self.lblSec.SetLabel('%d sec' %sec)
		self.lblPercent.SetLabel(("%s%%" %ret))
		


	#device wrapper 
	def CpuStart(self):
		try:
			self.device.cpu_stress_start()
		except:
			self.handleError("Error occured during cpu_stress_start")

	def CpuGet(self):
		try:
			return self.device.cpu_get()
		except:
			self.handleError("Error occured during cpu_get")

	def CpuEnd(self):
		try:
			self.device.cpu_stress_end()
		except:
			self.handleError("Error occured during cpu_stress_end")


	def GoNextTest(self):
		self.Close()
		

if __name__ == '__main__':
	app = wx.App()
	Test(None, title='')
	app.MainLoop()