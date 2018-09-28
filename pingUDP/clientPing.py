import socket
import time
# import socket.timeout as TimeoutException
# set timeout 5 second
udp_ip = "127.0.0.1"
udp_port = 5005

clientSocket= socket.socket(socket.AF_INET, # Internet 
				      socket.SOCK_DGRAM)  # UDP

sockServer = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sockServer.bind((udp_ip, 5006))
 
clientSocket.settimeout(1)
for i in range(0,20):
  sequence_number = i
  start = time.time()
  clientSocket.sendto("Ping " + str(i) + " " + str(start), (udp_ip, udp_port))
  receive = False
  # while not receive:
	#   mensage, addr = sockServer.recvfrom(1024) # Tamanho do buffer eh 1024 bytes
  #   print(mensage)
  # Receive the client packet along with the address it is coming from
  try:
    message, address = sockServer.recvfrom(1024)
  except socket.timeout:
    print("Timeout!!! Try again...")
    continue
  end = time.time()
  if message != '':
    print(message)
    rtt = end - start
    print("RTT = " + str(rtt))