import socket
import time
# import socket.timeout as TimeoutException
# set timeout 5 second
udp_ip_receive = "177.105.60.245"
udp_port_receive = 5005

udp_ip_send = "177.105.60.226"
udp_port_send = 5005

clientSocket= socket.socket(socket.AF_INET, # Internet 
				      socket.SOCK_DGRAM)  # UDP
sockServer = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP


sockServer.bind((udp_ip_receive, udp_port_receive))
sockServer.settimeout(0.250)

for i in range(0,20):
  sequence_number = i
  start = time.time()
  clientSocket.sendto("Ping " + str(i) + " " + str(start), (udp_ip_send, udp_port_send))

  try:
    message, address = sockServer.recvfrom(1024)
  except socket.timeout:
    print("Timeout!!! Try again...")
    continue
  end = time.time()
  if message != '':
    print(message)
    rtt = end - start
    print("RTT = " + str(rtt) + "\n")