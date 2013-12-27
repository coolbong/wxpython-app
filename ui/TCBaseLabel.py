#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx


class MpLabel(wx.StaticText):
	#Size enum
	SMALL = 0
	MEDIUM = 1
	LARGE = 2

	def __init__(self, *args, **kw):
		super(MpLabel, self).__init__(*args, **kw)
		self.SetForegroundColour(wx.WHITE)

		self.smallFont 	= wx.Font(8, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
		self.mediumFont = wx.Font(13, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
		self.largeFont 	= wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)

		self.SetFont(self.largeFont)

	def SetFontSize(self, size):
		if size == self.SMALL:
			self.SetFont(self.smallFont)
		elif size == self.MEDIUM:
			self.SetFont(self.mediumFont)
		elif size == self.LARGE:
			self.SetFont(self.largeFont)

	def SetFontColor(self, flag):
		if flag == False:
			self.SetForegroundColour(wx.RED)
		else:
			self.SetForegroundColour(wx.BLUE)
