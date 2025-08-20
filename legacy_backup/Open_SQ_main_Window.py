import tkinter
import ttkbootstrap as ttk
from Open_SecurityQ_Window import SecurityQuestion_Config
from Center_window import center_window
import csv

class Main_SQ_Config(SecurityQuestion_Config):
    def __init__(self, window, nickname):
        self.file = "User_SecurityQuestion.csv"
        self.nickname = nickname
        self.window = ttk.Toplevel(window)

        center_window(self.window, 800, 400)
        self.window.title("Security Question Config")

        # 标题label选择
        label1 = ttk.Label(self.window, text="Choose a category as your security question:")
        label1.place(x=200, y=30)

        # 使用 ttk 库中的 RadioButton 选项以作出问题选择
        c1 = ttk.Radiobutton(self.window, text="Your Birthday", command=self.c1_operation)
        c1.place(x=300, y=80)

        c2 = ttk.Radiobutton(self.window, text="Your Hometown", command=self.c2_operation)
        c2.place(x=300, y=120)

        c3 = ttk.Radiobutton(self.window, text="Your School", command=self.c3_operation)
        c3.place(x=300, y=160)

        label2 = ttk.Label(self.window, text="Notice that we only allow you to set one unique category\nof the security question for the sake of your safety!", bootstyle="danger")
        label2.place(x=150, y=200)

    def c1_operation(self):
        self.create_question_window("Birthday", "Enter your birthday:")

    def c2_operation(self):
        self.create_question_window("Hometown", "Enter your hometown:")

    def c3_operation(self):
        self.create_question_window("School", "Enter your school:")

    def create_question_window(self, category, question):
        question_window = ttk.Toplevel(self.window)
        center_window(question_window, 520, 300)
        question_window.title(f"{category} Question")

        label = ttk.Label(question_window, text=question)
        label.place(x=80, y=70)

        answer_entry = ttk.Entry(question_window, show=None)
        answer_entry.place(x=270, y=70)

        button = ttk.Button(question_window, text="Submit", bootstyle="dark",
                            command=lambda: self.handle_and_save(self.nickname, category, answer_entry.get()))
        button.place(x=200, y=200)

    def handle_and_save(self, name, category, message):
        if not message:
            tkinter.messagebox.showerror("Error", "Answer cannot be empty.")
            return

        try:
            with open(self.file, "a", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([name, category, message])
            tkinter.messagebox.showinfo("Success", "Security question set successfully.")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"An error occurred: {e}")

