import tkinter as tk
from tkinter import filedialog
import os

from services.services import uploadFile


class Materials:
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

    def browse_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        filename = os.path.basename(self.file_path)
        self.label.configure(text=f"Selected file: {filename}")

    def upload_file(self):
        if self.file_path:
            filename = os.path.basename(self.file_path)
            file_extension = os.path.splitext(self.file_path)[1]
            file_extension = file_extension[1:]
            res = uploadFile(filename, self.file_path, file_extension, 'lecturer', 'Materials')
            if res['success']:
                self.success_label.configure(text="File upload success")
            else:
                self.success_label.configure(text="Something went wrong")
        else:
            self.label.configure(text="No file selected")
