# Présentation des résultats ( dB max, Fréquence, nom de l'instrument) 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
ZetCode wxPython tutorial

In this example we create a Go To class
layout with wx.BoxSizer.

author: Jan Bodnar
website: www.zetcode.com
last modified: April 2018
"""

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        font.SetPointSize(9)

# nom de l'instrument   

        st1 = wx.StaticText(panel, label='Instrument',pos=(10,10))
        st1.SetFont(font)

        

# Amplitude du fondamental
        st2 = wx.StaticText(panel, label='Amplitude du fondamental',pos=(10,50))
        st2.SetFont(font)
        
 # Amplitude du fondamental  
        st2 = wx.StaticText(panel, label='Frequence du fondamental',pos=(10,90))
        st2.SetFont(font)
       

    
        btn1 = wx.Button(panel, label='Ok', size=(70, 30),pos=(10,130))
       

       




def main():

    app = wx.App()
    ex = Example(None, title='Go To Class')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()