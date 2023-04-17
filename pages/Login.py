import tkinter as tk
from tkinter import messagebox

from pages.lecturerHomepage import LecturerHomePage
from services.services import login
from pages.studenthomepage import StudentHomePage


def loginTo(email, password, usertype, self):
    res = login(email, password, usertype)
    if usertype == 'student':
        if res:
            self.destroy()
            StudentHomePage().mainloop()
        else:
            messagebox.showerror(title="Status", message="Invalid UserName or Password")
    if usertype == 'lecturer':
        if res:
            self.destroy()
            LecturerHomePage().mainloop()
        else:
            messagebox.showerror(title="Status", message="Invalid UserName or Password")


class Login(tk.Tk):
    def __init__(self, usertype):
        super().__init__()

        self.geometry("500x300")
        self.title(f'{usertype} login')
        self.bind("<KeyPress>", self.shortcut)
        label = tk.Label(self, text="Enter your Credentials", font=('Helvetica', 18))
        label.pack(padx=10, pady=20)

        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.userType = usertype

        frame = tk.Frame(self)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        emailLabel = tk.Label(frame, text="Login ID", font=('Helvetica', 14))
        emailLabel.grid(row=0, column=0, padx=10, pady=10)

        emailBox = tk.Entry(frame, width=15, font=('Arial', 14), textvariable=self.email)
        emailBox.grid(row=0, column=1, padx=10, pady=10)

        passwordLabel = tk.Label(frame, text="Password", font=('Helvetica', 14))
        passwordLabel.grid(row=1, column=0, padx=10, pady=10)

        passwordBox = tk.Entry(frame, width=15, show='*', font=('Arial', 14), textvariable=self.password)
        passwordBox.grid(row=1, column=1, padx=10, pady=10)
        frame.pack(fill='x', pady=10, padx=10)

        loginButton = tk.Button(self, text="Login", font=('Helvetica', 14), command=self.login)
        loginButton.pack(padx=10, pady=10)

        exitButton = tk.Button(self, text="Exit", font=('Helvetica', 14), command=self.destroy)
        exitButton.pack(padx=10, pady=10)

    def login(self):
        email = self.email.get()
        password = self.password.get()
        loginTo(email, password, self.userType, self)

    def shortcut(self, event):
        if event.keysym == 'Return':
            return self.login()
        if event.keysym == 'Esc':
            return self.destroy()