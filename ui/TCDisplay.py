#!/usr/bin/python
# -*- coding: utf-8 -*-
# TBD : gradient, 

import wx
import TC
import TCBase
import TCTouch as nextTC

class Test(TCBase.Base):

	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="DISPLAY/HDMI TEST", tc=TC.TCDisplay)
		self.InitUI()
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.Centre()
		self.Show()

	def InitDevice(self):
		print ("Device Init %s" %self.title)
		#self.SpeakerBothOn()
		#self.PlayStart()
		

	def Finalize(self):
		print ("Device Finalize %s" %self.title)
		#self.PlayStop()
		#self.SpeakerBothOn()

	def InitUI(self):
		#self.panel.SetBackgroundColour('red')
		self.panel.Bind(wx.EVT_PAINT, self.OnPaint)
		self.panel.Bind(wx.EVT_LEFT_UP, self.OnClick)
		self.index = 0

		self.HideResultBtn()
		self.HideTitleLbl()
	
	def OnPaint(self, event):
		if self.index == 0:
			dc = wx.PaintDC(self.panel)
			size = self.panel.GetClientSize()

			height = size.height / 6
			height_mod = size.height % 6
			
			dc.GradientFillLinear((0, 0, size.width, height), '#ff0000', '#000000', wx.EAST)
			dc.GradientFillLinear((0, height , size.width, height), '#ffff00', '#000000', wx.EAST)
			dc.GradientFillLinear((0, (2*height), size.width, height), '#00ff00', '#000000', wx.EAST)
			dc.GradientFillLinear((0, (3*height), size.width, height), '#0000ff', '#000000', wx.EAST)
			dc.GradientFillLinear((0, (4*height), size.width, height), '#ff00ff', '#000000', wx.EAST)
			dc.GradientFillLinear((0, (5*height), size.width, height + height_mod), '#ffffff', '#000000', wx.EAST)


	def OnClick(self, e):
		self.index += 1
		
		if self.index == 1:
			#self.SpeakerRightOn()
			self.panel.SetBackgroundColour('red')
		if self.index == 2:
			#self.SpeakerLeftOn()
			self.panel.SetBackgroundColour('green')
		elif self.index == 3:
			#self.SpeakerRightOn()
			self.panel.SetBackgroundColour('blue')
		elif self.index == 4:
			#self.SpeakerLeftOn()
			self.panel.SetBackgroundColour('white')
		elif self.index == 5:
			#self.SpeakerBothOn()
			self.panel.SetBackgroundColour('black')
			self.ShowResultBtn()
			self.ShowTitleLbl()
		

	def GoNextTest(self):
		nextTC.Test(parent=self.parent, title="")
		print "GoNextTest"
		self.Close()

	#devive wrapper
	def IsPlaying(self):
		try:
			play_flag = self.device.sound_play_status()
			if play_flag == 1:
				return True
			else:
				return False
		except:
			self.handleError("Error occured during sound_play_status")	
	
	def PlayStart(self):
		try:
			self.device.sound_play_start()
		except:
			self.handleError("Error occured during sound_play_start")
	
	def PlayStop(self):
		try:
			self.device.sound_play_stop()
		except:
			self.handelError("Error occured during sound_play_stop")

	def SpeakerLeftOn(self):
		try:
			self.device.sound_speaker_left_on()
		except:
			self.handelError("Error occured during sound_speaker_left_on")

	def SpeakerRightOn(self):
		try:
			self.device.sound_speaker_right_on()
		except:
			self.handelError("Error occured during sound_speaker_right_on")

	def SpeakerBothOn(self):
		try:
			self.device.sound_speaker_both_on()
		except:
			self.handelError("Error occured during sound_speaker_both_on")

	


if __name__ == '__main__':
	app = wx.App()
	Test(None, title='DISPLAY/HDMI TEST')
	app.MainLoop()