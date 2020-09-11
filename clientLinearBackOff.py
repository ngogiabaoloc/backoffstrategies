from socket import *
import re
import random
from time import sleep
serverName = 'localhost'
serverPort = 12000
clientSocket = socket (AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
sum = 0
for number in range (0,20):
    delay = 0
    print("==========================================")
    message = "ping message number "+str(number)
    print('Sending: ',message)
    for attempt in range(0,9):
        clientSocket.sendto(message.encode(), (serverName,serverPort))
        def random_delay():
            if attempt==0:
                delay=0
            elif attempt==1:
                delay=random.randint(0,1)
            else:
                delay=random.randint(0,attempt)
            sleep(delay)
            print("Entering delay: ",delay)
        try:
            print("--------------------------------------")
            print('Attempt: ',attempt)
            sum = sum+1
            modifiedMessage, serverAddress =clientSocket.recvfrom(2048)
            if modifiedMessage.decode()== message.upper():
                print('Received: ', modifiedMessage.decode())
                break
            else:
                random_delay()
                print('Timed out !!!')
        except Exception:
            random_delay()
            sum = sum+1
            print('Timed out!!!')

clientSocket.close()
print('Average number of attempts: ', sum/20)
