#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

import TC
import TCBase
import TCStorage as nextTC

"""
4. test command

Application Action             Test Command                           설명
카메라 테스트 버튼 선택        /usr/bin/fbcam_mptest                  fbcam_mptest 을 실행하고 Preview 를 실행
                               cameraInit();                          (이 때, 카메라 출력이 framebuffer 를 직접 제어하므로 테스트 화면의 버튼은 하단에 표시 요망)

촬영 버튼 선택                 echo "2" > /tmp/camd_status.txt        사진 촬영 후 "/tmp/test.jpg" 에 저장하고, 상태 정보를 갱신한다.
                               statusUpdate(CAMD_RECV_SHUTTER);       [ /tmp/camd_status.txt => 2(CAMD_RECV_SHUTTER) -> 3(CAMD_SNAPSHOT_OK) ]

촬영 사진 표시                 echo "4" > /tmp/camd_status.txt        사진 촬영이 정상적으로 되었으면, Preview 정지하고 촬영된 사진을 표시한다.
(Preview 정지)                 statusUpdate(CAMD_RECV_PREVIEW_STOP);  [ /tmp/camd_status.txt => 4(CAMD_RECV_PREVIEW_STOP) -> 5(CAMD_PREVIEW_STOP_OK) ]

촬영 사진 확인 버튼 선택       echo "0" > /tmp/camd_status.txt        사진 확인 후 버튼을 부트면 다시 Preview 를 시작한다.
(Preview 시작)                 statusUpdate(CAMD_RECV_PREVIEW_START); [ /tmp/camd_status.txt => 0(CAMD_RECV_PREVIEW_START) -> 1(CAMD_PREVIEW_START_OK) ]

카메라 테스트 종료 버튼 선택   echo "6" > /tmp/camd_status.txt        카메라를 끄고 fbcam_mptest 를 종료한다.
                               statusUpdate(CAMD_RECV_EXIT);          [ /tmp/camd_status.txt => 6(CAMD_RECV_EXIT) -> 7(CAMD_EXIT_OK) ]
"""

CAMD_RECV_PREVIEW_START = 0
CAMD_PREVIEW_START_OK = 1
CAMD_RECV_SHUTTER = 2
CAMD_SNAPSHOT_OK = 3
CAMD_RECV_PREVIEW_STOP = 4
CAMD_PREVIEW_STOP_OK = 5
CAMD_RECV_EXIT = 6
CAMD_EXIT_OK = 7
CAMD_STATUS_MAX = 8

