from hashlib import sha256
import time
import csv
import ttkbootstrap as ttk
import tkinter.messagebox
from  Center_window import center_window
from Main_Window_GUI import main


def create_notice_window(window, title, message):
    """

    :param window: 父窗口
    :param title: 所需要设置的窗口标题名称
    :param message: 所需要传递的信息
    :return:
    """
    notice_window = ttk.Toplevel(window)
    center_window(notice_window, 320, 300)
    notice_window.title(title)
    ttk.Label(notice_window, text=message).grid(row=0, column=0, pady=10, padx=10, sticky='nsew')
    close_button = ttk.Button(notice_window, text="Close", bootstyle="danger", command=notice_window.destroy)
    close_button.grid(row=1, column=0, pady=10)


def handle_login(window,nic_name,psw):
    """

    :param window: 父窗口
    :param nic_name: 传入的用户昵称
    :param psw: 传入的用户密码
    :return:  也不能叫return，若登陆成功则选择运行main函数用户主功能界面
    """
    if User_Authorization(window, nic_name, psw):
        with open("User_file.csv", 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for user_id, user_nickname, user_psw in reader:
                if nic_name == user_nickname:
                    us_id = user_id
        ## 登录成功，延迟关闭当前窗口，然后打开新窗口
        window.after(1000, lambda:[main(nic_name,us_id),window.destroy()])  # 延迟 2 秒关闭窗口


def User_Authorization(window, nic_name, psw)->bool:
    password_encrypt = sha256(psw.encode()).hexdigest()
    try:
        with open("User_file.csv", 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for user_id, user_nickname, user_psw in reader:
                if nic_name == user_nickname:
                    if password_encrypt == user_psw:
                        # 登录成功
                        tkinter.messagebox.showinfo(title="Welcome",message="You've successfully logged in!")

                        #create_notice_window(window,"Welcome","You've successfully logged in!")
                        return True
                    else:
                        # 密码错误
                        create_notice_window(window, "Ops...", "Wrong Password. Please try again.")
                        return False

            # 用户名未找到
            create_notice_window(window, "Ops...", "User information not found. Please try again.")
            return False

    except FileNotFoundError:
        # 文件未找到
        create_notice_window(window, "Ops...", "No one has signed up yet!")
        return False


