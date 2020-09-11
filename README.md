# backoffstrategies
Goal:
The goal of the project is to gain first-hand experience of the utility of backoff strategies for reducing collisions.
Problem Statement: 
Implement three different client codes that do the following:
1. It sends 20 messages to the server. After sending each message, the client waits up to 1 second for a response from the server. If a response is received within this time, it prints the response. Otherwise, it retries after a delay. The three clients will have three delay strategies:
1. No delay. The request is resent immediately without any backoff.
2. Exponential backoff.
3. Linear backoff.
In each case, the client gives up and moves on to the next request at the end of 10 attempts. At the end, the client prints out the average number of attempts per message.
