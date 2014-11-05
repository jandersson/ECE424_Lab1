__author__ = 'Jonas Andersson'

import time, _thread as thread
import json  #handles serializing and sending/receiving JSON data
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
        #reply='Lab2_echo--'+data
        data = json.loads(data)

        #inspect data header and determine action
        if data['header'] == 'measurements':
            with open("test.txt", "w") as outfile:
                json.dump(data, outfile, indent=4)
                reply = data
        if data['header'] == 'get measurements':
            reply = loadMeasures()
            with open(data['username'] + '.txt', "r") as measurements:
                user_measurements = json.loads(measurements)
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

def start_server():
    thread.start_new_thread(makeWindow, ('Server',))
    dispatcher()

