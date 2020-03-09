# Projet de POO : Shazam_Instrument
# Hugo LE ROY, JUNAY Léa
# 02/03/2020

#code pour faire une fenêtre et un bouton
#pas utile pour l'instant
import wx

class MaFenetre(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Ma fenêtre avec bouton')
        
        nb_boutons = 16
        self.ma_grille = wx.GridSizer(rows=4, cols=4, vgap=10, hgap=10)
        font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_BOLD)
        for i in range(nb_boutons):
            bouton = wx.Button(self,  label='X')
            bouton.SetFont(font)
            bouton.Bind(wx.EVT_BUTTON, self.OnBouton)            
            self.ma_grille.Add(bouton, i,wx.EXPAND)          
           
        self.SetSizerAndFit(self.ma_grille)        
        self.Show()

    def OnBouton(self, event):
        bouton = event.GetEventObject()
        s = bouton.GetLabel()
        if s == "X":
            bouton.SetLabel("O")
        elif s == "O":
            bouton.SetLabel("X")
       
if __name__ == '__main__':
    app = wx.App()
    frame = MaFenetre()
    app.MainLoop()
