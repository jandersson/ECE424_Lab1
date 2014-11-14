__author__ = 'Jonas Andersson'

try:
    import thread
except ImportError:
    import _thread as thread

try:
    from tkinter import *
    from tkinter import messagebox
except ImportError:
    from Tkinter import *
    import tkMessageBox

import socket
import Server
import json  # used for serializing data for socket buffer


class Login:

    def __init__(self, master):
        self.master = master
        #Instantiate the frame and display it
        self.frame = Frame(self.master)
        self.frame.pack()
        self.master.title('Client')
        self.measurement = {'header': 'measurements',
                            'username': None,
                            'height': None,
                            'weight': None,
                            'blood pressure': None}
        self.login_info = {'header': 'login info',
                           'username': None,
                           'password': None,
                           'authenticated': False}
        self.make_menu()

    def login(self, master):
        #Display the login window
        self.login_window = Toplevel(master)
        self.login_window.title('Log-In')

        self.username_label = Label(self.login_window, text="Name")
        self.username_label.grid(column=0, row=0)

        self.user_entry = Entry(self.login_window)
        self.user_entry.bind('<Return>', (lambda x: self.verify()))
        self.user_entry.grid(column=1, row=0)

        self.ID_label = Label(self.login_window, text="ID")
        self.ID_label.grid(column=0, row=1)

        self.password_entry = Entry(self.login_window)
        self.password_entry.bind('<Return>', (lambda x: self.verify()))
        self.password_entry.grid(column=1, row=1)

        self.login_btn = Button(self.login_window, text='Login', command=lambda: self.verify())
        self.login_btn.grid(column=0, row=2)

        self.cancel_btn = Button(self.login_window, text='Cancel', command=self.login_window.destroy)
        self.cancel_btn.grid(column=1, row=2)

        self.login_window.wait_window()

    def make_menu(self):
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)
        file = Menu(menu_bar)
        menu_bar.add_cascade(label='File', menu=file, underline=0)
        account = Menu(menu_bar)
        menu_bar.add_cascade(label='Account', menu=account, underline=0)
        measure = Menu(menu_bar)
        menu_bar.add_cascade(label='Measure', menu = measure, underline=0)

        #Populate options (in a logged out state)
        #Register event handlers
        if not self.login_info['authenticated']:
            file.add_command(label='Save', command=self.save, underline=0, state='disabled')
            account.add_command(label='Log-In', command=lambda: self.login(self.master), underline=0, state='active')
            account.add_command(label='Log-Out', command=self.logout, underline=0, state='disabled')
            measure.add_command(label='Current', underline=0, state='disabled')
            measure.add_command(label='Last', underline=0, state='disabled')
        if self.login_info['authenticated']:
            file.add_command(label='Save', command=self.save, underline=0, state='active')
            account.add_command(label='Log-In', command=lambda: self.login(self.master), underline=0, state='disabled')
            account.add_command(label='Log-Out', command=self.logout, underline=0, state='active')
            measure.add_command(label='Current', command=lambda: self.measure(self.master), underline=0, state='active')
            measure.add_command(label='Last', command=lambda: self.get_measurement(), underline=0, state='active')

    def logout(self):
        try:
            if messagebox.askyesno("Logout", "Logout?"):
                self.login_info['authenticated'] = False
                self.make_menu()
        except NameError:
            if tkMessageBox.askyesno("Logout", "Logout?"):
                self.login_info['authenticated'] = False
                self.make_menu()

    def save(self):
        try:
            if messagebox.askyesno("Save", "Save?"):
                self.master.destroy()
        except NameError:
            if tkMessageBox.askyesno("Save", "Save?"):
                self.master.destroy()

    def verify(self):
        self.login_info['username'] = str(self.user_entry.get())
        self.login_info['password'] = str(self.password_entry.get())
        reply = self.send_data(self.login_info)
        if reply['authenticated']:
            self.login_info['authenticated'] = True
            try:
                messagebox.showinfo("Logged In", "You have successfully logged in")
            except NameError:
                tkMessageBox.showinfo("Logged In", "You have successfully logged in")
            self.login_window.destroy()
            self.make_menu()
        else:
            try:
                messagebox.showerror("Invalid Name/ID", "You have entered an invalid Name/ID, please try again")
            except NameError:
                tkMessageBox.showerror("Invalid Name/ID", "You have entered an invalid Name/ID, please try again")

    def measure(self, master):
        self.measure_window = Toplevel(master)
        self.measure_window.title('Measurement')

        #Create Labels
        self.height_label = Label(self.measure_window, text='Height')
        self.height_label.grid(column=0, row=0)
        self.weight_label = Label(self.measure_window, text='Weight')
        self.weight_label.grid(column=0, row= 1)
        self.bp_label = Label(self.measure_window, text='Blood Pressure')
        self.bp_label.grid(column=0, row=2)

        #Create Entries
        self.height_entry = Entry(self.measure_window)
        self.height_entry.grid(column=1, row=0)
        self.weight_entry = Entry(self.measure_window)
        self.weight_entry.grid(column=1, row=1)
        self.bp_entry = Entry(self.measure_window)
        self.bp_entry.grid(column=1, row=2)

        #Create Buttons
        self.enter_button = Button(self.measure_window, text='Enter', command=lambda: self.send_measurement())
        self.enter_button.grid(column=0, row =3)
        self.cancel_button = Button(self.measure_window, text='Cancel', command=lambda: self.measure_window.destroy())
        self.cancel_button.grid(column=1, row=3)
        self.measure_window.wait_window()

    def get_measurement(self):
        measurements = self.send_data({'username': self.login_info['username'],
                                       'header': 'get measurements'})
        try:
            messagebox.showinfo('Measurement', 'Name: ' + self.login_info['username'] +
                                '\nHeight: ' + measurements['height'] +
                                '\nWeight: ' + measurements['weight'] +
                                '\nBlood Pressure: ' + measurements['blood pressure'])
        except NameError:
            tkMessageBox.showinfo('Measurement', 'Name: ' + self.login_info['username'] +
                                  '\nHeight: ' + measurements['height'] +
                                  '\nWeight: ' + measurements['weight'] +
                                  '\nBlood Pressure: ' + measurements['blood pressure'])


    def send_data(self, raw_data):
        data = json.dumps(raw_data)
        sock = self.open_connection()
        sock.send(data.encode())
        print("Data Sent")
        raw_reply = sock.recv(1024).decode()
        reply = json.loads(raw_reply)
        print('Reply received')
        sock.close()
        return reply

    def send_measurement(self):
        """This function gets a socket object from the open_connection function and then sends the measurement data"""
        self.measurement['height'] = self.height_entry.get()
        self.measurement['weight'] = self.weight_entry.get()
        self.measurement['blood pressure'] = self.bp_entry.get()
        self.measurement['username'] = self.login_info['username']
        self.send_data(self.measurement)
        self.measure_window.destroy()

    def open_connection(self):
        sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create a socket object
        sockobj.connect(('127.0.0.1', 50007)) #Connect to server
        print('Socket created')
        return sockobj

def makeWindow(myTitle):
    root = Tk()
    lab1 = Login(root)
    root.title(myTitle)
    root.mainloop()

if __name__ == '__main__':
    thread.start_new_thread(makeWindow, ('Client',))
    Server.start_server()



