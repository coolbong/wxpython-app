#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

class Test(wx.Frame):

	def __init__(self, parent, title):
		super(Test, self).__init__(parent, title="Key Char TEST")
		self.InitUI()
		self.InitBind()
		self.SetBackgroundColour('black')
		self.Show()

	def InitUI(self):
		print "InitUI"		
		self.panel = wx.Panel(self)
		self.plusKey = 0
		self.lblVolumeUp 	= wx.StaticText(self.panel, -1, 'Volume + ( 0 )', (80, 80))
		self.btn = wx.Button (self.panel, label="ok")

	def InitBind(self):
		print "InitBind"
		self.btn.Bind(wx.EVT_KEY_UP, self.OnKeyUpEvent)
		self.btn.Bind(wx.EVT_CHAR, self.OnKeyCharEvent)
		self.btn.Bind(wx.EVT_CLOSE, self.OnClose)
	
	def OnClose(self, event):
		self.Destroy()

	def OnKeyUpEvent(self, evt):
		keycode = evt.GetKeyCode()

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
		print ("key char code: %s" %keyname)


if __name__ == '__main__':
	app = wx.App()
	Test(None, title='')
	app.MainLoop()