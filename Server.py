__author__ = 'Jonas Andersson'

import time
try:
    import thread
except ImportError:
    import _thread as thread
import json  #handles serializing and sending/receiving JSON data
from socket import *
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

def serve_forever():
    myHost = '127.0.0.1'
    myPort = 50007
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.bind((myHost, myPort))
    sockobj.listen(5)
    return sockobj

def now():
    return time.ctime(time.time())


def handleClient(connection):
    while True:
        raw_data = connection.recv(1024).decode()
        if not raw_data: break
        reply = 'error'
        data = json.loads(raw_data)

        #inspect data header and determine action
        if data['header'] == 'measurements':
            data['time'] = now()
            current_measures = loadMeasures(data['username'])
            current_measures.append(data)
            print('File is measurements')
            with open(data['username'] + ".txt", "w") as outfile:
                json.dump(current_measures, outfile, indent=4)
                reply = json.dumps(data)
        if data['header'] == 'get measurements':
            print('File is data request')
            measurements = loadMeasures(data['username'])
            #Get only the last item in the measurements list (the latest one)
            measurements = measurements[-1]
            reply = json.dumps(measurements)
        if data['header'] == 'login info':
            print('File is authentication request')
            data['authenticated'] = verify(data)
            reply = json.dumps(data)
        connection.send(reply.encode())


def verify(login_info):
    with open("accounts.txt", "r") as account_file:
        accounts = json.load(account_file)
    for key,users in accounts.items():
        for user in users:
            if (user['username'] == login_info['username']) and (user['password'] == login_info['password']):
                return True
    return False



def dispatcher(sockobj):
    while True:
        connection, address = sockobj.accept()
        print('Server connected by', address,'at', now())
        thread.start_new_thread(handleClient, (connection,))



def makeWindow(myTitle):
    root = Tk()
    root.title(myTitle)
    label1 = Label(root, text='Server is running!')
    label1.pack()
    root.mainloop()


def loadAccounts(fileName,name,pwd,pri):
    with open (fileName, 'r') as account_file:
        pass
    return


def loadMeasures(username):
    print('Loading measurements for ' + username)
    with open(username + '.txt', "r") as measurements:
        return json.load(measurements)


def start_server():
    sockobj = serve_forever()
    thread.start_new_thread(makeWindow, ('Server',))
    dispatcher(sockobj)

