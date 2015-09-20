# coding: utf-8

import wx
from janela_soma import *
from janela_fat import *
from janela_exp import *

class Menu(wx.Frame):
    
    def __init__(self, parent, id, title, cache_soma, cache_exp, cache_fat):
        
        # Cria janela.
        wx.Frame.__init__(self, parent, id, title, size=(280, 150))
        self.Centre()
        self.Show(True)

        # Define os objetos que serão processados.
        self.cacheSoma = cache_soma
        self.cacheExp = cache_exp
        self.cacheFat = cacheFat
        
        # Cria os botões.
        self.buttonSoma = wx.Button(self, label='Soma', pos=(30, 20))
        self.buttonFat = wx.Button(self, label='Fat', pos=(150, 20))
        self.buttonExp = wx.Button(self, label='Exp', pos=(90, 60))
        
        # Conecta um metodo aos botões.
        self.buttonSoma.Bind(wx.EVT_BUTTON, self.on_buttonSoma)
        self.buttonFat.Bind(wx.EVT_BUTTON, self.on_buttonFat)
        self.buttonExp.Bind(wx.EVT_BUTTON, self.on_buttonExp)
    
    # Trata o evento do botão soma.
    def on_buttonSoma(self, event):
        
        app = wx.App()
        ''' 
        Passando o objeto cacheSoma como parâmetro, pois se não passar, ele será reiniciado a cada
        construção da janela gráfica.
        '''
        JanelaSoma(None, -1, 'Soma', self.cacheSoma)
        app.MainLoop()
    
        # Trata o evento do botão fat
    def on_buttonFat(self, event):
        app = wx.App()
        '''
        Passando o objeto cacheFat como parâmetro, pois se não passar, ele será reiniciado a cada
        construção da janela gráfica.
        '''
        JanelaFat(None, -1, 'Fatorial', self.cacheFat)
        app.MainLoop()
        
        # Trata o evento do botão exp.
    def on_buttonExp(self, event):
        app = wx.App()
        '''
        Passando o objeto cacheExp como parâmetro, pois se não passar, ele será reiniciado a cada
        construção da janela gráfica.
        '''
        JanelaExp(None, -1, 'Pow', self.cacheExp)
        app.MainLoop()

cacheSoma = CacheNumber()
cacheExp = CacheNumber()
cacheFat = CacheNumber()
app = wx.App()
Menu(None, -1, 'Menu', cacheSoma, cacheExp, cacheFat)
app.MainLoop()
