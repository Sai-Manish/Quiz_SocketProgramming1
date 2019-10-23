import socket
import select
from thread import *
import sys
import time
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    print "Correct usage: script, IP address, port number"
    exit()

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.bind((IP_address, Port)) 
server.listen(100)

list_of_clients=[]

Q = ["(1) What is the total number of states in India\n(a) 29\n(b) 27\n(c) 28\n(d) 26",
"(2) What is the total number of union territories in India\n(a) 9\n(b) 7\n(c) 8\n(d) 6",
"(3) What is the largest state in india by area\n(a) Rajasthan\n(b) Uttar Pradesh\n(c) Karnataka\n(d) Gujarat",
"(4) What is the largest city in india by area\n(a) Bengaluru\n(b) Pune\n(c) Mumbai\n(d) bhopal",
"(5) Which state has highest population in India\n(a) Bihar\n(b) Maharashtra\n(c) West Bengal\n(d) Uttar Pradesh",
"(6) Which state has highest literacy rate in India\n(a) Mizoram\n(b) Goa\n(c) Kerala\n(d) Tripura",
"(7) Which state has highest GDP in India\n(a) Maharashtra\n(b) Uttar Pradesh\n(c) Karnataka\n(d) Tamil Nadu",
"(8) What is the rank of India in total land area in the world\n(a) 9\n(b) 7\n(c) 8\n(d) 6"
"(9)The ratio of width of our national flag to its length is\n(a)3:5\n(b)2:3\n(c)2:4\n(d)3:4\n"
"(10)In which Yuga,Shree Rama was born in Ayodhya\n(a)Satya Yuga\n(b)Treta Yuga\n(c)Dwapara Yuga\n(d)KaliYuga\n"
]

A = ['a','b','a','c','d','c','a','b','b','b']
Count=[]
client = ["address",-1]
buzzar =[0, 0, 0]

def clientthread(conn, addr):
    conn.send("Welcome to this Quiz world!\n")
    #sends a message to the client whose user object is conn
    while True:
                
            message = conn.recv(2048)  
            if message:
                if buzzar[0]==0:
                    client[0] = conn
                    buzzar[0] = 1
                    i = 0
                    while i < len(list_of_clients):
                            if list_of_clients[i] == client[0]:
                                break
                            i +=1
                    client[1] = i

                elif buzzar[0] ==1 and conn==client[0]:
                    
                        yal = message[0] == A[buzzar[2]][0]
                        print A[buzzar[2]][0] 
                        if yal:
                            broadcast("player " + str(client[1]+1) +" scored " + "+1" + "\n")
                            Count[i] += 1
                            if Count[i]==2:
                                endgame()

                        else:
                            broadcast("player" + str(client[1]+1) + " -1" + "\n")
                            Count[i] -= 1
                        buzzar[0]=0
                        if len(Q) != 0:
                            Q.pop(buzzar[2])
                            A.pop(buzzar[2])
                        if len(Q)==0:
                            endgame()
                        quiz()

                else:
                        conn.send("player " + str(client[1]+1) + " aldready pressed buzzer\n")
            else:
                    remove(conn)

'''def endgame():
        broadcast("GAME OVER\n")
        buz[1]=1
        j = Count.index(max(Count))
        broadcast("player " + str(j+1)+ " wins!! by scoring "+str(Count[j])+" points.")
        for i in range(len(list_of_clients)):
            list_of_clients[i].send("You scored " + str(Count[i]) + " points.")
            list_of_clients[i].exit()
        server.close()
'''
def broadcast(message):
    for clients in list_of_clients:
        try:
            clients.send(message)
        except:
            clients.close()
            remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

def quiz():
    buzzar[2] = random.randint(0,10000)%len(Q)
    if len(Q) != 0:
        for connection in list_of_clients:
            connection.send(Q[buzzar[2]])

def endgame():
        broadcast("GAME OVER\n")
        buzzar[1]=1
        j = Count.index(max(Count))
        broadcast("player " + str(j+1)+ " wins!! by scoring "+str(Count[j])+" points.")
        for i in range(len(list_of_clients)):
            list_of_clients[i].send("You scored " + str(Count[i]) + " points.")
            list_of_clients[i].exit()
        server.close()

while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    Count.append(0)
    print addr[0] + " connected"
    start_new_thread(clientthread,(conn,addr))
    if(len(list_of_clients)==3):
        quiz()
conn.close()
server.close()

