#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

import TC
import TCBase
import TCAudio as nextTC
from TCBaseLabel import MpLabel
from wx.lib.pubsub import Publisher


#storage test 
class Test(TCBase.Base):

	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="STORAGE TEST", tc=TC.TCStorage)
		self.InitUI()
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.SetBackgroundColour('black')
		self.Show()

	def InitDevice(self):
		try:
			print ("Device Init %s" %self.title)
		except:
			print "Unexpected error"

	def Finalize(self):
		try:
			print ("Device Finalize %s" %self.title)
			#self.device.
		except:
			print "Unexpected error"

	def InitUI(self):
		self.lblStorage 	= MpLabel(self.panel, -1, 'Movinand: Not Tested', (80, 80))
		self.timer = wx.CallLater(300, self.OnLoaded)

	def OnLoaded(self, *args, **kw):
		self.lblStorage.SetLabel('Movinand(%sG): PASS' %self.GetStorageSize())


	def GoNextTest(self):
		nextTC.Test(parent=self.parent, title="")
		print "GoNextTest"
		self.Close()

	#device wrapper
	def GetStorageSize(self):
		try:
			return self.device.storage_size()
		except:
			self.handleError("Error occured during storage_size")
		

if __name__ == '__main__':
	app = wx.App()
	Test(None, title='')
	app.MainLoop()