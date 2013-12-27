#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

import TC
import TCBase
import TCButton



class Test(TCBase.Base):
	colours = ['White', 'Black', 'Yellow', 'Red', 'Green', 'Blue', 'Purple',
		'Brown', 'Aquamarine', 'Forest Green', 'Light Blue', 'Goldenrod',
		'Cyan', 'Orange', 'Navy', 'Dark Grey', 'Light Grey']

	thicknesses = [1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128]

	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="TOUCH TEST", tc=TC.TCTouch)
		self.InitUI()
		#self.bindEvents()
		#self.initBuffer()
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
		#checkbox1 = wx.CheckBox(self.panel, label="", pos=(8, 8))
		#checkbox2 = wx.CheckBox(self.panel, label="", pos=(8, 768))
		#checkbox3 = wx.CheckBox(self.panel, label="", pos=(1248, 8))
		#checkbox4 = wx.CheckBox(self.panel, label="", pos=(1248, 768))

		btn_width = btn_height = 30
		margin = 10

		self.btnLeftTop = wx.Button(self.panel, label="", pos=(margin, margin), size=(btn_width, btn_height))
		self.btnRightTop = wx.Button(self.panel, label="", pos=(1280 - margin - btn_width, margin), size=(btn_width, btn_height))
		self.btnLeftBot = wx.Button(self.panel, label="", pos=(margin, 800-margin-btn_height), size=(btn_width, btn_height))
		self.btnRightBot = wx.Button(self.panel, label="", pos=(1280 - margin - btn_width, 800-margin-btn_height), size=(btn_width, btn_height))

		self.btnLeftTop.SetFont(self.btnFont)
		self.btnRightTop.SetFont(self.btnFont)
		self.btnLeftBot.SetFont(self.btnFont)
		self.btnRightBot.SetFont(self.btnFont)

		self.btnLeftTop.Bind(wx.EVT_LEFT_UP, self.OnTouchBtnUp)
		self.btnRightTop.Bind(wx.EVT_LEFT_UP, self.OnTouchBtnUp)
		self.btnLeftBot.Bind(wx.EVT_LEFT_UP, self.OnTouchBtnUp)
		self.btnRightBot.Bind(wx.EVT_LEFT_UP, self.OnTouchBtnUp)


		self.panel.Bind(wx.EVT_PAINT, self.onPaint)
		self.panel.Bind(wx.EVT_LEFT_DOWN, self.onLeftDown)
		self.panel.Bind(wx.EVT_LEFT_UP, self.onLeftUp)
		self.panel.Bind(wx.EVT_MOTION, self.onMotion)
		
		self.lblTitle.SetPosition((8, 70))
		self.currentThickness = self.thicknesses[8]
		self.currentColour = self.colours[0]
		self.pen = wx.Pen(wx.NamedColour(self.currentColour), self.currentThickness, wx.SOLID)
		self.guidepen = wx.Pen(wx.NamedColour(self.colours[2]), self.currentThickness, wx.SOLID)
		self.lines = []

		


		#self.previousPosition = (0, 0)

	def GoNextTest(self):
		TCButton.Test(parent=self.parent, title="")
		print "GoNextTest"
		self.Close()

	def OnTouchBtnUp(self, evt):
		btn = evt.GetEventObject()

		if btn.GetLabel() == "":
			btn.SetLabel("✓")
		else:
			btn.SetLabel("")

	
	def onLeftDown(self, event):
		#self.previousPosition = (0, 0)
		self.previousPosition = event.GetPositionTuple()
		self.currentLine = []

		#TBD drawPoint
		dc = wx.PaintDC(self.panel)
		dc.SetPen(self.pen)
		x, y = self.previousPosition
		points = [(x,y), (x+1, y+1)]
		#dc.DrawPointList(points, self.pen)
		dc.DrawPoint(x, y)
		#dc.DrawPointPoint(self.previousPosition)
		
		print "onLeftDown"

	def onLeftUp(self, event):
		
		#dc = wx.PaintDC(self.panel)
		#dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
		#dc.Clear()
		self.panel.Refresh()
		print "onLeftUp"

	def onRightUp(self, event):
		print "onRightUp"

	def onMotion(self, event):
		if event.Dragging() and event.LeftIsDown():
			print "OnMotion"
			dc = wx.PaintDC(self.panel)
			currentPosition = event.GetPositionTuple()
			lineSegment = self.previousPosition + currentPosition
			#self.drawLines(dc, (self.currentColour, self.currentThickness, [lineSegment]))
			lineSegments = [lineSegment]		

			#pen = wx.Pen(wx.NamedColour(self.currentColour), self.currentThickness, wx.SOLID)
			dc.SetPen(self.pen)
			for lineSegment in lineSegments:
				dc.DrawLine(*lineSegment)

			self.currentLine.append(lineSegment)
			self.previousPosition = currentPosition

	def onSize(self, event):
		print "onSize"

	def onIdle(self, event):
		print "onIdle"

	def onPaint(self, event):
		#dc = wx.BufferedPaintDC(self.panel, self.buffer)
		dc = wx.PaintDC(self.panel)
		#dc.Clear()
		dc.SetPen(self.guidepen)
		dc.DrawLine(0, 0, 0, 800)
		dc.DrawLine(0, 0, 1280, 0)
		dc.DrawLine(0, 800, 1280, 800)
		dc.DrawLine(1280, 0, 1280, 800)

		
		dc.DrawLine(1280, 0, 0, 800)
		dc.DrawLine(0, 0, 1280, 800)
		


		print "onPaint"

	def cleanup(self, event):
		print "cleanup"

	
	def drawLines(dc, *lines):
		print dc
		dc.BeginDrawing()
		for colour, thickness, lineSegments in lines:
			pen = wx.Pen(wx.NamedColour(colour), thickness, wx.SOLID)
			dc.SetPen(pen)
			for lineSegment in lineSegments:
				dc.DrawLine(*lineSegment)
		dc.EndDrawing()

if __name__ == '__main__':
	app = wx.App()
	Test(None, title='')
	app.MainLoop()