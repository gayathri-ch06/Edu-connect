import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from services.services import submit

user_answers = {}

class Quizzes:
    def __init__(self, root, res):
        root.title("Quiz")
        self.questions = res['message']

        # Create a dictionary to store the user's answers
        self.user_answers = {}

        # Create a frame to display the questions
        self.questions_frame = tk.Frame(root)
        self.questions_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create a canvas to add a scrollbar
        self.canvas = tk.Canvas(self.questions_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a scrollbar to the canvas
        self.scrollbar = ttk.Scrollbar(self.questions_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))

        # Create a frame to hold the questions and options
        self.questions_container = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.questions_container, anchor='nw')

        # Add a label to display the title of the quiz
        self.title_label = tk.Label(self.questions_container, text="Quiz")
        self.title_label.pack(side=tk.TOP, padx=5, pady=5)

        # Loop through each question and add it to the frame
        for i, question in enumerate(self.questions):
            # Add a label for the question
            question_label = tk.Label(self.questions_container, text=f"{i + 1}. {question['question']}")
            question_label.pack(side=tk.TOP, padx=5, pady=5)

            # Loop through each option and add it to the frame as a radio button
            for option in question["options"]:
                option_button = tk.Radiobutton(self.questions_container, text=option, variable=i, value=option,
                                               command=lambda i=i, option=option: self.select_option(i, option))
                option_button.pack(side=tk.TOP, padx=5, pady=2)

        # Add a button to submit the answers
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answers)
        self.submit_button.pack(side=tk.TOP, padx=10, pady=10)

        # Add a label to display the result of the quiz
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(side=tk.TOP, padx=10, pady=10)

        # Resize the main window to fit the content
        root.update()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        root.geometry(f"{self.questions_frame.winfo_width()+self.scrollbar.winfo_width()+50}x{self.questions_frame.winfo_height()+self.submit_button.winfo_height()+self.result_label.winfo_height()+100}")

    # Function to handle selection of an option
    def submit_answers(self):
        # Check if all questions have been answered
        if len(self.user_answers) != len(self.questions):
            self.result_label.config(text="Please answer all questions.")
            return

        # Check each answer and update the result label
        correct_answers = 0
        quiz_data = []
        for i, question in enumerate(self.questions):
            quiz_data.append({"question": question['question'], "answer": self.user_answers[i]})
            if self.user_answers[i] == question["answer"]:
                correct_answers += 1
        res = submit(quiz_data, 'quiz')
        if res['status']:
            messagebox.showinfo(title="Login Status", message=res['message'])
        else:
            messagebox.showinfo(title="Login Status", message="Something went wrong")
        self.result_label.config(text=f"You got {correct_answers} out of {len(self.questions)} questions correct.")

    def select_option(self, question_index, option):
        self.user_answers[question_index] = option