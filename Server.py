__author__ = 'Jonas Andersson'

import ssl
import pprint
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
        #raw_data = connection.recv(1024).decode()
        raw_data = connection.read().decode()
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
        connection.write(reply.encode())


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
        try:
            connection, address = sockobj.accept()
            connstream = ssl.wrap_socket(connection,
                                     server_side=True,
                                     certfile="server_cert.pem",
                                     keyfile="server_cert.pem",
                                     ca_certs="client_cert.pem",
                                     cert_reqs=ssl.CERT_REQUIRED)
            print('Server connected by', address, 'at', now())
            print(repr(connstream.getpeername()))
            print(connstream.cipher())
            print(pprint.pformat(connstream.getpeercert()))
            thread.start_new_thread(handleClient, (connstream,))
        except ssl.SSLError:
            print("Authentication error detected. Logging event")
            log_error(address)

def log_error(address):
    try:
        with open("log.txt", "a") as log:
            log.write("SSL Error: " + 'Server connected by ' + str(address) + ' at ' + str(now()) + "\n")
    except IOError:
        with open("log.txt", "w") as log:
            log.write("SSL Error: " + 'Server connected by ' + str(address) + ' at ' + str(now()) + "\n")


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