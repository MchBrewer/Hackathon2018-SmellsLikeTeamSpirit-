import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages')
import wx

class window(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(window, self).__init__(*args, **kwargs)
        self.Center()
        self.Show()
        
        self.panel  = wx.Panel  (self,  size=(800,250), pos=(0,0),      style=(wx.SUNKEN_BORDER))
        self.Input  = wx.Panel  (self,  size=(400,250), pos=(0,250),    style=(wx.SUNKEN_BORDER))
        self.Output = wx.Panel  (self,  size=(400,250), pos=(400,250),  style=(wx.SUNKEN_BORDER))
        
        self.panel.SetBackgroundColour("grey")
        
        self.sumBTN     = wx.Button (self.panel,    label="sigma",  pos=(10,10),    size=(75,25))
        self.piBTN      = wx.Button (self.panel,    label="pi",     pos=(85, 10),   size=(75,25))
        
        self.sumBTN.Bind(wx.EVT_BUTTON, self.sumClick)
        self.piBTN.Bind(wx.EVT_BUTTON, self.piClick)
        
        
    def sumClick(self, evt):
        self.limitVariable = wx.TextCtrl(self.Input, -1, "n =",       pos=(0, 55),        size=(30,25))
        self.sumInTop   = wx.TextCtrl(self.Input, -1,   "10",         pos=(35,55),       size=(50,25))
        
        self.funcInput  = wx.TextCtrl(self.Input, -1,   "k^2",         pos=(25,85),       size=(150,25))
        
        self.countingVariable = wx.TextCtrl(self.Input, -1, "k =",     pos=(0, 115),        size=(30,25))
        self.sumInBtm   = wx.TextCtrl(self.Input, -1,   "1",         pos=(35,115),      size=(50,25))
    
    def piClick(self, evt):
        self.limitVariable = wx.TextCtrl(self.Input, -1, "4",       pos=(0, 55),        size=(30,25))
        self.sumInTop   = wx.TextCtrl(self.Input, -1,   "4",        pos=(35,55),        size=(50,25))
        
        self.funcInput   = wx.TextCtrl(self.Input, -1,   "4",        pos=(25,85),        size=(25,25))
        
        self.countingVariable = wx.TextCtrl(self.Input, -1, "4",     pos=(0, 115),        size=(30,25))
        self.sumInOut   = wx.TextCtrl(self.Input, -1,   "4",        pos=(35,115),        size=(50,25))       
        
def main():
    app = wx.App()
    window(None, title = "Project Notation", size = (800,500))
    app.MainLoop()
    
main()