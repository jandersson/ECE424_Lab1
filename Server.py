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
        raw_data = connection.recv(1024).decode()
        if not raw_data: break
        reply = 'error'
        data = json.loads(raw_data)

        #inspect data header and determine action
        if data['header'] == 'measurements':
            print('File is measurements')
            with open("test.txt", "w") as outfile:
                json.dump(data, outfile, indent=4)
                reply = json.dumps(data)
        if data['header'] == 'get measurements':
            print('File is data request')
            measurements = loadMeasures(data['username'])
            reply = json.dumps(measurements)
        if data['header'] == 'login info':
            print('File is authentication request')
            data['authenticated'] = verify(data)
            reply = json.dumps(data)
        connection.send(reply.encode())
####################################

## Modify following code for lab2 ##
def verify(login_info):
    with open("accounts.txt", "r") as account_file:
        accounts = json.load(account_file)
    for key,users in accounts.items():
        for user in users:
            if (user['username'] == login_info['username']) and (user['password'] == login_info['password']):
                return True
    return False
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
    with open (fileName, 'r') as account_file:
        pass
    return
####################################

## Modify following code for lab2 ##
def loadMeasures(username):
    print('Loading measurements for ' + username)
    with open(username + '.txt', "r") as measurements:
        return json.load(measurements)
####################################

def start_server():
    thread.start_new_thread(makeWindow, ('Server',))
    dispatcher()

