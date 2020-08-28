from socket import *
from tkinter import *
from threading import *



def clientThread()
	#takes care of most things
	 while True:
        line = clients[i].recv(1024).decode("utf-8")
        print(clientAddress[0] + ":" + str(clientAddress[1]) + " says: " + line)

        for client in clients:
            client.send(("added:     " + line).encode("utf-8"))

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
hostSocket.listen()
print ("Waiting for connection...")


while True:
    clientSocket, clientAddress = hostSocket.accept()
    clients.append(clientSocket)
    print ("Connection established with: ", clientAddress[0] + ":" + str(clientAddress[1]))   
    thread = Thread(target=clientThread, args=(clientSocket, clientAddress, ))
    thread.start()
