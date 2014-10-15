__author__ = 'Jonas Andersson'

from tkinter import *  # get widget classes

#Initialize Global State
logged_in = False

class Login:

    def __init__(self, master):

        #Instantiate the frame and display it
        frame = Frame(master)
        frame.pack()

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
        loginwindow = Toplevel(master)

        username = StringVar()
        user_entry = Entry(loginwindow, textvariable=username)
        user_entry.pack()

        password = StringVar()
        password_entry = Entry(loginwindow, textvariable=password)
        password_entry.pack()

        login_btn = Button(loginwindow, text='Login', command=lambda:self.verify(username,"Logged in!"))
        login_btn.pack()
        cancel_btn = Button(loginwindow, text='Cancel')
        cancel_btn.pack()

        loginwindow.wait_window()


    def makeform(self, root, fields):
        ### Write your code here###
        pass

    def logout(self):
        ### Write your code here###
        pass

    def save(self):
        ### Write your code here###
        pass

    def verify(self, entries, dialog):
        ### Write your code here###
        print(dialog + entries)

# def makemenu(win, cond):
#     if not cond:
#
#     else:
#         file.add_command(label='Save', command=save, underline=0, state='active')
#         account.add_command(label='Log-In', command=login, underline=0, state='disabled')
#         account.add_command(label='Log-Out', command=logout, underline=0, state='active')

if __name__ == '__main__':

    root = Tk()  # or Toplevel()
    root.title('ECE424_Lab1')  # set window-mgr info
    lab1 = Login(root)

    # makemenu(root, False)  # associate a menu bar
    root.mainloop()
    root.destroy()

