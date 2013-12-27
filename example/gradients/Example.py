#!/usr/bin/python
#http://zetcode.com/wxpython/gdi/

import wx

class Gradients(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, size=(1280, 800))
		self.panel = wx.Panel(self, -1)
		self.panel.SetBackgroundColour(wx.BLACK)

		self.panel.Bind(wx.EVT_PAINT, self.OnPaint)

		self.Centre()
		self.Show(True)

	def OnPaint(self, event):
		dc = wx.PaintDC(self.panel)
#red
#yellow
#green
#blue
#purple
#white		
		dc.GradientFillLinear((0, 0, 1280, 133), '#ff0000', '#000000', wx.EAST)
		dc.GradientFillLinear((0, 133, 1280, 133), '#ffff00', '#000000', wx.EAST)
		dc.GradientFillLinear((0, 266, 1280, 133), '#00ff00', '#000000', wx.EAST)
		dc.GradientFillLinear((0, 399, 1280, 133), '#0000ff', '#000000', wx.EAST)
		dc.GradientFillLinear((0, 532, 1280, 133), '#ff00ff', '#000000', wx.EAST)
		dc.GradientFillLinear((0, 665, 1280, 135), '#ffffff', '#000000', wx.EAST)

app = wx.App()
Gradients(None, -1, 'Gradients')
app.MainLoop()
