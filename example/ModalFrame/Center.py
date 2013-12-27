#!/usr/bin/env python
import wx

class frame(wx.Frame):
	
	def __init__(self):
		wx.Frame.__init__(self, parent = None, id = -1)

		panel = wx.Panel(self)

		text = wx.StaticText(panel, -1, "Some text")

		btn1 = wx.Button(panel, label="Yes", size=(200,30))
		btn2 = wx.Button(panel, label="No", size=(200,30))
		text.CenterOnParent()
		sizer = wx.GridSizer(2, 2, 5, 5)
		sizer.Add(text, 0, wx.ALL |wx.CENTRE | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTRE_VERTICAL)
		sizer.Add(btn1, 0, wx.ALL |wx.CENTRE | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTRE_VERTICAL)
		sizer.Add(btn2, 0, wx.ALL |wx.CENTRE | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTRE_VERTICAL)
		panel.SetSizer(sizer)
		self.Fit()
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.Show()
		
		
def main():
	
	ex = wx.App()
	frame()
	ex.MainLoop()    


if __name__ == '__main__':
	main()