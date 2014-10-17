__author__ = 'Jonas Andersson'

from tkinter import *  # get widget classes

#Initialize Global State
logged_in = False

class DialogBox(Toplevel):

    def __init__(self, parent, title = None):
        Toplevel.__init__(self, parent)
        self.transient(parent)

        if title:
            self.title(title)

        body = Frame(self)
        self.body()
        body.pack(padx=5, pady=5)

        self.wait_window(self)

    def body(self):
        user_entry = Entry(self)
        user_entry.bind('<Return>', (lambda:self.verify))
        user_entry.pack()

    def verify(self):
        username = self.user_entry.get()
        print(username)

class Login:

    def __init__(self, master):

        #Instantiate the frame and display it
        self.frame = Frame(master)
        self.frame.pack()
        master.title('ECE424_Lab1')
        #Create options menu bar
        menu_bar = Menu(master)
        master.config(menu=menu_bar)
        file = Menu(menu_bar)
        menu_bar.add_cascade(label='File', menu=file, underline=0)
        account = Menu(menu_bar)
        menu_bar.add_cascade(label='Account', menu=account, underline=0)

        #Populate options (in a logged out state)
        #Register event handlers
        file.add_command(label='Save', command=self.save, underline=0, state='disabled')
        account.add_command(label='Log-In', command=lambda:self.login(master), underline=0, state='active')
        account.add_command(label='Log-Out', command=self.logout, underline=0, state='disabled')

    def login(self, master):
        #Handler for the login event
        self.login_window = Toplevel(master)
        self.login_window.title('Log-In')

        self.username_label = Label(self.login_window, text="Name")
        self.username_label.grid(column=0, row=0)
        self.username_label.pack()

        self.user_entry = Entry(self.login_window)
        self.user_entry.bind('<Return>', (lambda x: self.verify()))
        self.user_entry.grid(column=1, row=0)
        self.user_entry.pack()

        self.ID_label = Label(self.login_window, text="ID")
        self.ID_label.grid(column=0, row=1)
        self.ID_label.pack()

        self.password_entry = Entry(self.login_window)
        self.password_entry.bind('<Return>', (lambda x: self.verify()))
        self.password_entry.grid(column=1, row=1)
        self.password_entry.pack()

        self.login_btn = Button(self.login_window, text='Login', command=lambda: self.verify())
        self.login_btn.grid(column=0, row=2)
        self.login_btn.pack()

        self.cancel_btn = Button(self.login_window, text='Cancel', command=self.login_window.destroy)
        self.login_btn.grid(column=1, row=2)
        self.cancel_btn.pack()



        self.login_window.wait_window()


    def make_form(self, root, fields):
        ### Write your code here###
        pass

    def logout(self):
        ### Write your code here###
        pass

    def save(self):
        ### Write your code here###
        pass

    def verify(self):
        global logged_in
        username = str(self.user_entry.get())
        password = str(self.password_entry.get())
        if (username == "test") and (password == "1234"):
            logged_in = True
            print("Successfully Logged in!")
            self.login_window.destroy()
        else:
            print("That is not a valid username/password")


# def makemenu(win, cond):
#     if not cond:
#
#     else:
#         file.add_command(label='Save', command=save, underline=0, state='active')
#         account.add_command(label='Log-In', command=login, underline=0, state='disabled')
#         account.add_command(label='Log-Out', command=logout, underline=0, state='active')

if __name__ == '__main__':

    root = Tk()  # or Toplevel()
    lab1 = Login(root)
    # makemenu(root, False)  # associate a menu bar
    root.mainloop()
    root.destroy()

