# coding: utf-8
import socket
import tratamento

# Endereco IP do Servidor
HOST = '192.168.0.115'

# Porta que o Servidor esta
PORT = 7070                     

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)


while True:
    msg, cliente = udp.recvfrom(1024)
    print msg

    # Verifica na tabela se existe algum ip válido para a operação passada.
    resultado = tratamento.tabela(msg)

    if(resultado == False):
        udp.sendto('0', cliente)

    else:
        udp.sendto(resultado, cliente)


udp.close()