#image reference
#http://stackoverflow.com/questions/3502772/wxpython-centering-an-image-in-a-panel
class Test(TCBase.Base):


	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="CAMERA TEST", tc=TC.TCCamera)
		self.InitUI()
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.SetBackgroundColour('black')
		self.Show()

	def InitDevice(self):
		try:
			print ("Device Init %s" %self.title)
			self.device.cameraInit()
		except:
			print "Unexpected error"

	def Finalize(self):
		try:
			print ("Device Finalize %s" %self.title)
			print ("status: %d" %CAMD_RECV_EXIT)
			self.device.statusUpdate(CAMD_RECV_EXIT)
		except:
			print ("Unexpected error Finalize %s" %self.title)

	def InitUI(self):
		y_pos = 60
		
		#self.btnRecord = wx.Button(self.panel, label="RECORD", pos=(170, y_pos), size=(300, 60))
		self.btnRecord = wx.Button(self.panel, label="SNAPSHOT", pos=(60, 755), size=(200, 45))
		#self.btnVerify = wx.Button(self.panel, label="VERIFY", pos=(810, y_pos), size=(300, 60))
		self.btnBack1 = wx.Button(self.panel, label="BACK", pos=(380, 755), size=(200, 45))
		self.btnFail1 = wx.Button(self.panel, label="FAIL", pos=(700, 755), size=(200, 45))
		self.btnPass1 = wx.Button(self.panel, label="PASS", pos=(1020, 755), size=(200, 45))

		self.btnRecord.SetFont(self.btnFont)
		self.btnBack1.SetFont(self.btnFont)
		self.btnFail1.SetFont(self.btnFont)
		self.btnPass1.SetFont(self.btnFont)
		#self.btnVerify.SetFont(self.btnFont)

		self.btnRecord.Bind(wx.EVT_LEFT_UP, self.OnRecordClicked)
		self.btnBack1.Bind(wx.EVT_LEFT_UP, self.OnBackClicked)
		self.btnPass1.Bind(wx.EVT_LEFT_UP, self.OnPassClicked)
		self.btnFail1.Bind(wx.EVT_LEFT_UP, self.OnFailClicked)
		#self.btnVerify.Bind(wx.EVT_LEFT_UP, self.OnVerifyClicked)

		#self.btnCamera = wx.ToggleButton(self.panel, 1, label="NOT YET!!", pos=(440, 8), size=(400, 60))
		#self.Bind(wx.EVT_TOGGLEBUTTON, self.OnCameraClicked, id =1)
		self.HideResultBtn()
		
		

		
	def OnCameraClicked(self, e):
		print "OnCameraClicked"
		label = self.btnCamera.GetLabel()
		print label

	def OnRecordClicked(self, e):
		print "OnRecordClicked"
		try:
			print ("OnRecordClicked %s" %self.title)
			self.device.statusUpdate(CAMD_RECV_SHUTTER)
			self.InitTimer()
		except:
			print ("Unexpected error OnRecordClicked")

	def OnVerifyClicked(self, e):
		print "OnVerifyClicked"
		#jpg = wx.Image(opj("/tmp/test.jpg"), wx.BITMAP_TYPE_JPEG).ConvertToBitmap()

		image_file = '/tmp/test.jpg'
		bitmap = wx.Bitmap('/tmp/test.jpg')
		#img = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		# image's upper left corner anchors at panel coordinates (0, 0)
		bitmap = self.scale_bitmap(bitmap, 640, 400)
		self.bitmap1 = wx.StaticBitmap(self.panel, -1, bitmap, (320, 200))
		#self.panel.Refresh()
		# show some image details
		#str1 = "%s  %dx%d" % (image_file, bmp1.GetWidth(), bmp1.GetHeight()) 
		#parent.SetTitle(str1)

	def scale_bitmap(self, bitmap, width, height):
		image = wx.ImageFromBitmap(bitmap)
		image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
		result = wx.BitmapFromImage(image)
		return result

	def InitTimer(self):
		self.timer = wx.Timer(self)
		self.timer.Start(500)
		self.Bind(wx.EVT_TIMER, self.OnTimer)

	def OnTimer(self, event):
		status = 0
		try:
			status = self.device.statusCheck()
		except:
			print ("Unexpected error OnRecordClicked")

		if status == CAMD_SNAPSHOT_OK:
			try:
				print ("OnTimer %s" %self.title)
				self.timer.Stop()
				self.device.statusUpdate(CAMD_RECV_PREVIEW_STOP)

				image_file = '/tmp/test.jpg'
				bitmap = wx.Bitmap('/tmp/test.jpg')
				#img = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				# image's upper left corner anchors at panel coordinates (0, 0)
				bitmap = self.scale_bitmap(bitmap, 640, 400)
				self.bitmap1 = wx.StaticBitmap(self.panel, -1, bitmap, (320, 200))

				#self.ShowResultBtn()
				#self.btnRecord.Hide()
				self.panel.Refresh()

				#self.PhotoView()
			except:
				print ("Unexpected error OnTimer")

	#def PhotoView(self):
	#	print "photo view"



	def GoNextTest(self):
		nextTC.Test(parent=self.parent, title="")
		print "GoNextTest"
		self.Close()
		

if __name__ == '__main__':
	app = wx.App()
	Test(None, title='')
	app.MainLoop()