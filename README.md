# backoffstrategies
Goal:
The goal of the project is to gain first-hand experience of the utility of backoff strategies for reducing collisions.
Problem Statement: 
The code below simulates a really busy server that accepts sentences as requests and returns capitalized
sentences as responses. This code is also available as a text attachment, and must not be altered.
import random
from time import sleep
from socket import *
BUSY_PERCENT = 50
serverPort = 12000
def get_busy():
random_number = random.randint(0, 100)
if random_number < BUSY_PERCENT:
print("Getting busy ...")
sleep(1)
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive requests')
while True:
get_busy()
message, clientAddress = serverSocket.recvfrom(2048)
print('Received request:\n', message.decode(), '\nfrom client:\n', clientAddress)
modifiedMessage = message.decode().upper()
serverSocket.sendto(modifiedMessage.encode(), clientAddress)
get_busy()
I implemented three different client codes that do the following:
1. It sends 20 messages to the server. After sending each message, the client waits up to 1 second for a response from the server. If a response is received within this time, it prints the response. Otherwise, it retries after a delay. The three clients will have three delay strategies:
1. No delay. The request is resent immediately without any backoff.
2. Exponential backoff.
3. Linear backoff.
In each case, the client gives up and moves on to the next request at the end of 10 attempts. At the end, the client prints out the average number of attempts per message.
