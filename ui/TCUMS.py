#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

import TC
import TCBase
import TCBaseLabel


class Test(TCBase.Base):

	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="UMS Enable", tc=TC.TCFuncUmsEnable)
		self.tsp_type = None
		self.InitUI()
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.Show()

	def InitUI(self):
		btn_width = 480
		btn_height = 200


		pos_x = (1280 - btn_width) / 2
		pos_y = (800 - btn_height) /2

		self.btnDisable = wx.Button(self.panel, label="UMS Disable", pos=(pos_x, pos_y), size=(btn_width, btn_height))
		self.btnDisable.SetFont(self.btnFont)

		self.btnDisable.Bind(wx.EVT_LEFT_UP, self.OnDisableClicked)
		self.HideResultBtn()

	def InitDevice(self):
		print ("Device Init %s" %self.title)
		self.EnableUMS()

	def Finalize(self):
		print ("Device Finalize %s" %self.title)
		self.DisableUMS()
	

	def OnDisableClicked(self, evt):
		print "btn Clicked"
		self.Close()

	def GoNextTest(self):
		self.Close()

	def EnableUMS(self):
		try:
			return self.device.umsEnable()
		except:
			self.handleError("Error occured during umsEnable")

	def DisableUMS(self):
		try:
			return self.device.umsDisable()
		except:
			self.handleError("Error occured during usmDisable")


if __name__ == '__main__':
	app = wx.App()
	Test(None, title='')
	app.MainLoop()