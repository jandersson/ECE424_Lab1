__author__ = 'Jonas Andersson'

from tkinter import *  # get widget classes
from tkinter import messagebox

#Initialize Global State
logged_in = False

class Login:

    def __init__(self, master):
        self.master = master
        #Instantiate the frame and display it
        self.frame = Frame(self.master)
        self.frame.pack()
        self.master.title('ECE424_Lab1')
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

        #Populate options (in a logged out state)
        #Register event handlers
        if not logged_in:
            file.add_command(label='Save', command=self.save, underline=0, state='disabled')
            account.add_command(label='Log-In', command=lambda:self.login(self.master), underline=0, state='active')
            account.add_command(label='Log-Out', command=self.logout, underline=0, state='disabled')
        if logged_in:
            file.add_command(label='Save', command=self.save, underline=0, state='active')
            account.add_command(label='Log-In', command=lambda:self.login(self.master), underline=0, state='disabled')
            account.add_command(label='Log-Out', command=self.logout, underline=0, state='active')

    def logout(self):
        global logged_in
        if messagebox.askyesno("Logout", "Logout?"):
            logged_in = False
            self.make_menu()

    def save(self):

        if messagebox.askyesno("Save", "Save?"):
            self.master.destroy()

    def verify(self):
        global logged_in
        username = str(self.user_entry.get())
        password = str(self.password_entry.get())
        if (username == "test") and (password == "1234"):
            logged_in = True
            messagebox.showinfo("Logged In", "You have successfully logged in")
            self.login_window.destroy()
            self.make_menu()
        else:
            messagebox.showerror("Invalid Name/ID", "You have entered an invalid Name/ID, please try again")

if __name__ == '__main__':

    root = Tk()  # or Toplevel()
    lab1 = Login(root)
    root.mainloop()