#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

import TC
import TCBase
from TCBaseLabel import MpLabel


class Test(TCBase.Base):

	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="GPS TEST", tc=TC.TCRFGps)
		self.parent = parent
		self.InitUI()
		self.InitTimer()
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.SetBackgroundColour('black')
		self.Show()

	def InitDevice(self):
		try:
			print ("Device Init %s" %self.title)
			self.device.gps_start()
		except:
			print "Unexpected error"

	def Finalize(self):
		try:
			print ("Device Finalize %s" %self.title)
			self.device.gps_end()
		except:
			print "Unexpected error"

	def InitUI(self):
		self.lblStatus			= MpLabel(self.panel, -1, 'STATUS: SATELLITE STATUS', (80, 80))
		self.lblMaxPrn			= MpLabel(self.panel, -1, 'MAX PRN: 31 SNR: 50.0', (650, 80))
		self.lblTimeToFirstFix	= MpLabel(self.panel, -1, 'TIME TO FIRST FIX: 26 sec', (80, 130))
		self.lblLatitude			= MpLabel(self.panel, -1, 'LATITUDE: 37402009', (80, 180))
		self.lblLongitude		= MpLabel(self.panel, -1, 'LONGITUDE:127.1099916', (80, 230))
		self.lblAltitude 		= MpLabel(self.panel, -1, 'ALTITUDE: 112.5m', (80, 280))
		self.lblSpeed 			= MpLabel(self.panel, -1, 'SPEED: 0.0 m/sec', (80, 330))
		self.lblAccuracy 		= MpLabel(self.panel, -1, 'ACCURACY: 5.0 m', (80, 380))
		self.lblNumOfSvcs 		= MpLabel(self.panel, -1, 'NUM OF SVCS: 12', (80, 430))
		
	def InitTimer(self):
		self.timer = wx.Timer(self)
		self.timer.Start(self.timegap)
		self.Bind(wx.EVT_TIMER, self.OnTimer)

	def OnTimer(self, event):
		#self.lblLSensor.SetLabel("VALUE: %d luxes" %self.device.get_lsensor_data())
		fix = None
		prn = None
		snr = None
		speed = None
		svc = None
		acc = None
		lng = None
		lat = None
		alt = None

		self.GpsSync()
		state = self.GpsGetState()
		fix = self.GpsGetTimeFix()
		prn = self.GpsGetPRN()
		snr = self.GpsGetSNR()
		speed = self.GpsGetSpeed()
		svc = self.GpsGetSVC()
		acc = self.GpsGetAcc()
		lng = self.GpsGetLng()
		lat = self.GpsGetLat()
		alt = self.GpsGetAlt()

		self.lblStatus.SetLabel('STATUS: %s STATE' %state)
		self.lblMaxPrn.SetLabel('MAX PRN: %f SNR: %f' %(prn, snr))
		self.lblTimeToFirstFix.SetLabel('TIME TO FIRST FIX: %f sec' %fix)
		self.lblLatitude.SetLabel('LATITUDE: %f' %lat)
		self.lblLongitude.SetLabel('LONGITUDE:%f' %lng)
		self.lblAltitude.SetLabel('ALTITUDE: %fm' %alt)
		self.lblSpeed.SetLabel('SPEED: %f m/sec' %speed)
		self.lblAccuracy.SetLabel('ACCURACY: %f m' %acc)
		self.lblNumOfSvcs.SetLabel('NUM OF SVCS: %f' %svc)




	def GoNextTest(self):
		print "GoNextTest"
		self.Close()

	def GpsSync(self):
		try:
			self.device.gps_sync_data()
		except:
			self.handleError("Error occured during gps_sync_data")

	def GpsGetState(self):
		try:
			#if self.device.gps_get_status() == 0:
			return "SATELLITE"
		except:
			self.handleError("Error occured during gps_get_status")
	
	def GpsGetTimeFix(self):
		try:
			return self.device.gps_get_TimeOfFirstFix()
		except:
			self.handleError("Error occured during gps_get_TimeOfFirstFix")

	def GpsGetPRN(self):
		try:
			return self.device.gps_get_MaxPRM()
		except:
			self.handleError("Error occured during gps_get_MaxPRM")

	def GpsGetSNR(self):
		try:
			return self.device.gps_get_MaxSNRv()
		except:
			self.handleError("Error occured during gps_get_MaxSNRv")

	def GpsGetSpeed(self):
		try:
			return self.device.gps_get_Speed()
		except:
			self.handleError("Error occured during gps_get_Speed")

	def GpsGetSVC(self):
		try:
			return self.device.gps_get_NumOfSVCS()
		except:
			self.handleError("Error occured during gps_get_NumOfSVCS")

	def GpsGetAcc(self):
		try:
			return self.device.gps_get_Accuracy()
		except:
			self.handleError("Error occured during gps_get_Accuracy")
	def GpsGetLng(self):
		try:
			return self.device.gps_get_Longitude()
		except:
			self.handleError("Error occured during gps_get_Longitude")
	def GpsGetLat(self):
		try:
			return self.device.gps_get_Latitude()
		except:
			self.handleError("Error occured during gps_get_Latitude")
	def GpsGetAlt(self):
		try:
			return self.device.gps_get_Altitude()
		except:
			self.handleError("Error occured during gps_get_Altitude")


if __name__ == '__main__':
	app = wx.App()
	Test(None, title='')
	app.MainLoop()