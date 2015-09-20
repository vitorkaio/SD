# coding: utf-8

from timeout import *
from random import shuffle
import socket

def escolhe_ip(nome_arquivo):
	'''
	Essa função tem como objetivo ler ips de um arquivo, carregar para
	uma lista, embaralhar e retorna um.
	'''

	arq = open(nome_arquivo, 'r')
	lista = list()

	for line in arq.readlines():
		lista.append(line)

	arq.close()
	shuffle(lista)
	i = 0

	while i < len(lista):
		ip = lista[i]

		try:
			with Timeout(2):
				teste = testa_ip(ip)

				if teste == True:
					return ip
				
				else:
					print 'Servidor %s está off' %(ip)
					i += 1

		except Timeout.Timeout:
			print 'Servidor %s está off' %(ip)
			i += 1

	return False

################### Testa o ip ###################
# Se a funcão não responder dentro de 2 segundos, retorna false.
def testa_ip(ip):
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		mysock.connect((ip, 3000))

	except socket.error:
		return False

	return True
