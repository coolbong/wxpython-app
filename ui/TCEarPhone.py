#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx


import TC
import TCBase
import TCMIC as nextTC

class Test(TCBase.Base):

	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="EARPHONE TEST", tc=TC.TCEarPhone)
		self.InitUI()
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.SetBackgroundColour('black')
		self.Show()

	def InitDevice(self):
		self.SpeakerBothOff()
		self.SpeakerBothOn()

	def Finalize(self):
		self.PlayStop()
		self.SpeakerBothOn()

	def InitUI(self):
		self.btnLeft 	= wx.Button(self.panel, label="LEFT (OFF)", pos=(320, 8), size=(200, 55))
		self.btnBoth 	= wx.Button(self.panel, label="BOTH (OFF)", pos=(535, 8), size=(200, 55))
		self.btnRight 	= wx.Button(self.panel, label="RIGHT (OFF)", pos=(750, 8), size=(200, 55))

		self.btnLeft.SetFont(self.btnFont)
		self.btnBoth.SetFont(self.btnFont)
		self.btnRight.SetFont(self.btnFont)
		
		self.btnLeft.Bind(wx.EVT_LEFT_UP, self.OnLeftClicked)
		self.btnBoth.Bind(wx.EVT_LEFT_UP, self.OnBothClicked)
		self.btnRight.Bind(wx.EVT_LEFT_UP, self.OnRightClicked)

		self.timer = wx.CallLater(300, self.OnLoaded)

		
	
	def OnLoaded(self, *args, **kw):
		self.isConnected = self.IsConnected()
		if self.isConnected == False:
			self.PopupEarPhoneConnect()
		#TBD dimmed UI

	def PopupEarPhoneConnect(self):
		self.dial = self.dialog(self, 'Please Connect EarPhone!!', self.DialogResult)
		self.dial.ShowModal()

	def DialogResult(self, e):
		if e.GetId() == wx.ID_OK:
			print "ok"
		else:
			print "cancel"



	def OnLeftClicked(self, e):
		if self.IsPlaying():
			self.SpeakerLeftOn()
		else:
			self.SpeakerLeftOn()
			self.PlayStart()
		self.btnLeft.SetLabel("LEFT (ON)")
		self.btnBoth.SetLabel("BOTH (OFF)")
		self.btnRight.SetLabel("RIGHT (OFF)")

	def OnBothClicked(self, e):
		if self.IsPlaying():
			self.SpeakerBothOn()
		else:
			self.SpeakerBothOn()
			self.PlayStart()

		try:
			self.btnLeft.SetLabel("LEFT (OFF)")
			self.btnBoth.SetLabel("BOTH (ON)")
			self.btnRight.SetLabel("RIGHT (OFF)")
		except:
			print ("OnBothClicked Unexpected error %s" %self.title)

	def OnRightClicked(self, e):
		if self.IsPlaying():
			self.SpeakerRightOn()
		else:
			self.SpeakerRightOn()
			self.PlayStart()

		try:
			self.btnLeft.SetLabel("LEFT (OFF)")
			self.btnBoth.SetLabel("BOTH (OFF)")
			self.btnRight.SetLabel("RIGHT (ON)")
		except:
			print ("OnRightClicked Unexpected error %s" %self.title)

	def GoNextTest(self):
		nextTC.Test(parent=self.parent, title="")
		print "GoNextTest"
		self.Close()

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
			self.device.sound_earjack_left_on()
		except:
			self.handelError("Error occured during sound_speaker_left_on")

	def SpeakerRightOn(self):
		try:
			self.device.sound_earjack_right_on()
		except:
			self.handelError("Error occured during sound_speaker_right_on")

	def SpeakerBothOn(self):
		try:
			self.device.sound_earjack_both_on()
		except:
			self.handelError("Error occured during sound_speaker_both_on")

	def SpeakerBothOff(self):
		try:
			self.device.sound_speaker_both_off()
		except:
			self.handelError("Error occured during sound_speaker_both_on")

	def IsConnected(self):
		try:
			is_connected = self.device.earjack_check()
			if is_connected == 1:
				return True
			else:
				return False
		except:
			handleError("Error occured during earjack_check")	


if __name__ == '__main__':
	app = wx.App()
	Test(None, title='')
	app.MainLoop()