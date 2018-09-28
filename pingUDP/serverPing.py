import socket
import os

udp_ip = "127.0.0.1"
udp_port = 5005

sockServer = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sockClient = socket.socket(socket.AF_INET, # Internet
			socket.SOCK_DGRAM) # UDP

# Faz o bind local. Associa um socket com um IP e uma Porta.
sockServer.bind((udp_ip, udp_port))
# sockClient.bind((udp_ip, 5006))

while True:
	mensage, addr = sockServer.recvfrom(1024) # Tamanho do buffer eh 1024 bytes
	sockClient.sendto(mensage, (udp_ip, 5006))
     
	if mensage == "EXIT":
		print "Cliente Desconectou"
		break
	else:
		print "Mensagem recebida:", mensage
