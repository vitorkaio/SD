# coding: utf-8

import os, re, socket, shufle_ip

# Verifica qual ip representa a string passada e monitora se está online.

def tabela(msg):

    ''' 
    1 - Soma
    2 - Fatorial
    3 - Exponenciação

    '''

    msgRetorno = ''

    if(msg == '1'):

        # Chama a função que retorna um ip se possível.
        verifica = shufle_ip.escolhe_ip('somaIp.txt')

        if(verifica != False):
            return verifica

        else:
            return False


    elif(msg == '2'):

         # Chama a função que retorna um ip se possível.
        verifica = shufle_ip.escolhe_ip('fatIp.txt')

        if(verifica != False):
            return verifica

        else:
            return False


    elif(msg == '3'):

        # Chama a função que retorna um ip se possível.
        verifica = shufle_ip.escolhe_ip('expIp.txt')

        if(verifica != False):
            return verifica

        else:
            return False