from socket import *
from tkinter import *
from threading import *


clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

hostIp = "127.0.0.1"
portNumber = 7500

canSend = 0

clientSocket.connect((hostIp, portNumber))


def sendLine():
	#sends a line to the server


def recvLine():
	#recieves a line from the server