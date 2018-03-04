import wx

class window(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(window, self).__init__(*args, **kwargs)
        self.Center()
        self.Show()
        
        self.panel      = wx.Panel  (self,  size=(800,500))
        self.panel.SetBackgroundColour("Cream")
        
        self.sigBTN     = wx.Button (self.panel,    label="sigma",  pos=(10,10),    size=(75,25))
        self.piBTN      = wx.Button (self.panel,    label="pi",     pos=(10, 35),   size=(75,25))
        
       #self.funcInput  = wx.TextEntryDialog    (self.panel,    "Promt",    "title",            "DefaultText")
        self.fuctInput  = wx.TextCtrl(self.panel,   -1,             "f(x)",         pos=(10,55),    size=(150,50))  
        
        
def main():
    app = wx.App()
    window(None, title = "Project Notation", size = (800,500))
    app.MainLoop()
    
main()