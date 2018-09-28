import socket
import os

udp_ip_receive = "177.105.60.226"
udp_port_receive = 5005

sockServer = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sockClient = socket.socket(socket.AF_INET, # Internet
			socket.SOCK_DGRAM) # UDP

# Faz o bind local. Associa um socket com um IP e uma Porta.
sockServer.bind((udp_ip_receive, udp_port_receive))

while True:
	mensage, addr = sockServer.recvfrom(1024) # Tamanho do buffer eh 1024 bytes
	print(addr)
	sockClient.sendto(mensage, (addr[0], udp_port_receive))
     
	if mensage == "EXIT":
		print "Cliente Desconectou"
		break
	else:
		print "Mensagem recebida:", mensage
