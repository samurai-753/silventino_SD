import socket
import time
# import socket.timeout as TimeoutException
# set timeout 5 second

udp_ip_send = "177.105.60.80"
udp_port_send = 5002

clientSocket= socket.socket(socket.AF_INET, # Internet 
				      socket.SOCK_DGRAM)  # UDP

clientSocket.settimeout(0.250)

numeroPacotesPerdidos = 0
somaRTT = 0

for i in range(0,20):
  sequence_number = i
  start = time.time()
  clientSocket.sendto("Ping\n", (udp_ip_send, udp_port_send))

  try:
    message, address = clientSocket.recvfrom(1024)
  except socket.timeout:
    numeroPacotesPerdidos += 1
    print("Pacote "+ str(i) +": Timeout!!! Try again...\n")
    time.sleep(1)
    continue
  end = time.time()
  if message != '':
    # print(message)
    rtt = end - start
    somaRTT += rtt
    print("Pacote "+ str(i) +": RTT = " + str(rtt) + "\n")
  time.sleep(1)

print(str(numeroPacotesPerdidos) + " pacotes perdidos")
mediaRTT = (somaRTT/(20 - numeroPacotesPerdidos))
print("RTT medio: " + str(mediaRTT))