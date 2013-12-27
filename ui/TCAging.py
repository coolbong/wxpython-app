#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

import TC
import TCBase
import TCBaseLabel

class Test(TCBase.Base):

	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="Aging TEST", tc=TC.TCAging)
		self.InitUI()
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.Show()

	def InitDevice(self):
		try:
			print ("Device Init %s" %self.title)
		except:
			print "Unexpected error"
	
	def Finalize(self):
		try:
			print ("Device Finalize %s" %self.title)
		except:
			print "Unexpected error"


	def InitUI(self):
		
		lblSec 		= TCBaseLabel.MpLabel(self.panel, -1, '%d sec', (80, 80))
		lblPercent 	= TCBaseLabel.MpLabel(self.panel, -1, '%d %', (80, 130))
		lblTime 		= TCBaseLabel.MpLabel(self.panel, -1, 'Play Time: 0 sec', (80, 180))

	def GoNextTest(self):
		self.Close()


if __name__ == '__main__':
	app = wx.App()
	Test(None, title='')
	app.MainLoop()