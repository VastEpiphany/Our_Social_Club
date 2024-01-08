import tkinter as tk
import ttkbootstrap as ttk
import csv

class StudentBlackBoard:
    def __init__(self, frame):
        self.frame = frame
        self.messages_file = "BBmessages.csv"
        self.messages_text = ttk.Text(frame, height=10, width=50)
        self.messages_text.pack()
        self.load_messages()

        # 输入框和提交按钮
        self.input_text = ttk.Entry(frame, width=50)
        self.input_text.pack()
        self.submit_button = ttk.Button(frame, text="Submit Messages", command=self.add_message)
        self.submit_button.pack()

    def add_message(self):
        message = self.input_text.get()
        if message:
            # 将留言添加到 Text 小部件
            self.messages_text.insert(ttk.END, message + "\n")
            # 清空输入框
            self.input_text.delete(0, ttk.END)
            # 保存留言到 CSV 文件
            self.save_message(message)

    def save_message(self, message):
        with open(self.messages_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([message])

    def load_messages(self):
        try:
            with open(self.messages_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.messages_text.insert(ttk.END, row[0] + "\n")
        except FileNotFoundError:
            pass  # 文件不存在时暂时不做任何操作