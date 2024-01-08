import tkinter as tk
import csv
from Center_window import center_window
from tkinter import scrolledtext, messagebox, Toplevel

class OpinionBox:
    def __init__(self, master):
        self.master = master
        self.file = 'User_opinions.csv'
        self.bad_words = {
            "fucking", "shit",  # 实际的脏话或不当词汇
            "damn", "hell",  # 示例
            # ... 更多的脏话或不当词汇 ...
        }
        self.create_opinion_box()

    def create_opinion_box(self):
        self.opinion_box = Toplevel(self.master)  # 创建一个顶级窗口
        self.opinion_box.title("Opinion box")
        center_window(self.opinion_box,800,600)

        #创建一个文字提示Label并且布局
        self.label1 = tk.Label(self.opinion_box,text="Enter your opinions here in this entry:")
        self.label1.place(x=100,y=20)

        # 创建并放置文本输入框
        self.opinion_text = scrolledtext.ScrolledText(self.opinion_box, wrap=tk.WORD, height=10, width=50)
        self.opinion_text.place(x=200,y=50)

        # 创建并放置提交按钮
        submit_button = tk.Button(self.opinion_box, text="Submit comments", command=self.submit_opinion)
        submit_button.place(x=400,y=350)

        # 创建并放置查看意见按钮
        view_button = tk.Button(self.opinion_box, text="View the comments submitted", command=self.view_opinions)
        view_button.place(x=400,y=400)

    def submit_opinion(self):
        opinion = self.opinion_text.get("1.0", tk.END).strip()
        if opinion:
            if self.contains_bad_word(opinion):
                messagebox.showwarning("Commit failure", "Your comment contains inappropriate language. Please revise it.")
                return

            with open(self.file, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([opinion])  # 使用 CSV 格式写入
            self.opinion_text.delete("1.0", tk.END)
            messagebox.showinfo("Submit successfully", "Your comments have been submitted. Thank you!")
        else:
            messagebox.showwarning("Commit failure", "Comments cannot be empty.")

    def view_opinions(self):
        try:
            with open(self.file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                opinions = "\n\n".join(row[0] for row in reader)  # 读取 CSV 文件并合并意见

            opinion_display_window = Toplevel()
            opinion_display_window.title("Comments have been submitted")
            opinion_display = scrolledtext.ScrolledText(opinion_display_window, wrap=tk.WORD, height=10, width=50)
            opinion_display.pack()
            opinion_display.insert(tk.END, opinions)
        except FileNotFoundError:
            messagebox.showwarning("warning", "There are currently no submissions.")

    def contains_bad_word(self, text):
        words = set(word.lower() for word in text.split())
        return any(bad_word in words for bad_word in self.bad_words)

