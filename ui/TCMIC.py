#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

import TC
import TCBase
import TCCamera as nextTC
from TCBaseLabel import MpLabel


class Test(TCBase.Base):

	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="MIC TEST", tc=TC.TCMIC)
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
		except:
			print "Unexpected error"

	def InitUI(self):
		self.btnRecord = wx.Button(self.panel, label="RECORD && PLAY", pos=(440, 10), size=(400, 60))
		self.btnRecord.SetFont(self.btnFont)
		self.btnRecord.Bind(wx.EVT_LEFT_UP, self.OnRecordClicked)
		
	def OnRecordClicked(self, e):
		print "OnRecordClicked"
		#print self.btnLeft.GetLabel()
		#label = self.btnRecord.GetLabel()

		#if self.btnRecord.IsEnable():
		self.btnRecord.SetLabel("Now Recording ...")
		self.btnRecord.Disable()

		self.RecordStart()
		self.lblRecordInfo = MpLabel(self.panel, label="Now\nRecording\n...", pos=(540, 80))
		self.lblRecordInfo.SetForegroundColour(wx.RED)
		wx.CallLater(6000, self.OnRecordStop)

	def OnRecordStop(self, *args, **kw):
		self.RecordStop()

		self.btnRecord.SetLabel("Now Playing ...")
		self.lblRecordInfo.SetLabel("Now\nPlaying\n...")
		self.lblRecordInfo.SetForegroundColour(wx.BLUE)

		self.PlayRecordedData()
		wx.CallLater(10000, self.OnPlayStop)

	def OnPlayStop(self, *args, **kw):
		self.StopRecordedData()
		
		self.btnRecord.SetLabel("RECORD && PLAY")
		self.btnRecord.Enable()
		self.lblRecordInfo.Hide()
		


	def GoNextTest(self):
		nextTC.Test(parent=self.parent, title="")
		print "GoNextTest"
		self.Close()

	#device wrapper
	def RecordStart(self):
		try:
			#print("Record Start")
			self.device.record_start()
		except:
			self.handelError("Error occured during RecordStart")
	
	def RecordStop(self):
		try:
			#print("Record Stop")
			self.device.record_stop()
		except:
			self.handleError("Error occured during RecordStop")

	def PlayRecordedData(self):
		try:
			#print("Play Recored Data")
			self.device.sound_speaker_both_on()
			self.device.record_play_start()
		except:
			self.handleError("Error occured during RecordStop")

	def StopRecordedData(self):
		try:
			#print("Stop Recored Data")
			self.device.record_play_stop()
		except:
			self.handleError("Error occured during RecordStop")		

	def SpeakerBothOn(self):
		try:
			self.device.sound_speaker_both_on()
		except:
			self.handelError("Error occured during sound_speaker_both_on")


if __name__ == '__main__':
	app = wx.App()
	Test(None, title='')
	app.MainLoop()