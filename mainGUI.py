import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages')
import wx
from formula import Formula

class window(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(window, self).__init__(*args, **kwargs)
        self.Center()
        self.Show()
        
        self.panel      = wx.Panel  (self,  style=(wx.SUNKEN_BORDER),           pos=(0,0),          size=(800,250))
        self.Input      = wx.Panel  (self,  style=(wx.SUNKEN_BORDER),           pos=(0,250),        size=(400,250))
        self.Output     = wx.Panel  (self,  style=(wx.SUNKEN_BORDER),           pos=(400,250),      size=(400,250))
        
        self.panel.SetBackgroundColour("grey")
        
        self.sumBTN     = wx.Button (self.panel,    label=u'\u03A3',            pos=(10,10),        size=(75,25))
        self.piBTN      = wx.Button (self.panel,    label=u'\u03A0',            pos=(85, 10),       size=(75,25))
        self.commitBTN  = wx.Button (self.panel,    label="Convert",            pos=(362,225),      size=(75,25))
        self.formulaType = ""
        
        self.sumBTN.Bind(wx.EVT_BUTTON, self.sumClick)
        self.piBTN.Bind(wx.EVT_BUTTON, self.piClick)
        self.commitBTN.Bind(wx.EVT_BUTTON, self.convertClick)
        
        self.varTop     = wx.TextCtrl   (self.Input, -1,   "n",                 pos=(10,55),        size=(25,25))
        self.equSign1   = wx.StaticText (self.Input, label="=",                 pos=(35,55),        size=(25,25))
        self.sumInTop   = wx.TextCtrl   (self.Input, -1,   "10",                 pos=(60,55),        size=(25,25))
        self.funcInput  = wx.TextCtrl   (self.Input, -1,   "k",                 pos=(85,85),        size=(150,25))
        self.varBtm     = wx.TextCtrl   (self.Input, -1,   "k",                 pos=(10,115),       size=(25,25))
        self.equSign2   = wx.StaticText (self.Input, label="=",                 pos=(35,115),       size=(25,25))
        self.sumInBtm   = wx.TextCtrl   (self.Input, -1,   "0",                 pos=(60,115),       size=(25,25))
        
        self.codeOutput = wx.TextCtrl (self.Output, -1, "Code Output Here",    pos=(5, 5),      size=(300,200), style=wx.TE_MULTILINE)
        self.codeOutput.SetModified(False)
        self.codeOutput.SetBackgroundColour('white')
        
        
    def sumClick(self, evt):
        for child in self.Input.GetChildren():
            child.Destroy()
        self.formulaType = "sigma"
        
        self.symbol     = wx.StaticText (self.Input, label=u'\u03A3',            pos=(50,90),       size=(50,50))
        self.symbol.SetFont(wx.Font(24, wx.ROMAN, wx.BOLD, wx.NORMAL))
        
        self.varTop     = wx.TextCtrl   (self.Input, -1,   "n",                 pos=(10,55),        size=(25,25))
        self.equSign1   = wx.StaticText (self.Input, label="=",                 pos=(35,55),        size=(25,25))
        self.sumInTop   = wx.TextCtrl   (self.Input, -1,   "10",                 pos=(60,55),        size=(25,25))
        self.funcInput  = wx.TextCtrl   (self.Input, -1,   "k",                 pos=(85,85),        size=(150,25))
        self.varBtm     = wx.TextCtrl   (self.Input, -1,   "k",                 pos=(10,115),       size=(25,25))
        self.equSign2   = wx.StaticText (self.Input, label="=",                 pos=(35,115),       size=(25,25))
        self.sumInBtm   = wx.TextCtrl   (self.Input, -1,   "0",                 pos=(60,115),       size=(25,25))
        
    def piClick(self, evt):
        for child in self.Input.GetChildren():
            child.Destroy()
        self.formulaType = "pi"
        
        self.symbol     = wx.StaticText (self.Input, label=u'\u03A0',            pos=(50,90),             size=(50,50))
        self.symbol.SetFont(wx.Font(24, wx.ROMAN, wx.BOLD, wx.NORMAL))
        
        self.varTop     = wx.TextCtrl   (self.Input, -1,   "n",                 pos=(10,55),        size=(25,25))
        self.equSign1   = wx.StaticText (self.Input, label="=",                 pos=(35,55),        size=(25,25))
        self.sumInTop   = wx.TextCtrl   (self.Input, -1,   "10",                 pos=(60,55),        size=(25,25))
        self.funcInput  = wx.TextCtrl   (self.Input, -1,   "k",                 pos=(85,85),        size=(150,25))
        self.varBtm     = wx.TextCtrl   (self.Input, -1,   "k",                 pos=(10,115),       size=(25,25))
        self.equSign2   = wx.StaticText (self.Input, label="=",                 pos=(35,115),       size=(25,25))
        self.sumInBtm   = wx.TextCtrl   (self.Input, -1,   "1",                 pos=(60,115),       size=(25,25))
    
    def convertClick(self, evt):
        expression = "lambda " + self.varBtm.GetValue() + ": " + self.funcInput.GetValue()
        parameters = {}
        parameters["_n_"] = self.sumInTop.GetValue()
        parameters["_i_"] = self.sumInBtm.GetValue()
        parameters["result"] = 0.0
        variableNames = {}
        variableNames["_n_"] = self.varTop.GetValue()
        variableNames["_k_"] = self.varBtm.GetValue()
        variableNames["_i_"] = "i"
        formula = Formula(self.formulaType, parameters, variableNames, expression)
        code = formula.getCode()
        self.codeOutput.SetValue(code)
    
def main():
    x = 800
    y = 500
    
    app = wx.App()
    window(None, title = "Project Notation",                                                    size=(x,y))
    app.MainLoop()
    
main()