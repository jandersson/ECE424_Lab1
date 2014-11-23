__author__ = 'Jonas Andersson'

import time
import dbTools
try:
    import thread
except ImportError:
    import _thread as thread
import json  # handles serializing and sending/receiving JSON data
from socket import *
try:
    from tkinter import *
except ImportError:
    from Tkinter import *


def serve_forever():
    #TODO: remove import * for socket
    myHost = '127.0.0.1'
    myPort = 50007
    sockobj = socket(AF_INET, SOCK_STREAM)
    # the SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting
    # for its natural timeout to expire. Preventing the OSError: [Errno 98] Address already in use
    sockobj.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockobj.bind((myHost, myPort))
    sockobj.listen(5)
    return sockobj

def now():
    return time.ctime(time.time())


def handleClient(connection):
    while True:
        raw_data = connection.recv(1024).decode()
        if not raw_data:
            break
        reply = 'error'
        data = json.loads(raw_data)

        #inspect data header and determine action
        if data['header'] == 'measurements':
            data['time'] = now()
            print('Message is measurements')
            dbTools.insert_measurements(data)
            reply = json.dumps(data)
        if data['header'] == 'get measurements':
            print('Message is data retrieval request')
            measurements = dbTools.get_latest_measurement(data['username'])
            reply = json.dumps(measurements)
        if data['header'] == 'login info':
            print('Message is authentication request')
            data['authenticated'] = verify(data)
            reply = json.dumps(data)
        connection.send(reply.encode())


def verify(login_info):
    '''
    Verifies the user submitted login info and returns true if verified or false if verification failed.
    If the get_login function returns None, no match was found in the database and verification fails
    If the get_login function returns a tuple, a match was found in the database and the user is verified
    :param login_info:
    :return:
    '''
    result = dbTools.get_login(login_info)
    if not result:
        return False
    else:
        return True


def dispatcher(sockobj):
    while True:
        connection, address = sockobj.accept()
        print('Server connected by', address, 'at', now())
        thread.start_new_thread(handleClient, (connection,))


def makeWindow(myTitle):
    root = Tk()
    root.title(myTitle)
    label1 = Label(root, text='Server is running!')
    label1.pack()
    root.mainloop()


def start_server():
    dbTools.make_tables()
    sockobj = serve_forever()
    thread.start_new_thread(makeWindow, ('Server',))
    dispatcher(sockobj)