import wx
import wxpil
import code128 as barcode

class Example(wx.Frame):
	def __init__(self, *args, **kw):
		super(Example, self).__init__(*args, **kw) 
		self.InitUI()
		
		
	def InitUI(self):

		panel = wx.Panel(self)

		pil = barcode.code128_image("NULL", height=72, thickness=3, quiet_zone=True)
		
		img = wxpil.PilImageToWxBitmap(pil)

		bitmap = wx.StaticBitmap(self, -1, img)
		bitmap.SetPosition((10, 10))

		self.SetTitle('Button Test')
		self.Centre()
		self.Show(True)  


def main():
	ex = wx.App()
	Example(None)
	ex.MainLoop()    


if __name__ == '__main__':
	main()  