#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

import TC
import TCBase
import TCBaseLabel




TSP_TYPE_A = TC.TCFuncTSPConfig +1 #LGIT
TSP_TYPE_B = TC.TCFuncTSPConfig + 2 #HEESUNG
BACK = TC.TCFuncTSPConfig + 3
REBOOT = TC.TCFuncTSPConfig + 4
TEST_TOP_BTN_ID = TC.TCFuncTSPConfig + 5
TEST_BOT_BTN_ID = TC.TCFuncTSPConfig + 6

class Test(TCBase.Base):

	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="TSP Config", tc=TC.TCFuncTSPConfig)
		self.tsp_type = None
		self.InitUI()
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.Show()

	def InitUI(self):
		btn_width = 280
		btn_height = 200

		pos_gap = 30

		pos_x_1 = pos_gap
		pos_x_2 = pos_gap + btn_width + pos_gap
		pos_x_3 = pos_gap + btn_width + pos_gap + btn_width + pos_gap
		pos_x_4 = pos_gap + btn_width + pos_gap + btn_width + pos_gap + btn_width + pos_gap

		#print pos_x_4 + btn_width

		pos_y = (800 / 2) - (btn_height/2)

		self.btnTypeA = wx.Button(self.panel, TSP_TYPE_A, label="HEESUNG", pos=(pos_x_1, pos_y), size=(btn_width, btn_height))
		self.btnTypeB = wx.Button(self.panel, TSP_TYPE_B, label="LGIT", pos=(pos_x_2, pos_y), size=(btn_width, btn_height))
		

		self.btnTspBack = wx.Button(self.panel, BACK, label="Back", pos=(pos_x_3, pos_y), size=(btn_width, btn_height))
		self.btnReboot = wx.Button(self.panel, REBOOT, label="Reboot", pos=(pos_x_4, pos_y), size=(btn_width, btn_height))


		self.btnTop = wx.Button(self.panel, TEST_TOP_BTN_ID, label=" TOUCH ME", pos=(240, 100), size=(800, 100))
		self.btnBottom = wx.Button(self.panel, TEST_BOT_BTN_ID, label="TOUCH ME", pos=(240, 600), size=(800, 100))

		self.btnTypeA.SetFont(self.btnFont)
		self.btnTypeB.SetFont(self.btnFont)
		self.btnTspBack.SetFont(self.btnFont)
		self.btnReboot.SetFont(self.btnFont)

		self.btnTop.SetFont(self.btnFont)
		self.btnBottom.SetFont(self.btnFont)

		self.btnTypeA.Bind(wx.EVT_LEFT_UP, self.OnTSPBtnClicked)
		self.btnTypeB.Bind(wx.EVT_LEFT_UP, self.OnTSPBtnClicked)
		self.btnTspBack.Bind(wx.EVT_LEFT_UP, self.OnTSPBtnClicked)
		self.btnReboot.Bind(wx.EVT_LEFT_UP, self.OnTSPBtnClicked)

		self.btnTop.Bind(wx.EVT_LEFT_UP, self.OnTSPBtnClicked)
		self.btnBottom.Bind(wx.EVT_LEFT_UP, self.OnTSPBtnClicked)

		self.read_tsp_type = self.GetTspType()
		#print "TSPConfig %s" %tsp_type
		if self.read_tsp_type == "A":
			self.btnTypeA.SetForegroundColour(wx.BLUE)
		elif self.read_tsp_type == "B":
			self.btnTypeB.SetForegroundColour(wx.BLUE)

		self.HideResultBtn()

	def OnTSPBtnClicked(self, evt):
		id = evt.GetEventObject().GetId()
		if id == TSP_TYPE_A:
			print "EFS write param: TYPE A"
			#self.SetTspType("A")
			self.tsp_type = "A"
			self.btnTypeA.SetForegroundColour(wx.BLUE)
			self.btnTypeB.SetForegroundColour(wx.BLACK)
			#self.Close()
		elif id == TSP_TYPE_B:
			print "EFS write param: TYPE B"
			#self.SetTspType("B")
			self.tsp_type = "B"
			self.btnTypeA.SetForegroundColour(wx.BLACK)
			self.btnTypeB.SetForegroundColour(wx.BLUE)
			#self.Close()
		elif id == BACK:
			self.SetTspType(self.tsp_type)
			self.Close()
		elif id == REBOOT:
			self.SetTspType(self.tsp_type)
			self.Reboot()
		elif id == TEST_TOP_BTN_ID:
			color = self.btnTop.GetForegroundColour()
			if color == wx.BLUE:
				self.btnTop.SetForegroundColour(wx.RED)
			else:
				self.btnTop.SetForegroundColour(wx.BLUE)
		elif id == TEST_BOT_BTN_ID:
			color = self.btnBottom.GetForegroundColour()
			if color == wx.BLUE:
				self.btnBottom.SetForegroundColour(wx.RED)
			else:
				self.btnBottom.SetForegroundColour(wx.BLUE)

		else:
			print "unknown type"
		

	def GoNextTest(self):
		self.Close()


	def GetTspType(self):
		try:
			PARAM_INFO_TSP_TYPE = 10
			return self.device.paramRead(PARAM_INFO_TSP_TYPE)
			#return "Unknown"
		except:
			self.handleError("Error occured during tsp type")

	def SetTspType(self, tsp_type):
		if tsp_type == None:
			print "tsp_type is None"
			return
		if tsp_type == self.read_tsp_type:
			print "same tsp_type return"
			return
		try:
			PARAM_INFO_TSP_TYPE = 10
			self.device.paramWrite(self.PARAM_INFO_TSP_TYPE, tsp_type)
			data = self.device.paramRead(self.PARAM_INFO_TSP_TYPE)

			ret = self.efs.NeedFormat()
			print "need Format %s" %ret
			if self.efs.NeedFormat():
				self.efs.Format()

			ret = self.efs.WriteTsp2EFS(data)
			print "efs write result : %s" %ret


			#print ("SetTspType %s" %tsp_type)
		except:
			self.handleError("Error occured during tsp type")	

	def Reboot(self):
		try:
			#return self.device.paramWrite(PARAM_INFO_TSP_TYPE, tsp_type)
			self.device.systemReboot("")
			self.Close()
			print ("Reboot")
		except:
			self.handleError("Error occured during reboot")	



if __name__ == '__main__':
	app = wx.App()
	Test(None, title='')
	app.MainLoop()