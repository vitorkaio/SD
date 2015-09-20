# coding: utf-8
import wx
import socket
import urllib
from classe_number import *
from classe_cache_number import *

class JanelaFat(wx.Frame):
    
    ''' Classe que constrói a janela referente a Fatorial.'''
    
    def __init__(self, parent, id, title, cache):
        
        # Cria janela.
        wx.Frame.__init__(self, parent, id, title, size=(280, 280))
        self.Centre()
        self.Show(True)
        
        self.cacheFat = cache
        
        # Cria um texto static
        self.text = wx.StaticText(self, label='Enter with a Number:', pos=(10, 10))

        # Cria uma caixa de texto.
        self.edit = wx.TextCtrl(self, size=(250, -1), pos=(10, 30))
        
        # Cria um button.
        self.button = wx.Button(self, label='ok', pos=(90, 120))
        
        # Conecta um method ao button.
        self.button.Bind(wx.EVT_BUTTON, self.on_button)
        
    def on_button(self, event):

        # Pegas os valores das caixas de texto
        a = self.edit.GetValue()

        try:
            a = int(a)

        except:
             wx.MessageBox('NumberFormatException', 'Erro')
             return

        finally:
            a = str(a)
        
        # Verifica o cache.
        verifica = self.cacheFat.getValor(a, '1')
        if verifica != False:
                resultado = verifica
                imprimeResultado = 'Cache -> ' + str(resultado)
        
        # Se o valor não estiver no cache, conecta no servidor para realiza a operação.
        else:
            HOST = '192.168.0.115'  # Endereco IP do Servidor de nomes.
            PORT = 7070            # Porta que o Servidor esta escutando.
            udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            dest = (HOST, PORT)

            msg = '2' # 1 -> Representa Fatorial.
            udp.sendto (msg, dest)
            resultado, dst = udp.recvfrom(1024)
            
            # Se o valor for 0, quer dizer que não existe servidor on com a operação Fatorial.
            if resultado == '0':
                imprimeResultado = 'Servidor não encontrado'

            else:
                ip = resultado.replace('\n', '')

                f = urllib.urlopen("http://" + ip + ":3000/" + "fat?a=" + a +"&b=" + '1')
                contents = f.read()
                f.close()

                imprimeResultado = str(contents)
                
                # Adiciona o valor a e b e seu resultado no array de cache.
                fat = Number(a, '1', contents)
                verifica = self.cacheFat.insere(fat)
        
        
        # Mostra o resultado
        try:
            wx.MessageBox(imprimeResultado)
            
            # Zera os campos de texto.
            self.edit.SetValue('')
            udp.close()
            
            # Se algo inesperado ocorrer
        except:
            t = ''
