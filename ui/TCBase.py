#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import TC
import sys
sys.path.append('./lib/')
sys.path.append('./native/')


try:
	import mptest as device
except ImportError as exc:
	import dummy as device
	print sys.stderr.write("Error: fail to import device module".format(exc))


import code128 as barcode
import wxpil
import efs

import TCBaseLabel
from TCBaseDialog import MpDialog

from wx.lib.pubsub import Publisher




class Base(wx.Frame):

	PARAM_INFO_SERIAL_NUM 	= 0
	PARAM_INFO_WIFI_MAC 		= 1
	PARAM_INFO_BT_ADDRESS 	= 2
	PARAM_INFO_ACC_OFFSET 	= 3
	PARAM_INFO_MAG_OFFSET 	= 4
	PARAM_INFO_GYRO_OFFSET 	= 5
	PARAM_INFO_WV_KEYBOX 	= 6
	PARAM_INFO_WV_KEYBOX 	= 6
	PARAM_INFO_RESERVED01 	= 7
	PARAM_INFO_RESERVED02 	= 8
	PARAM_INFO_RESERVED03 	= 9
	PARAM_INFO_TSP_TYPE 		= 10

	def __init__(self, parent, title, tc):
		super(Base, self).__init__(parent, title=title, size=(1280, 800))
		
		self.parent = parent
		self.tc = tc
		self.title = title
		#native interface
		self.device = device
		self.dialog = MpDialog
		
		#barcode
		self.barcode = barcode
		self.wxpil = wxpil
		self.efs = efs

		#timer
		self.timegap = 300


		self.InitDevice()
		self.InitBaseUI()
		self.Centre()

	def InitDevice(self):
		print "base device init"

	def InitBaseUI(self):
		self.panel = wx.Panel(self, -1)

		#default black
		self.panel.SetBackgroundColour(wx.BLACK)

		#default button font
		self.btnFont = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.BOLD)

		self.lblTitle = TCBaseLabel.MpLabel(self.panel, -1, self.title, (8,8))
		self.InitResultUI()
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		

	def InitResultUI(self):
		self.btnBack = wx.Button(self.panel, label="BACK", pos=(294, 720), size=(200, 55))
		self.btnFail = wx.Button(self.panel, label="FAIL", pos=(540, 720), size=(200, 55))
		self.btnPass = wx.Button(self.panel, label="PASS", pos=(796, 720), size=(200, 55))

		self.btnBack.SetFont(self.btnFont)
		self.btnFail.SetFont(self.btnFont)
		self.btnPass.SetFont(self.btnFont)

		self.btnBack.Bind(wx.EVT_LEFT_UP, self.OnBackClicked)
		self.btnPass.Bind(wx.EVT_LEFT_UP, self.OnPassClicked)
		self.btnFail.Bind(wx.EVT_LEFT_UP, self.OnFailClicked)

	def HideTitleLbl(self):
		self.lblTitle.Hide()

	def ShowTitleLbl(self):
		self.lblTitle.Show()

	def HideResultBtn(self):
		self.btnBack.Hide()
		self.btnPass.Hide()
		self.btnFail.Hide()

	def ShowResultBtn(self):
		self.btnBack.Show()
		self.btnPass.Show()
		self.btnFail.Show()


	def OnBackClicked(self, e):
		self.Close()

	def OnPassClicked(self, e):
		print "OnPassClicked"
		self.SendPass()
		self.GoNextTest()

	def OnFailClicked(self, e):
		print "OnFailClicked"
		self.SendFail()
		self.Close()

	def SendPass(self):
		msg = ["True", self.tc]
		Publisher().sendMessage(("MPTest.result"), msg)

	def SendFail(self):
		msg = ["False", self.tc]
		Publisher().sendMessage(("MPTest.result"), msg)

	

	def OnClose(self, evt):
		#if self.timer != None:
		#	self.timer.Stop()
		#	del self.timer
		msg = ["Close", self.tc]
		Publisher().sendMessage(("MPTest.result"), msg)

		self.Finalize()
		self.Destroy()

	def handleError(self, msg):
		dial = self.dialog(None, msg, self.OnHandleError)
		dial.ShowModal()

	def OnHandleError(self, evt):
		if evt.GetId() == wx.ID_OK:
			self.Destroy()


	def Finalize(self):
		print "base finalize"

	#hal interface wrapper
	def ReadParam(self, id):
		try:
			return self.device.paramRead(id)
		except:
			self.handleError("Error occured during paramRead")




if __name__ == '__main__':

	app = wx.App()
	Base(None, title='Base TEST')
	app.MainLoop()