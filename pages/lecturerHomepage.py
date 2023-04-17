import tkinter as tk
from tkinter import *

from Frames.lecturer.Materials import Materials
from Frames.lecturer.Students import Students
from Frames.lecturer.Assignments import Assignments
from Frames.student.Courses import Courses
from Frames.student.DiscussionForum import DiscussionForum
from Frames.lecturer.Feedback import Feedback
from Frames.lecturer.Quizzes import Quizzes
from services.services import getStudents, getAssignments, getFeedback


def destroyAllFrames(root):
    for frame in root.winfo_children():
        frame.pack_forget()
        for widget in frame.winfo_children():
            widget.destroy()


def goTo(self, frameName):
    destroyAllFrames(self)
    match frameName:
        case 'Students':
            res = getStudents()
            Students(self, res)
        case 'Assignments':
            # res = getAssignments()
            Assignments(self)
        case 'Quizzes':
            Quizzes(self)
        case 'Materials':
            Materials(self)
        case 'Feedback':
            Feedback(self)
        case 'exit':
            self.destroy()


class LecturerHomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('HomePage')
        self.geometry('500x300')
        self.tk.call('tk', 'useinputmethods', '1')
        self.bind("<KeyPress>", self.shortcut)

        # Creating Menubar
        menubar = Menu(self, tearoff=False)
        self.config(menu=menubar)

        # Adding Menus
        menubar.add_command(label='Students', command=lambda: goTo(self, 'Students'))
        menubar.add_command(label='Assignments', command=lambda: goTo(self, 'Assignments'))
        menubar.add_command(label='Quizzes', command=lambda: goTo(self, 'Quizzes'))
        menubar.add_command(label='Materials', command=lambda: goTo(self, 'Materials'))
        menubar.add_command(label='Feedback', command=lambda: goTo(self, 'Feedback'))
        menubar.add_command(label='Exit', command=lambda: goTo(self, 'exit'))

        goTo(self, 'Students')

    def shortcut(self, event):
        if event.keysym == 'Escape':
            return self.destroy()
