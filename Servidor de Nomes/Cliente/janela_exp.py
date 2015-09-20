# coding: utf-8
import wx
import socket
import urllib
from classe_number import *
from classe_cache_number import *

class JanelaExp(wx.Frame):
    
    ''' Classe que constrói a janela referente a Exponenciação.'''
    
    def __init__(self, parent, id, title, cache):
        
        # Cria janela
        wx.Frame.__init__(self, parent, id, title, size=(280, 280))
        self.Centre()
        self.Show(True)
        
        self.cacheSoma = cache
        
        # Cria um texto est�tico
        self.text = wx.StaticText(self, label='Enter with a NumberA:', pos=(10, 10))
        self.text = wx.StaticText(self, label='Enter with a NumberB:', pos=(10, 60))
        
        # Cria uma caixa de edi��o de texto
        self.edit = wx.TextCtrl(self, size=(250, -1), pos=(10, 30))
        self.edit2 = wx.TextCtrl(self, size=(250, -1), pos=(10, 80))
        
        # Cria um bot�o
        self.button = wx.Button(self, label='ok', pos=(90, 120))
        
        # Conecta um m�todo ao bot�o
        self.button.Bind(wx.EVT_BUTTON, self.on_button)
        
    def on_button(self, event):

        # Pegas os valores das caixas de texto
        a = self.edit.GetValue()
        b = self.edit2.GetValue()

        try:
            a = int(a)
            b = int(b)

        except:
             wx.MessageBox('NumberFormatException', 'Erro')
             return

        finally:
            a = str(a)
            b = str(b)
        
        # Verifica o cache
        verifica = self.cacheSoma.getValor(a, b)
        if verifica != False:
                resultado = verifica
                imprimeResultado = 'Cache -> ' + str(resultado)
        
        # Se o valor não estiver no cache, conecta no servidor para realiza a operação.
        else:
            HOST = '192.168.0.115'  # Endereco IP do Servidor de nomes.
            PORT = 7070            # Porta que o Servidor esta escutando.
            udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            dest = (HOST, PORT)

            msg = '3' # 1 -> Representa exponenciação.
            udp.sendto (msg, dest)
            resultado, dst = udp.recvfrom(1024)
            
            # Se o valor for 0, quer dizer que não existe servidor on com a operação soma.
            if resultado == '0':
                imprimeResultado = 'Servidor não encontrado'

            else:
                ip = resultado.replace('\n', '')

                f = urllib.urlopen("http://" + ip + ":3000/" + "exp?a=" + a +"&b=" + b)
                contents = f.read()
                f.close()

                imprimeResultado = str(contents)
                
                # Adiciona o valor a e b e seu resultado no array de cache.
                exp = Number(a, b, contents)
                verifica = self.cacheSoma.insere(exp)
        
        
        # Mostra o resultado
        try:
            wx.MessageBox(imprimeResultado)
            
            # Zera os campos de texto.
            self.edit.SetValue('')
            self.edit2.SetValue('')
            udp.close()
            
            # Se algo inesperado ocorrer
        except:
            t = ''
