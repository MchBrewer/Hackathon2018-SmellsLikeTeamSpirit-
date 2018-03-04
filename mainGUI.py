import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages')
import wx

class window(wx.Frame):
    def __init__(self, x, y, *args, **kwargs):
        self.topX = x
        self.topY = y/2
        
        self.btmX = x/2
        self.vtmy = y/2
        
        
        super(window, self).__init__(*args, **kwargs)
        self.Center()
        self.Show()
        
        self.panel      = wx.Panel  (self,  style=(wx.SUNKEN_BORDER),       pos=(0,0),          size=(800,250))
        self.Input      = wx.Panel  (self,  style=(wx.SUNKEN_BORDER),       pos=(0,250),        size=(400,250))
        self.Output     = wx.Panel  (self,  style=(wx.SUNKEN_BORDER),       pos=(400,250),      size=(400,250))
        
        self.panel.SetBackgroundColour("grey")
        
        self.sumBTN     = wx.Button (self.panel,    label="sigma",          pos=(10,10),        size=(75,25))
        self.piBTN      = wx.Button (self.panel,    label="pi",             pos=(85, 10),       size=(75,25))
        
        self.sumBTN.Bind(wx.EVT_BUTTON, self.sumClick)
        self.piBTN.Bind(wx.EVT_BUTTON, self.piClick)
        
        
    def sumClick(self, evt):
        for child in self.Input.GetChildren():
            child.Destroy()
            
        self.sumInTop   = wx.TextCtrl(self.Input, -1,   "1",                pos=(10,55),        size=(25,25))
        self.funcInput  = wx.TextCtrl(self.Input, -1,   "2",                pos=(25,85),        size=(150,25))
        self.sumInBtm   = wx.TextCtrl(self.Input, -1,   "3",                pos=(10,115),       size=(25,25))
    
    def piClick(self, evt):
        for child in self.Input.GetChildren():
            child.Destroy()
        
        self.sumInTop   = wx.TextCtrl(self.Input, -1,   "4",                pos=(10,55),        size=(25,25))
        self.funcInput  = wx.TextCtrl(self.Input, -1,   "5",                pos=(25,85),        size=(150,25))
        self.sumInOut   = wx.TextCtrl(self.Input, -1,   "6",                pos=(10,115),       size=(25,25))
        
        
def main():
    x = 800
    y = 500
    
    app = wx.App()
    window(None, x, y, title = "Project Notation",                                                    size=(x,y))
    app.MainLoop()
    
main()