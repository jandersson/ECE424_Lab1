__author__ = 'Jonas'

import time, _thread as thread
from socket import *
from tkinter import *

myHost = ''
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)

def now():
    return time.ctime(time.time())

## Modify following code for lab2 ##
def handleClient(connection):
    while True:
        data = connection.recv(1024).decode()

        if not data: break
        reply='Lab2_echo--'+data
        connection.send(reply.encode())
####################################

## Modify following code for lab2 ##
def verify(data, name, pwd):

    return
####################################

## Modify following code for lab2 ##
def dispatcher():
    while True:
        connection, address = sockobj.accept()
        print('Server connected by', address,'at', now())

        thread.start_new_thread(handleClient, (connection,))
####################################

def makeWindow(myTitle):
    root = Tk()
    root.title(myTitle)
    label1 = Label(root, text='Server is running!')
    label1.pack()
    root.mainloop()

## Modify following code for lab2 ##
def loadAccounts(fileName,name,pwd,pri):

    return
####################################

## Modify following code for lab2 ##
def loadMeasures(connection):

    return
####################################

thread.start_new_thread(makeWindow, ('ECE424_Lab2_Server',))
dispatcher()

