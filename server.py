from socket import *
from threading import *
import random

clients = []
players = 4


def clientThread(clientSocket, clientAddress):
    i = 0
    while True:
        clients[i].send("0110011101101111".encode("utf-8"))
        line = clients[i].recv(1024).decode("utf-8")
        print(clientAddress[0] + ":" + str(clientAddress[1]) + " says: " + line)
        i = i+1

        for client in clients:
            client.send(("added:     " + line).encode("utf-8"))

        if i > (players-1):
            for client in clients:
                client.send(" game over".encode("utf-8"))
            break

        if not line:
            clients.remove(clientSocket)
            print(clientAddress[0] + ":" + str(clientAddress[1]) + " disconnected")
            break
    clientSocket.close()


hostSocket = socket(AF_INET, SOCK_STREAM)
hostSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

hostIp = "127.0.0.1"
portNumber = 7500
hostSocket.bind((hostIp, portNumber))
hostSocket.listen()
print ("Waiting for connection...")


while True:
    clientSocket, clientAddress = hostSocket.accept()
    clients.append(clientSocket)
    print ("Connection established with: ", clientAddress[0] + ":" + str(clientAddress[1]))
    if len(clients) > (players-1):
        random.shuffle(clients)
        thread = Thread(target=clientThread, args=(clientSocket, clientAddress, ))
        thread.start()