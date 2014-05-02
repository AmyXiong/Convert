#! /usr/bin/env python

import wx

class ConvertFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Convert feet and inches to centimeters")

		self.panel = wx.Panel(self)
		
		self.prompt1 = wx.StaticText(self.panel, label="Enter the number for feet:", pos=(40, 10))
		self.feetBox = wx.TextCtrl(self.panel, pos=(280, 10))
		
		self.prompt2 = wx.StaticText(self.panel, label="Enter the number for inches:", pos=(40, 50))
		self.inchBox = wx.TextCtrl(self.panel, pos=(280, 50))
		
		self.response = wx.StaticText(self.panel, pos=(40, 150))
		
		self.btnConvert = wx.Button(self.panel, label="Convert", pos=(150, 100))
		self.btnConvert.Bind(wx.EVT_BUTTON, self.OnConvert)

	def OnConvert(self, e):
		feet = self.feetBox.GetValue()
		inch = self.inchBox.GetValue()
		
		
		
		try:
			feet = float(feet)
			inch = float(inch)
			centimeters = str(feet*30.48 + inch*2.54)
			self.response.SetLabel("The number in centimeters is" + centimeters)
			
		except:
			wx.MessageBox("Sorry, you didn't enter a number.", "Info", wx.OK)
			
		
#------------- Main Program Below -----------------------------

app = wx.App(False)

frame = ConvertFrame(None)

frame.Show()

app.MainLoop()