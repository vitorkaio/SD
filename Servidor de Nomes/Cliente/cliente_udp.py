# coding: utf-8

import socket
import urllib
from classe_number import *
from classe_cache_number import *
from janela_menu import *

# Aproveita a classe CacheSoma() para utilizar no exponencial
cacheSoma = CacheNumber()
cacheExp = CacheNumber()
cacheFat = CacheNumber()
''' 
    Passando o objeto cacheSoma como parâmetro, pois se não passar, ele será reiniciado a cada
    construção da janela gráfica.
'''
# Cria a janela de menu.
menu = Menu(None, -1, 'Menu', cacheSoma, cacheExp, cacheFat)

