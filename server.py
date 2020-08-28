from socket import *
from tkinter import *
from threading import *

def clientThread()
	#takes care of most things


hostSocket = socket(AF_INET, SOCK_STREAM)
hostSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

hostIp = "127.0.0.1"
portNumber = 7500
hostSocket.bind((hostIp, portNumber))
hostSocket.listen()
hostSocket.listen()
print ("Waiting for connection...")
