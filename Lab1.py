__author__ = 'Jonas Andersson'

from Tkinter import *  # get widget classes

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
        account.add_command(label='Log-In', command=self.login(master), underline=0, state='active')
        account.add_command(label='Log-Out', command=self.logout, underline=0, state='disabled')

    def login(self, master):
        #Handler for the login event
        loginwindow = Toplevel(master)
        user_entry = Entry(loginwindow)
        user_entry.pack()
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
        pass

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
    # root.title('ECE424_Lab1')  # set window-mgr info
    # makemenu(root, False)  # associate a menu bar
    root.mainloop()
    root.destroy()

