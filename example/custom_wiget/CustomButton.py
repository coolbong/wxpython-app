import wx




class MyButton(wx.Button):
	
	def __init__(self, *args, **kw):
		super(MyButton, self).__init__(*args, **kw) 
		self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

	def OnButtonClicked(self, e):
		print 'event reached button class'
		e.Skip()

class Example(wx.Frame):
		   
	def __init__(self, *args, **kw):
		super(Example, self).__init__(*args, **kw) 
		self.InitUI()
		
		
	def InitUI(self):

		panel = wx.Panel(self)

		button1 = MyButton(panel, id=100,label='Ok', pos=(15, 15))
		button2 = MyButton(panel, id=200,label='Ok', pos=(15, 50))

		self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

		self.SetTitle('Button Test')
		self.Centre()
		self.Show(True)  

	def OnButtonClicked(self, e):
		print 'event reached frame class'
		print e.GetEventObject().GetId()
		e.Skip()


def main():
	ex = wx.App()
	Example(None)
	ex.MainLoop()    


if __name__ == '__main__':
	main()  