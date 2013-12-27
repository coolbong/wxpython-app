import wx

class MpDialog(wx.Frame):

	callBack = None

	def __init__(self, parent, msg, callback):
		wx.Frame.__init__(self, parent, title="", style=wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP)
		self.callback = None
		self.msg = msg
		
		self.InitUI()
		self.SetBackgroundColour(wx.BLACK)
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)

		if callback != None:
			self.callback = callback

	def InitUI(self):
		fluid_sizer = wx.BoxSizer(wx.HORIZONTAL)
		fluid_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

		self.fixed_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1,-1), wx.TAB_TRAVERSAL)
		#self.fixed_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
		self.fixed_panel.SetBackgroundColour(wx.BLACK)
		
		fixed_sizer = wx.BoxSizer(wx.VERTICAL)
		fixed_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

		fixed_sizer.SetMinSize(wx.Size(150,-1))
		self.lbl = wx.StaticText(self.fixed_panel, -1, self.msg)
		btnFont = wx.Font(17, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
		self.lbl.SetForegroundColour(wx.WHITE)
		self.lbl.SetFont(btnFont)
		
		gridSizer = wx.GridSizer(1, 2, 5, 5)
		
		self.m_button1 = wx.Button(self.fixed_panel, wx.ID_CANCEL, "Cancle", size=(-1, 50))
		self.m_button2 = wx.Button(self.fixed_panel, wx.ID_OK, "OK", size=(-1, 50))
		self.m_button1.SetFont(btnFont)
		self.m_button2.SetFont(btnFont)

		self.m_button1.Bind(wx.EVT_BUTTON, self.onClose)
		self.m_button2.Bind(wx.EVT_BUTTON, self.onClose)
		
		gridSizer.AddMany([
			(self.m_button1, 0, wx.EXPAND), 	(self.m_button2, 0, wx.EXPAND)
			])

		fixed_sizer.Add(self.lbl, 0, wx.ALL, 5)

		#fixed_sizer.Add(self.m_button1, 0, wx.ALL, 5)
		fixed_sizer.Add(gridSizer, 0, flag=wx.EXPAND)
		fixed_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
		self.fixed_panel.SetSizer(fixed_sizer)
		self.fixed_panel.Layout()
		fixed_sizer.Fit(self.fixed_panel)

		fluid_sizer.Add(self.fixed_panel, 0, wx.EXPAND |wx.ALL, 5)

		fluid_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
		self.SetSizer(fluid_sizer)
		self.Layout()


	def onClose(self, event):
		#self.eventLoop.Exit()
		if self.callback != None:
			self.callback(event)
		self.Close()

	def ShowModal(self):
		#self.MakeModal()
		self.Show()