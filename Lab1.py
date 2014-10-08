__author__ = 'Jonas'
from tkinter import * # get widget classes
from tkinter.messagebox import * # get standard dialogs

def close():
    root.destroy()

def login():
    ### Write your code here###
    return

def makeform(root, fields):
    ### Write your code here###
    return

def logout():
    ### Write your code here###
    return

def save():
    ### Write your code here###
    return

def verify(entries,dialog):
    ### Write your code here###
    return

def makemenu(win,cond):
    top = Menu(win) # win=top-level window
    win.config(menu=top) # set its menu option
    file = Menu(top)
    top.add_cascade(label='File', menu=file, underline=0)
    account = Menu(top)
    top.add_cascade(label='Account', menu=account, underline=0)
    if cond==False:
        file.add_command(label='Save', command=save, underline=0,state='disabled')
        account.add_command(label='Log-In', command=login, underline=0,state='active')
        account.add_command(label='Log-Out', command=logout, underline=0,state='disabled')
    else:
        file.add_command(label='Save', command=save, underline=0,state='active')
        account.add_command(label='Log-In', command=login, underline=0,state='disabled')
        account.add_command(label='Log-Out', command=logout, underline=0,state='active')


if __name__ == '__main__':


    root = Tk() # or Toplevel()
    root.title('ECE424_Lab1') # set window-mgr info
    makemenu(root,False) # associate a menu bar

##From Lab
    widget = Button(root, text='Hello GUI World', command=close)
    widget.pack()

    root.mainloop()

