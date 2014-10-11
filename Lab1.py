__author__ = 'Jonas'

from Tkinter import *  # get widget classes


class Login:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

    def login(self):
        print("Hello!")


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

#
# def makemenu(win, cond):
#     top = Menu(win)  # win=top-level window
#     win.config(menu=top)  # set its menu option
#     file = Menu(top)
#     top.add_cascade(label='File', menu=file, underline=0)
#     account = Menu(top)
#     top.add_cascade(label='Account', menu=account, underline=0)
#     if not cond:
#         file.add_command(label='Save', command=save, underline=0, state='disabled')
#         account.add_command(label='Log-In', command=login, underline=0, state='active')
#         account.add_command(label='Log-Out', command=logout, underline=0, state='disabled')
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

