import tkinter as tk
from tkinter import messagebox

from services.services import submit


class Feedback:
    def __init__(self, root):
        self.frame = tk.Frame(root)
        tk.Label(self.frame, text="Feedback Page", font=("Arial", 20)).grid(row=0, column=0)
        tk.Label(self.frame, text="No Files Available").grid(row=1, column=0)

        frame2 = tk.Frame(root)
        frame2.columnconfigure(0, weight=1)
        frame2.columnconfigure(1, weight=1)
        frame2.columnconfigure(2, weight=1)

        emailLabel = tk.Label(frame2, text="Email", font=('Helvetica', 14))
        emailLabel.grid(row=1, column=0)

        self.emailBox = tk.Entry(frame2, width=35, font=('Arial', 14))
        self.emailBox.grid(row=1, column=1, columnspan=3)

        feedbackLabel = tk.Label(frame2, text="Feedback", font=('Helvetica', 14))
        feedbackLabel.grid(row=2, column=0)

        self.feedbackBox = tk.Text(frame2, width=35, height=5, font=('Arial', 14))
        self.feedbackBox.grid(row=2, column=1, columnspan=3)
        frame2.pack()

        submitButton = tk.Button(root, text="Submit", font=('Helvetica', 14), command=self.submit)
        submitButton.pack(padx=10, pady=10)

    def submit(self):
        email = self.emailBox.get()
        feedback = self.feedbackBox.get("1.0", "end-1c")
        data = {"email": email, "feedback": feedback}
        res = submit(data, 'feedback')
        if res['status']:
            messagebox.showinfo(title="Login Status", message=res['message'])
        else:
            messagebox.showinfo(title="Login Status", message="Something went wrong")
