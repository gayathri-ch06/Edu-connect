import tkinter as tk
from tkinter import messagebox

from PIL import ImageTk, Image

from services.services import enrollCourse

courses = [
    {"name": "Python Programming", "details": "Learn Python programming language.\nIn this Python course, students "
                                              "will learn the fundamentals of the Python programming language,"
                                              "\n including basic syntax, data types, control structures, functions, "
                                              "and modules.\n They will also learn how to work with files, "
                                              "exceptions, and object-oriented programming concepts.\n\nThe course "
                                              "outcomes include:\n*Ability to write basic Python programs using the "
                                              "correct syntax and control structures.\n*Understanding of data types "
                                              "and how to manipulate them in Python.\n*Knowledge of functions and how "
                                              "to define and use them.\n*Ability to work with files and exceptions in "
                                              "Python.\n*Understanding of object-oriented programming concepts and "
                                              "how to implement them in Python.."},
    {"name": "Web Development", "details": "Build web applications using HTML, CSS, and JavaScript\nIn this web "
                                           "development course, students will learn the fundamentals of web "
                                           "development, including HTML, CSS, and JavaScript.\n They will also learn "
                                           "how to create responsive and user-friendly web pages using popular "
                                           "front-end frameworks and libraries like Bootstrap and jQuery.\n\nThe "
                                           "course outcomes include:\n*Ability to create web pages using HTML, "
                                           "including the use of tags, attributes, and elements.\n*Understanding of "
                                           "CSS and how to use it to style web pages, including selectors, "
                                           "properties, and values.\n*Knowledge of JavaScript and how to use it to "
                                           "add interactivity to web pages, including events, functions, "
                                           "and variables.\n*Familiarity with front-end frameworks and libraries like "
                                           "Bootstrap and jQuery, including how to use them to create responsive and "
                                           "user-friendly web pages.\n*Ability to create and manipulate web forms, "
                                           "including form validation and submission using JavaScript\n*Understanding "
                                           "of the basics of web design and user experience, including the principles "
                                           "of visual design and accessibility.\n*Experience working on real-world "
                                           "web development projects and applying the knowledge gained throughout the "
                                           "course."},
    {"name": "Data Science", "details": "Learn data analysis and machine learning using Python\nIn this data "
                                        "analytics course, students will learn the fundamentals of data analysis,"
                                        "\n including data wrangling, data visualization, and statistical analysis.\n "
                                        "They will also learn how to use popular tools and libraries like Pandas, "
                                        "NumPy, and Matplotlib to analyze and visualize data.\n\n*Ability to collect "
                                        "and clean data from various sources, including CSV files and "
                                        "databases.\n*Understanding of exploratory data analysis techniques, "
                                        "including data visualization, descriptive statistics, "
                                        "and data profiling.\n*Knowledge of data manipulation and analysis using "
                                        "Pandas, including filtering, grouping, merging, and transforming "
                                        "data.\n*Ability to perform statistical analysis on data using NumPy, "
                                        "including hypothesis testing and regression analysis.\n*Ability to perform "
                                        "statistical analysis on data using NumPy, including hypothesis testing and "
                                        "regression analysis.\n*Understanding of machine learning concepts and how to "
                                        "use them to make predictions on data.\n*Experience working on real-world "
                                        "data analytics projects and applying the knowledge gained throughout the "
                                        "course."},
    {"name": "Mobile App Development", "details": "Build mobile apps using Java or Kotlin\nIn this Mobile App "
                                                  "Development course, students will learn how to create mobile "
                                                  "applications for Android and iOS platforms using popular "
                                                  "programming languages and \nframeworks like Java, Kotlin, Swift, "
                                                  "and React Native. They will also learn how to design user "
                                                  "interfaces, integrate with APIs, and publish apps to app "
                                                  "stores.\n\nThe course outcomes include:\n*Understanding of mobile "
                                                  "application architecture and design principles, including user "
                                                  "interface design, navigation, and data persistence.\n*Knowledge of "
                                                  "programming languages and frameworks used for mobile app "
                                                  "development, including Java, Kotlin, Swift, and React "
                                                  "Native.\n*Ability to create basic and advanced mobile applications "
                                                  "for Android and iOS platforms using different programming "
                                                  "languages and frameworks.\n*Familiarity with mobile app "
                                                  "development tools and libraries, including Android Studio, Xcode, "
                                                  "and React Native CLI.\n*Understanding of how to integrate mobile "
                                                  "applications with APIs and back-end services, including cloud "
                                                  "services like Firebase and AWS.\n*Experience working on real-world "
                                                  "mobile app development projects and applying the knowledge gained "
                                                  "throughout the course.\n*Ability to publish mobile applications to "
                                                  "app stores and manage app distribution."}
]


class Courses:

    def __init__(self, root):
        frame = tk.Frame(root)
        frame.pack()

        label = tk.Label(frame, text="Courses Page", font=('Arial', '20'))
        label.pack()

        root.geometry('500x300')

        for course in courses:
            course_widget = tk.Frame(frame)
            course_widget.pack(side=tk.TOP, padx=5, pady=5)

            name_label = tk.Label(course_widget, text=course["name"])
            name_label.pack(side=tk.LEFT)

            enrollButton = tk.Button(course_widget, width=10, text="Enroll",
                                     command=lambda name=course["name"]: enroll(course_widget, name))
            enrollButton.pack(padx=10, pady=10, side=tk.LEFT)

            viewDetailsButton = tk.Button(course_widget, width=10, text="View Details",
                                          command=lambda details=course["details"]: view_details(details))
            viewDetailsButton.pack(padx=10, pady=10, side=tk.LEFT)

        def enroll(course_data, course_name):
            print(f"Enrolling in {course_name}...")
            res = enrollCourse(course_name)
            if res['status']:
                messagebox.showinfo(title="Login Status", message=res['message'])
            else:
                messagebox.showinfo(title="Login Status", message="Something went wrong")

        def view_details(details):
            # Open a new window to show course details
            details_window = tk.Toplevel()
            details_window.title('Course Details')
            details_label = tk.Label(details_window, justify="left", text=details)
            details_label.pack()
