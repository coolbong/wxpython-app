#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import ModalFrame

class Example(wx.Frame):
	def __init__(self, *args, **kw):
		super(Example, self).__init__(*args, **kw) 
		
		self.InitUI()
		
		
	def InitUI(self):

		panel = wx.Panel(self)

		button1 = wx.Button(panel, id=100,label='Ok', pos=(15, 15))
		button2 = wx.Button(panel, id=200,label='Ok', pos=(15, 50))

		self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

		self.SetTitle('Button Test')
		self.Centre()
		self.Show(True)  

	def OnButtonClicked(self, e):
		#print 'event reached frame class'
		btn = e.GetEventObject()
		if btn.GetId() == 100:

			modalFrame = ModalFrame.ModalFrame(self, u"PARAM 영역에 올바른 데이터가 들어있지 않습니다. \nBAR CODE 화면으로 이동하여 올바른 데이터를 입력하시겠습니까?" ,self.OnDialogClose)
			modalFrame.ShowModal()
		else:
			modalFrame = ModalFrame.ModalFrame(self, u"UMS 영역을 활성화 하시겠습니까?" ,self.OnUMSEnable)
			modalFrame.ShowModal()

		#dial = wx.MessageDialog(None, "PARAM 영역에 올바른 데이터가 들어있지 않습니다. \nBAR CODE 화면으로 이동하여 올바른 데이터를 입력하시겠습니까?", "Question", wx.OK|wx.CANCEL|wx.NO_DEFAULT|wx.ICON_QUESTION)
		#dial.ShowModal()
		print btn.GetId()

	def OnDialogClose(self, e):
		print e.GetEventObject().GetLabel()


	def OnUMSEnable(self, e):
		print e.GetId()
		print wx.ID_OK
		if e.GetId() == wx.ID_OK:
			modalFrame = ModalFrame.ModalFrame(self, u'릴리즈 업데이트를 진행하시겠습니까??', self.OnReleaseUpdate)
			modalFrame.ShowModal()
	
	def OnReleaseUpdate(self, e):
		print e.GetId()


def main():
	ex = wx.App()
	Example(None)
	ex.MainLoop()    


if __name__ == '__main__':
	main()  