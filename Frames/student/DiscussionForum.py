import tkinter as tk


class DiscussionForum:
    def __init__(self, root):
        root.geometry('500x300')
        self.frame = tk.Frame(root)
        self.frame.pack()
        self.label = tk.Label(self.frame, text="Discussion Forum Page")
        self.label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.messages = tk.Listbox(self.frame, width=100)
        self.messages.pack(expand=True)

        self.entry = tk.Text(self.frame, height=5)
        self.entry.pack(side=tk.BOTTOM, fill=tk.X)
        self.entry.bind("<Return>", self.add_message)

    def add_message(self, event):
        message = self.entry.get("1.0", "end-1c")
        self.entry.delete("1.0", tk.END)
        self.messages.insert(tk.END, message)
