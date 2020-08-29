from socket import *
from threading import *
from tkinter import *

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

hostIp = "127.0.0.1"
portNumber = 7500

canSend = 0

clientSocket.connect((hostIp, portNumber))

window = Tk()
window.title("poemly")

fullPoem = Text(window, width=50)
fullPoem.grid(row=0, column=0, padx=10, pady=10)

yourPoemLine = Entry(window, width=50)
yourPoemLine.insert(0,"")
yourPoemLine.grid(row=1, column=0, padx=10, pady=10)


def sendLine():
    global  canSend
    if canSend == 1:
        poemLine = yourPoemLine.get()

        yourPoemLine.delete("0",END)
        clientSocket.send(poemLine.encode("utf-8"))
        canSend = 0


sendLineBtn = Button(window, text="Add to Poem", width=20, command=sendLine)
sendLineBtn.grid(row=2, column=0, padx=10, pady=10)


def recvLine():
    global canSend
    while True:
        serverLine = clientSocket.recv(1024).decode("utf-8")
        if serverLine == "0110011101101111":
            canSend = 1
            fullPoem.insert(END, "\n" + "Your turn")

        else:
            print(serverLine)
            fullPoem.insert(END, "\n"+serverLine)


recvThread = Thread(target=recvLine)
recvThread.daemon = True
recvThread.start()

window.mainloop()
