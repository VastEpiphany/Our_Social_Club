import ttkbootstrap as ttk
import tkinter as tk
from Center_window import center_window
import csv

class DeleteFriend_Window:

    def __init__(self,window,this_user):
        self.file = "user_friend.csv"
        self.window = ttk.Toplevel(window)
        self.myname = this_user.nickname

        self.window.title("Delete Friends")
        center_window(self.window,800,600)

        #第一行文本所在位置
        text1 = ttk.Label(self.window,text="Enter the name of the friend that you want to delete:")
        text1.place(x=200,y=30)

        #第一行Entry输入框所在位置
        entry = ttk.Entry(self.window,show=None)
        entry.place(x=200,y=80)

        #第一行提交Button按钮所在位置以及所指向函数
        button = ttk.Button(self.window,text="Confirm",command=lambda:self.show_notification_and_delete(entry.get()))
        button.place(x=500,y=80)

    def delete_friend(self, d_nickname):
        flag = True
        try:
            #首先读取文档并且将所有与删除无关的内容全部复制
            with open(self.file, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                rest_list = [row for row in reader if row[1] != d_nickname or row[0] != self.myname]

            #其次再次以w模式读取文档，覆盖文档并重新写入数据
            with open(self.file, "w", newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(rest_list)

        except FileNotFoundError:
            tk.messagebox.showerror("Error", "File not found.")
            flag = False
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {e}")
            flag = False

        if flag:
            tk.messagebox.showinfo("Success", f"Friend '{d_nickname}' deleted successfully!")

    def show_notification_and_delete(self,d_nickname):
        if tk.messagebox.askyesno(title="Affirm?",message="Are you sure to delete this friend? This process cannot be reversed!"):
            self.delete_friend(d_nickname)
        else:
            pass



