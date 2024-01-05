import ttkbootstrap as ttk
import tkinter as tk
from Center_window import center_window
import csv


class ShowFriend_Window:

    def __init__(self, window, this_user):
        self.file = "user_friend.csv"
        self.window = ttk.Toplevel(window)
        self.myname = this_user.nickname

        self.window.title("Show Friends")
        center_window(self.window, 800, 600)

        # 第一行文本所在位置
        text1 = ttk.Label(self.window, text="Below are all your friends:")
        text1.place(x=200, y=30)

        # 调用 show_friends 方法并获取好友列表
        friends = self.show_friends()

        # 创建一个文本框来显示好友列表
        text_box = tk.Text(self.window, height=15, width=50)
        text_box.place(x=200, y=60)

        #第二行文本所在位置
        text2 = ttk.Label(self.window,text="We'll take a cup of kindeness yet,\nfor days of auld lang syne!",font=('Bradley Hand ITC', 10))
        text2.place(x=200,y=500)


        # 将好友列表添加到文本框
        for friend in friends:
            text_box.insert(tk.END, friend + '\n')

    def show_friends(self):
        friends = []
        try:
            with open(self.file, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == self.myname:
                        friends.append(row[1])
            return friends
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "Friend list file not found.")
            return []
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {e}")
            return []




