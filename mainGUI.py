import wx

class window(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(window, self).__init__(*args, **kwargs)
        self.Center()
        self.Show()
        
        self.panel = wx.Panel(self, size=(800,500))
        self.panel.SetBackgroundColour("Cream")
        
def main():
    app = wx.App()
    window(None, title = "Project Notation", size = (800,500))
    app.MainLoop()
    
main()