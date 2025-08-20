import tkinter
import ttkbootstrap as ttk
from Center_window import center_window
from hashlib import sha256
import csv


class Find_Psw_Window:
    def __init__(self,window):
        """

        :param window: 父窗口
        """
        self.file = "User_SecurityQuestion.csv"
        self.window = ttk.Toplevel(window)
        center_window(self.window,800,600)
        self.window.title("Find Your Password")

        label1 = ttk.Label(self.window,text="Enter your nickname of your account to continue:")
        label1.place(x=100,y=30)

        entry1 = ttk.Entry(self.window)
        entry1.place(x=500,y=30)

        button1 = ttk.Button(self.window,text="Submit",command=lambda:self.init_determine(entry1.get()))
        button1.place(x=600,y=100)


    def init_determine(self,name):
        """

        :param name:用户nickname的entry框中输入的内容
        :return:
        """
        #如果不是什么都没输入就点了Submit
        if name != "":
            self.after_det_then_next_question(name)
        else:
            tkinter.messagebox.showerror("Error","Please enter a valid nickname!")

    def after_det_then_next_question(self, name):
        result = self.read_file(name)
        if result == 1:    # 用户昵称未找到的情况
            tkinter.messagebox.showerror("Name Error", "The Nickname you enter isn't found!")
        elif result == 2:  # 存储文件未找到的情况
            tkinter.messagebox.showerror("File Not Found Error", "Are you kidding? Even the file isn't found!")
        else:
            category, message = result
            # 更新当前窗口的内容而不是销毁并重建
            self.update_window_for_question(name,category,message)

    def update_window_for_question(self, name,category,message):
        """

        :param name: 用户nickname昵称
        :param category: 用户密保问题类型
        :param message: 用户具体密保答案
        :return:
        """
        # 清空窗口中的所有组件
        for widget in self.window.winfo_children():
            widget.destroy()

        # 添加新的组件
        label1 = ttk.Label(self.window, text=f"Enter the {category} information concerning your account:")
        label1.place(x=200, y=30)
        entry1 = ttk.Entry(self.window, show=None)
        entry1.place(x=200, y=100)

        button1 = ttk.Button(self.window,text="Submit",command=lambda:self.handle_final(name,message,entry1.get()))
        button1.place(x=500,y=100)

    def handle_final(self,name,message,my_m):
        """

        :param name: 用户nickname昵称
        :param message: 用户密保答案
        :param my_m: 用户自己输入的密保答案
        :return:
        """
        if message == my_m:
            # 清空窗口中的所有组件
            for widget in self.window.winfo_children():
                widget.destroy()
            label1 = ttk.Label(self.window,text="Your answer is correct! Now you can set the new password for your account:")
            label1.place(x=100,y=30)

            label2 = ttk.Label(self.window,text="Enter your new password:")
            label2.place(x=200,y=100)

            entry1 = ttk.Entry(self.window,show="*")
            entry1.place(x=450,y=100)

            label3 = ttk.Label(self.window,text="Confirm your password again:")
            label3.place(x=200,y=200)

            entry2 = ttk.Entry(self.window,show="*")
            entry2.place(x=450,y=200)

            button = ttk.Button(self.window,text="Submit",command=lambda:self.validate_password_and_handle(name,entry1.get(),entry2.get()))
            button.place(x=400,y=300)



        else:
            tkinter.messagebox.showerror("Error","The message isn't correct. Please try again!")

    def validate_password_and_handle(self, name,v1, v2):
        """

        :param name: 用户nickname昵称
        :param v1: 用户重置密码第一次输入
        :param v2: 用户重置密码第二次输入
        :return:
        """
        if v1 == v2:
            # 处理密码匹配逻辑
            tkinter.messagebox.showinfo("Success", "Password has been reset successfully!")
            # 这里添加重设密码的逻辑
            self.change_psw_file(name,v2)
        else:
            tkinter.messagebox.showerror("Error", "The passwords you entered do not match. Please try again.")

    def change_psw_file(self, name, psw):
        password_encrypt = sha256(psw.encode()).hexdigest()
        try:
            # 读取现有的用户数据
            users = []
            with open("User_file.csv", "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for user_id, user_nickname, user_psw in reader:
                    if user_nickname == name:
                        # 更新匹配用户的密码
                        users.append([user_id, user_nickname, password_encrypt])
                    else:
                        users.append([user_id, user_nickname, user_psw])

            # 将更新后的数据写回文件
            with open("User_file.csv", "w", newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(users)

            # 密码更新成功的提醒
            tkinter.messagebox.showinfo("Success", "Password has been updated successfully.")

        except FileNotFoundError:
            tkinter.messagebox.showerror("File Error", "User file not found.")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"An error occurred: {e}")

    def read_file(self, name):
        try:
            with open(self.file, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == name:
                        return row[1], row[2]  # 返回category和message
                return 1  # 用户名未找到
        except FileNotFoundError:
            return 2