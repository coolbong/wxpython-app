import wx

class TimerFrame(wx.Frame):


	def __init__(self, parent, title):
		super(TimerFrame, self).__init__(parent, title=title, size=(320, 240))
		self.InitUI()
		self.SetBackgroundColour('black')
		self.Show()

	def InitUI(self):
		self.Centre()
		self.count = 0

		self.panel = wx.Panel(self)

		btnTimerStart = wx.Button(self.panel, label='Start', pos=(20, 30))
		btnTimerStop = wx.Button(self.panel, label='Stop', pos=(120, 30))

		btnTimerStart.Bind(wx.EVT_BUTTON, self.OnTimerStartBtnClicked)
		btnTimerStop.Bind(wx.EVT_BUTTON, self.OnTimerStopBtnClicked)

		self.Bind(wx.EVT_TIMER, self.OnTimer)

		btnTimerStart2 = wx.Button(self.panel, label='Start Call Later', pos=(20, 100))
		btnTimerStop2 = wx.Button(self.panel, label='Stop', pos=(150, 100))

		btnTimerStart2.Bind(wx.EVT_BUTTON, self.OnTimerStartBtnClicked2)
		btnTimerStop2.Bind(wx.EVT_BUTTON, self.OnTimerStopBtnClicked2)


		self.lblCounter = wx.StaticText(self.panel, label="count: 0", pos=(20, 150))
		

	def OnTimerStartBtnClicked(self, e):
		self.timer = wx.Timer(self)
		self.timer.Start(300)

	def OnTimerStopBtnClicked(self, e):
		self.timer.Stop()
		del self.timer

	def OnTimer(self, event):
		self.count += 1
		self.lblCounter.SetLabel("count: %d" % self.count)
		print "Timer Called"

	def OnTimerStartBtnClicked2(self, e):
		self.timer2 = wx.CallLater(1000, self.OnCallLater, 'a', 'b', 'c', [1, 2, 3])


	def OnTimerStopBtnClicked2(self, e):
		self.timer2.Stop()
		del self.timer2

	def OnCallLater(self, *args, **kw):
		self.timer2.Restart(1000, "Hello world")
		print("CallLater called with args=%s, kwargs=%s\n" % (args, kw))


#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
	app = wx.App(False)
	frame = TimerFrame(None, title="Timer Example")

	app.MainLoop()