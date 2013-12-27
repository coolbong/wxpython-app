import wx
import helloworld

class Example(wx.Frame):

	def __init__(self, parent, title):
		super(Example, self).__init__(parent, title=title, size=(320, 130))

		self.InitUI()
		self.Centre()
		self.Show()     

	def InitUI(self):

		panel = wx.Panel(self)
		sizer = wx.GridBagSizer(4, 4)

		text = wx.StaticText(panel, label="Click Ok")
		sizer.Add(text, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)

		#tc = wx.TextCtrl(panel)
		#sizer.Add(tc, pos=(1, 0), span=(1, 5), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

		buttonOk = wx.Button(panel, label="Ok", size=(90, 28))
		buttonClose = wx.Button(panel, label="Close", size=(90, 28))

		#event binding
		buttonOk.Bind(wx.EVT_BUTTON, self.OnOk)
		buttonClose.Bind(wx.EVT_BUTTON, self.OnClose)

		sizer.Add(buttonOk, pos=(3, 3))
		sizer.Add(buttonClose, pos=(3, 4), flag=wx.RIGHT|wx.BOTTOM, border=5)

		sizer.AddGrowableCol(1)
		sizer.AddGrowableRow(2)
		panel.SetSizerAndFit(sizer)

	def OnOk(self, e):
		#get native string
		title = helloworld.getString()
		dial = wx.MessageDialog(None, title, 'Info', wx.OK | wx.ICON_INFORMATION)
		ret = dial.ShowModal()
		self.Destroy()

	def OnClose(self, e):
		self.Destroy()


if __name__ == '__main__':
	app = wx.App()
	Example(None, title='Native interface test')
	app.MainLoop()