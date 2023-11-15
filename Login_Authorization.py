from hashlib import sha256
import csv
import ttkbootstrap as ttk
from  Center_window import center_window

def User_Authorization(window,nic_name,psw):
    """

    :param window:
    :param nic_name:
    :param psw:
    :return:
    """
    #借助相同加密方式将密码进行加密
    password_encrypt = sha256(psw.encode()).hexdigest()

    try:
        with open("User_file.csv",'r',encoding='utf-8') as file:
            reader = csv.reader(file)
            for user_id, user_nickname, user_psw in reader:
                notice_window = ttk.Toplevel(window)
                center_window(notice_window,320,300)
                if nic_name == user_nickname:
                    if password_encrypt == user_psw:
                        notice_window.title("Welcome")
                        message = "You've been successfully logged in!"
                    else:
                        notice_window.title("Ops...")
                        message = "Wrong Password. Please try again."
                else:
                    notice_window.title("Ops...")
                    message = "User information not found. Please try again."

                ttk.Label(notice_window, text=message).grid(row=0, column=0, pady=10, padx=10, sticky='nsew')

                # 添加关闭按钮
                close_button = ttk.Button(notice_window, text="Close", bootstyle="danger", command=notice_window.destroy)
                close_button.grid(row=1, column=0, pady=10)

                notice_window.grid_columnconfigure(0, weight=1)
                notice_window.grid_rowconfigure(0, weight=1)
    except FileNotFoundError:
        notice_window = ttk.Toplevel(window)
        notice_window.title("Ops...")
        center_window(notice_window,320,300)
        ttk.Label(notice_window, text="    No one has signed up yet!").grid(row=0, column=0, pady=10, padx=10, sticky='nsew')


