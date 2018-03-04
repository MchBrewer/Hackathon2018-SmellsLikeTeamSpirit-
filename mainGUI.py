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
        
        
    def sumClick(self, evt):
        self.sumInTop   = wx.TextCtrl(self.Input, -1,   "1",         pos=(10,55),    size=(25,25))
        self.fuctInput  = wx.TextCtrl(self.Input, -1,   "2",         pos=(20,85),      size=(150,25))
        self.sumInBtm   = wx.TextCtrl(self.Input, -1,   "3",         pos=(10,115),    size=(25,25))
        
        
def main():
    app = wx.App()
    window(None, title = "Project Notation", size = (800,500))
    app.MainLoop()
    
main()