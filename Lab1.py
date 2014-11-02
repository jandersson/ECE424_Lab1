__author__ = 'Jonas Andersson'

import _thread as thread, socket
from tkinter import *  # get widget classes
from tkinter import messagebox
import Server

class Login:

    def __init__(self, master):
        self.master = master
        self.logged_in = True
        #Instantiate the frame and display it
        self.frame = Frame(self.master)
        self.frame.pack()
        self.master.title('Client')
        self.make_menu()
        self.open_connection()

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
        if not self.logged_in:
            file.add_command(label='Save', command=self.save, underline=0, state='disabled')
            account.add_command(label='Log-In', command=lambda:self.login(self.master), underline=0, state='active')
            account.add_command(label='Log-Out', command=self.logout, underline=0, state='disabled')
            measure.add_command(label='Current', underline=0, state='disabled')
            measure.add_command(label='Last', underline=0, state='disabled')
        if self.logged_in:
            file.add_command(label='Save', command=self.save, underline=0, state='active')
            account.add_command(label='Log-In', command=lambda:self.login(self.master), underline=0, state='disabled')
            account.add_command(label='Log-Out', command=self.logout, underline=0, state='active')
            measure.add_command(label='Current', command=lambda:self.measure(self.master), underline=0, state='active')
            measure.add_command(label='Last', command=lambda:self.get_measurement(), underline=0, state='active')

    def logout(self):
        if messagebox.askyesno("Logout", "Logout?"):
            self.logged_in = False
            self.make_menu()

    def save(self):

        if messagebox.askyesno("Save", "Save?"):
            self.master.destroy()

    def verify(self):
        username = str(self.user_entry.get())
        password = str(self.password_entry.get())
        if (username == "test") and (password == "1234"):
            self.logged_in = True
            messagebox.showinfo("Logged In", "You have successfully logged in")
            self.login_window.destroy()
            self.make_menu()
        else:
            messagebox.showerror("Invalid Name/ID", "You have entered an invalid Name/ID, please try again")

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
        self.enter_button = Button(self.measure_window, text='Enter', command=lambda:self.send_measurement)
        self.enter_button.grid(column=0, row =3)
        self.cancel_button = Button(self.measure_window, text='Cancel', command=lambda:self.measure_window.destroy())
        self.cancel_button.grid(column=1, row=3)
        self.measure_window.wait_window()

    def get_measurement(self):
        messagebox.showinfo('Measurement', 'Name:\n' + 'Height:\n' + 'Weight:\n' + 'Blood Pressure:\n')

    def send_measurement(self):
        pass

    def open_connection(self):
        #Create Socket object
        sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Connect
        sockobj.connect(('127.0.0.1', 50007))
        print('Socket created')


def makeWindow(myTitle):
    root = Tk()
    lab1 = Login(root)
    root.title(myTitle)
#    label1 = Label(root, text='Server is running!')
#    label1.pack()
    root.mainloop()

if __name__ == '__main__':

    thread.start_new_thread(makeWindow, ('Client',))
    #root = Tk()  # or Toplevel()
    #lab1 = Login(root)
    #root.mainloop()
    Server.start_server()



