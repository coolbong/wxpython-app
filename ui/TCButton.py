#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

import TC
import TCBase
import TCEarPhone as nextTC

from TCBaseLabel import MpLabel


class Test(TCBase.Base):

	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="BUTTON TEST", tc=TC.TCButton)
		#self.device = device
		self.InitUI()
		self.InitTimer()
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.SetBackgroundColour('black')
		self.Show()

	def InitDevice(self):
		try:
			self.device.key_start()
		except:
			print "Unexpected error"

	def Finalize(self):
		try:
			self.device.key_end()
		except:
			print "Unexpected error"


	def InitUI(self):
		self.plusKey = 0
		self.minusKey = 0
		self.powerKey = 0

		self.lblVolumeUp 	= MpLabel(self.panel, -1, 'Volume + ( 0 )', (80, 80))
		self.lblVolumeDown 	= MpLabel(self.panel, -1, 'Volume - ( 0 )', (80, 130))
		self.lblPower 		= MpLabel(self.panel, -1, 'Power ( 0 )', (80, 180))
		
		self.Bind(wx.EVT_KEY_UP, self.OnKeyUpEvent)
		#self.Bind(wx.EVT_CLOSE, self.OnClose)
		
		#self.Bind(wx.EVT_CHAR, self.OnKeyCharEvent)
	
	def InitTimer(self):
		self.timer = wx.Timer(self)
		self.timer.Start(self.timegap)
		self.Bind(wx.EVT_TIMER, self.OnTimer)

	def OnTimer(self, event):
		try:
			keycode = self.device.key_get()
		except:
			keycode = 0
			print "Unexpected error:"

		print keycode

		if keycode == 115:
			self.plusKey += 1
			self.lblVolumeUp.SetLabel("Volume + ( %d )" %self.plusKey)
		elif keycode == 114:
			self.minusKey += 1
			self.lblVolumeDown.SetLabel("Volume - ( %d )" %self.minusKey)
		elif keycode == 116:
			self.powerKey += 1
			self.lblPower.SetLabel("Power ( %d )" %self.powerKey)

	def GoNextTest(self):
		nextTC.Test(parent=self.parent, title="")
		print "GoNextTest"
		self.Close()

	def OnKeyUpEvent(self, evt):
		keycode = evt.GetKeyCode()

		#key pad + : 388
		#key pad - : 390
		#key pad * : 387

		if keycode == 388:
			self.plusKey += 1
			self.lblVolumeUp.SetLabel("Volume + ( %d )" %self.plusKey)
		elif keycode == 390:
			self.minusKey += 1
			self.lblVolumeDown.SetLabel("Volume - ( %d )" %self.minusKey)
		elif keycode == 387:
			self.powerKey += 1
			self.lblPower.SetLabel("Power ( %d )" %self.powerKey)

		print ("key up code: %s" %keycode) 
		

	def OnKeyDownEvent(self, evt):
		keycode = evt.GetKeyCode()
		print ("key down code: %s" %keycode) 


	def OnKeyCharEvent(self, evt):
		keycode = evt.GetKeyCode()
		print ("key char code: %s" %keycode) 


	#def SetLogKeyUp(evt.GetInt())

		

if __name__ == '__main__':
	app = wx.App()
	Test(None, title='')
	app.MainLoop()