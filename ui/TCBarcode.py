#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os.path
import fcntl, socket, struct

import wx

import TC
import TCBase
import TCBaseLabel
#import TCCPU as nextTC
import TCAging as nextTC



class Test(TCBase.Base):

	BITMAP_POS_X = 80
	BITMAP_POS_Y = 80
	

	LABEL_POS_X  = 600
	#LABEL_POS_Y  = 80
	LABEL_GAP  = 20

	SEPERATOR = 150


	BARCODE_BT_LENGTH = 17
	BARCODE_SN_LENGTH = 15


	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="BAR CODE TEST", tc=TC.TCBarcode)
		self.keycodes = []
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

			if self.strBtMac == "":
				return

			if self.strWifiMac == "":
				return

			if self.strDeviceSN == "":
				return 

			self.device.paramWrite(self.PARAM_INFO_BT_ADDRESS, self.strBtMac)
			self.device.paramWrite(self.PARAM_INFO_WIFI_MAC, self.strWifiMac)
			self.device.paramWrite(self.PARAM_INFO_SERIAL_NUM, self.strDeviceSN)

			btmac		= self.device.paramRead(self.PARAM_INFO_BT_ADDRESS)
			wifimac		= self.device.paramRead(self.PARAM_INFO_WIFI_MAC)
			device_sn 	= self.device.paramRead(self.PARAM_INFO_SERIAL_NUM)

			#self.efs.WriteBT2EFS(btmac)
			#self.efs.WriteWifi2EFS(wifimac)
			#self.efs.WriteSN2EFS(device_sn)
		except :
			print "Unexpected error"

	def InitUI(self):
		self.panel.SetBackgroundColour(wx.WHITE)
		self.lblTitle.SetForegroundColour(wx.BLACK)

		self.HideResultBtn()
		self.btnBack.Show()
		

		#step 1 read file sn&mac
		data = self.LoadData()


		if data == None:
			try:
				self.strBtMac 		= self.ReadParam(self.PARAM_INFO_BT_ADDRESS)
				self.strWifiMac 		= self.ReadParam(self.PARAM_INFO_WIFI_MAC)
				self.strDeviceSN 	= self.ReadParam(self.PARAM_INFO_SERIAL_NUM)
				self.strTspType		= self.ReadParam(self.PARAM_INFO_TSP_TYPE)
				print ("strBtMac: %s strWifiMac %s strDeviceSN %s" %(strBtMac, strWifiMac, strDeviceSN))
			except:
				self.strBtMac =  ""
				self.strWifiMac = self.GetWifiMacAddr()
				self.strDeviceSN = ""
				self.strTspType = ""

		else:
			self.strBtMac 		= data[0][1]
			self.strDeviceSN 	= data[1][1]
			self.strWifiMac 		= self.GetWifiMacAddr()
			self.strTspType		= self.ReadParam(self.PARAM_INFO_TSP_TYPE)

		
		self.DrawBtMac(self.strBtMac)
		self.DrawWifiMac(self.strWifiMac)
		self.DrawDeviceSN(self.strDeviceSN)
		self.DrawTspType(self.strTspType)

		self.btnBack.Bind(wx.EVT_CHAR, self.OnKeyCharEvent)
		self.btnBack.SetFocus()

	def LoadData(self):
		datalines = self.efs.ReadSNFile()

		if datalines == None:
			return None

		list = []
		for line in datalines:
			list.append(line.split("="))

		return list


		"""
		filename = "./SN&MAC.txt"
		if os.path.exists(filename) == False:
			return None
		list = []
		with open(filename) as data:
			datalines = (line.rstrip('\r\n') for line in data)
			for line in datalines:
				#print line.split("=")
				list.append(line.split("="))
		return list
		"""
		


	def OnKeyCharEvent(self, evt):
		keycode = evt.GetKeyCode()
		#unichar = evt.GetUnicodeKey()
		if keycode < 256:
			if keycode == 0:
				keyname = "NUL"
			elif keycode < 27:
				keyname = "Ctrl-%s" % chr(ord('A') + keycode-1)
			else:
				keyname = "\"%s\"" % chr(keycode)
		else:
			keyname = "(%s)" % keycode
		#print ("key char code: %s" %keyname)
		self.keycodes.append(keyname)
		print self.keycodes



	def DrawBtMac(self, data):
		## bt mac address
		lblBtMac = TCBaseLabel.MpLabel(self.panel, -1, "BLUETOOTH MAC ADDRESS", (self.LABEL_POS_X,  self.BITMAP_POS_Y))
		lblBtMac.SetFontSize(TCBaseLabel.MpLabel.MEDIUM)
		lblBtMac.SetForegroundColour(wx.BLACK)
		
		lblBtMacData = TCBaseLabel.MpLabel(self.panel, -1, "", (self.LABEL_POS_X, self.BITMAP_POS_Y + self.LABEL_GAP))
		lblBtMacData.SetFontSize(TCBaseLabel.MpLabel.MEDIUM)
		lblBtMacData.SetForegroundColour(wx.BLACK)

		if data == "":
			lblBtMacData.SetLabel("Not available")
			return
		else:
			lblBtMacData.SetLabel(data)

		
		pil = self.barcode.code128_image(data, height=72, thickness=2, quiet_zone=True)
		bitmap = self.wxpil.PilImageToWxBitmap(pil)

		#bitmap = wx.Bitmap("./res/barcode_null.png")
		bitmapCtrl = wx.StaticBitmap(self.panel, -1, bitmap)
		bitmapCtrl.SetPosition((self.BITMAP_POS_X, 80))
		

	def DrawWifiMac(self, data):
		#wifi
		lblWifiMac = TCBaseLabel.MpLabel(self.panel, -1, "WIFI MAC ADDRESS", (self.LABEL_POS_X,  self.BITMAP_POS_Y + self.SEPERATOR))
		lblWifiMac.SetFontSize(TCBaseLabel.MpLabel.MEDIUM)
		lblWifiMac.SetForegroundColour(wx.BLACK)

		lblWifiMacData = TCBaseLabel.MpLabel(self.panel, -1, data, (self.LABEL_POS_X, self.BITMAP_POS_Y + self.SEPERATOR + self.LABEL_GAP))
		lblWifiMacData.SetFontSize(TCBaseLabel.MpLabel.MEDIUM)
		lblWifiMacData.SetForegroundColour(wx.BLACK)

		if data == "":
			lblWifiMacData.SetLabel("Not available")
			return
		else:
			lblWifiMacData.SetLabel(data)


		pil = self.barcode.code128_image(data, height=72, thickness=2, quiet_zone=True)
		bitmap = self.wxpil.PilImageToWxBitmap(pil)
		bitmapCtrl = wx.StaticBitmap(self.panel, -1, bitmap)
		bitmapCtrl.SetPosition((self.BITMAP_POS_X , self.BITMAP_POS_Y + self.SEPERATOR))

	def DrawDeviceSN(self, data):
		#device serial number
		lblDeviceSN = TCBaseLabel.MpLabel(self.panel, -1, "DEVICE S/N", (self.LABEL_POS_X,  self.BITMAP_POS_Y + (2*self.SEPERATOR)))
		lblDeviceSN.SetFontSize(TCBaseLabel.MpLabel.MEDIUM)
		lblDeviceSN.SetForegroundColour(wx.BLACK)

		lblDeviceSNData = TCBaseLabel.MpLabel(self.panel, -1, data, (self.LABEL_POS_X, self.BITMAP_POS_Y + (2*self.SEPERATOR) + self.LABEL_GAP))
		lblDeviceSNData.SetFontSize(TCBaseLabel.MpLabel.MEDIUM)
		lblDeviceSNData.SetForegroundColour(wx.BLACK)

		if data == "":
			lblDeviceSNData.SetLabel("Not available")
			return
		else:
			lblDeviceSNData.SetLabel(data)

		pil = self.barcode.code128_image(data, height=72, thickness=2, quiet_zone=True)
		bitmap = self.wxpil.PilImageToWxBitmap(pil)

		bitmapCtrl = wx.StaticBitmap(self.panel, -1, bitmap)
		bitmapCtrl.SetPosition((self.BITMAP_POS_X , self.BITMAP_POS_Y + (2*self.SEPERATOR)))


	def DrawTspType(self, data):

		lblTspType = TCBaseLabel.MpLabel(self.panel, -1, "Tsp Type", (self.LABEL_POS_X,  self.BITMAP_POS_Y + (3*self.SEPERATOR)))
		lblTspType.SetFontSize(TCBaseLabel.MpLabel.MEDIUM)
		lblTspType.SetForegroundColour(wx.BLACK)

		lblTspTypeData = TCBaseLabel.MpLabel(self.panel, -1, data, (self.LABEL_POS_X, self.BITMAP_POS_Y + (3*self.SEPERATOR) + self.LABEL_GAP))
		lblTspTypeData.SetFontSize(TCBaseLabel.MpLabel.MEDIUM)
		lblTspTypeData.SetForegroundColour(wx.BLACK)

		if data == "":
			lblTspTypeData.SetLabel("Not available")
			return
		else:
			if data == "A":
				data = "HEESUNG"
			elif data == "B":
				data = "LGIT"

			lblTspTypeData.SetLabel(data)
			

		pil = self.barcode.code128_image(data, height=72, thickness=2, quiet_zone=True)
		bitmap = self.wxpil.PilImageToWxBitmap(pil)

		bitmapCtrl = wx.StaticBitmap(self.panel, -1, bitmap)
		bitmapCtrl.SetPosition((self.BITMAP_POS_X , self.BITMAP_POS_Y + (3*self.SEPERATOR)))



	def GoNextTest(self):
		nextTC.Test(parent=self.parent, title="")
		print "GoNextTest"
		self.Close()

	def GetWifiMacAddr(self):
		ifname = 'wlan1'
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
			return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]
		except Exception as e:
			
			print ("error: %s" %e.strerror)
			return ""


	
	


if __name__ == '__main__':
	app = wx.App()
	Test(None, title='')
	app.MainLoop()