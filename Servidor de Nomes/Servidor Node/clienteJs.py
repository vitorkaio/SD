# coding: utf-8

import urllib

url = "http://localhost:3000/"
msg = 'a'
print "s = Para sair"

while msg != 's':
    
    msg = raw_input('\n1 - Soma\n2 - Fatorial\n3 - Exponenciação\nOp: ')
    
    if(msg != '1' and msg != '2' and msg != '3' and msg != 's'):
        print 'Valor inválido'
        
    if msg == '1':
        
        a = raw_input('A: ')
        b = raw_input('B: ')
        f = urllib.urlopen(url + "soma?a=" + a +"&b=" + b)
        contents = f.read()
        f.close()
        print contents
        
    if msg == '2':
        
        a = raw_input('A: ')
        f = urllib.urlopen(url + "fat?a=" + a)
        contents = f.read()
        f.close()
        print contents
        
    if msg == '3':
        
        a = raw_input('A: ')
        b = raw_input('B: ')
        f = urllib.urlopen(url + "exp?a=" + a +"&b=" + b)
        contents = f.read()
        f.close()
        print contents
        
    if msg == 's':
        break
