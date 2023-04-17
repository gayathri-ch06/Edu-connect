import os
from tkinter import Frame, Label, filedialog
import tkinter as tk

from services.services import download_file


class Files:
    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.label = Label(self.frame, text="Files Page", font=("Arial", 20))
        self.label.pack()

        self.file_listbox = tk.Listbox(self.frame)
        self.file_listbox.pack()

        # Get a list of files in the downloads directory
        self.download_dir = 'server/uploads/lecturer/Materials'
        files = os.listdir(self.download_dir)

        # Add each file to the listbox
        for file in files:
            self.file_listbox.insert(tk.END, file)

        # Create a button to download the selected file
        download_button = tk.Button(self.frame, text='Download', command=self.download_file)
        download_button.pack()

    def download_file(self):
        selected_file = self.file_listbox.get(tk.ACTIVE)
        print(self.download_dir + "/" + selected_file)
        path = self.download_dir + "/" + selected_file
        file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
        download_file(file_path, path)
