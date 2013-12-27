import wx

class Example(wx.Frame):
	def __init__(self, *args, **kw):
		super(Example, self).__init__(*args, **kw) 
		
		self.InitUI()
		
		
	def InitUI(self):

		panel = wx.Panel(self)
		panel.SetAutoLayout(True)

		button1 = wx.Button(panel, id=100,label='Ok', pos=(15, 15))
		
		lc = wx.LayoutConstraints()
		lc.centreX.SameAs(panel, wx.CentreX)
		lc.centreY.SameAs(panel, wx.CentreY)
		lc.height.AsIs()
		lc.width.AsIs()

		#print wx.CentreX
		#print wx.CentreY

		#print lc.centreX
		#print lc.centreY

		#print panel.GetSize()

		print wx.DisplaySize()

		#print w
		#print h


		button1.SetConstraints(lc)
		

		self.SetTitle('Button Test')
		self.Centre()
		self.Show(True)  


def main():
	ex = wx.App()
	Example(None)
	ex.MainLoop()


if __name__ == '__main__':
	main()
