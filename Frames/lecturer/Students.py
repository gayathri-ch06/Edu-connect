import tkinter as tk
from tkinter import ttk

from services.services import getStudents


class Students:
    def __init__(self, root, res):
        if res:
            # Create a canvas to hold the labels
            canvas = tk.Canvas(root)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            # Add a scrollbar to the canvas
            scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            # Configure the canvas to use the scrollbar
            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

            # Create a frame to hold the labels
            label_frame = tk.Frame(canvas)
            canvas.create_window((0, 0), window=label_frame, anchor='nw')

            # Add labels to the frame
            for name in res['message']:
                label = tk.Label(label_frame, width=15, text=name['name'], font=('Arial', '15'))
                label.pack(padx=5, pady=5)
