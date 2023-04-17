import tkinter as tk
from tkinter import filedialog
import os

from services.services import uploadFile, download_file


class Assignments:
    def __init__(self, root):
        self.file_path = ''
        self.frame = tk.Frame(root)
        self.frame.pack()
        self.label = tk.Label(self.frame, text="Selected file: ")
        self.label.pack(side=tk.TOP)
        self.browse_button = tk.Button(self.frame, text="Browse", command=self.browse_file)
        self.browse_button.pack(side=tk.LEFT)

        self.upload_button = tk.Button(self.frame, text="Upload file", command=self.upload_file)
        self.upload_button.pack(side=tk.LEFT)

        self.success_label = tk.Label(self.frame, text="", font=('Arial', 20))
        self.success_label.pack(side=tk.TOP)

        self.file_listbox = tk.Listbox(root)
        self.file_listbox.pack()

        # Get a list of files in the downloads directory
        self.download_dir = 'server/uploads/student/assignment'
        files = os.listdir(self.download_dir)

        # Add each file to the listbox
        for file in files:
            self.file_listbox.insert(tk.END, file)

        # Create a button to download the selected file
        download_button = tk.Button(root, text='Download', command=self.download_file)
        download_button.pack()

    def download_file(self):
        selected_file = self.file_listbox.get(tk.ACTIVE)
        print(self.download_dir + "/" + selected_file)
        path = self.download_dir + "/" + selected_file
        file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
        download_file(file_path, path)

    def browse_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        filename = os.path.basename(self.file_path)
        self.label.configure(text=f"Selected file: {filename}")

    def upload_file(self):
        if self.file_path:
            filename = os.path.basename(self.file_path)
            file_extension = os.path.splitext(self.file_path)[1]
            file_extension = file_extension[1:]
            res = uploadFile(filename, self.file_path, file_extension, 'lecturer', 'Assignments')
            if res['success']:
                self.success_label.configure(text="File upload success")
            else:
                self.success_label.configure(text="Something went wrong")
        else:
            self.label.configure(text="No file selected")
