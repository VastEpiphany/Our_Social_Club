import ttkbootstrap as ttk
from ttkbootstrap.constants import *  # 导入常量
from tkinter import PhotoImage
from User import User

def center_window(win, width, height):
    """
    该函数用于计算并设置窗口中心位置，需要与tkinter或ttk共同配合使用
    :param win: window窗口，即为tkinter的root操作对象
    :param width: 目标设置宽度
    :param height: 目标设置高度
    :return: 无需返回，函数直接操作设置
    """
    # 获取屏幕尺寸
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # 计算 x, y 位置
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)

    # 设置窗口位置
    win.geometry(f'{width}x{height}+{x}+{y}')


def confirm_psw(signup_window, nickname_entry, password_entry, password_rentry):
    """

    :param signup_window: 当前注册界面弹出窗口
    :param nickname_entry: 昵称输入框
    :param password_entry: 密码输入框
    :param password_rentry: 密码二次确认输入框
    :return:
    """
    nic_name = nickname_entry.get()
    psw_1 = password_entry.get()
    psw_2 = password_rentry.get()

    confirm_window = ttk.Toplevel(signup_window)
    confirm_window.grid_columnconfigure(0, weight=1)  # 使列能够扩展，以便居中


    if psw_1 == psw_2:
        confirm_window.title("Congratulations")
        center_window(confirm_window, 310, 300)
        message = f"Let's welcome {nic_name} for joining our club!"
        user = User(nic_name,psw_1)
        user.save_to_csv("User_file.csv")
    else:
        confirm_window.title("Hmm... Something is wrong")
        center_window(confirm_window, 310, 300)
        message = "Come on! Re-enter your password\nsince you don't want to forget, do you?"

    ttk.Label(confirm_window, text=message).grid(row=0, column=0, pady=10, padx=10, sticky='nsew')

    # 添加关闭按钮
    close_button = ttk.Button(confirm_window, text="Close", bootstyle="danger", command=confirm_window.destroy)
    close_button.grid(row=1, column=0, pady=10)

    confirm_window.grid_columnconfigure(0, weight=1)  # 配置网格布局，以便内容居中
    confirm_window.grid_rowconfigure(0, weight=1)    # 配置网格布局，使标签和按钮在垂直方向上居中

def open_signup_window(window):
    # 新界面基本内容确定
    signup_window = ttk.Toplevel(window)
    signup_window.title("Sign Up")

    # 设置窗口大小和位置
    center_window(signup_window, 700, 500)

    # 使用 grid 布局下的各个组件具体实现
    ttk.Label(signup_window, text="Freshman? Just give us your details to let us know!", font=("Helvetica", 13)).grid(row=0, column=0, columnspan=2, pady=10, padx=10)

    ttk.Label(signup_window, text="Nickname:").grid(row=1, column=0, pady=5, sticky='e')
    nickname_entry = ttk.Entry(signup_window)
    nickname_entry.grid(row=1, column=1, pady=5, padx=5, sticky='ew')

    ttk.Label(signup_window, text="Password:").grid(row=2, column=0, pady=5, sticky='e')
    password_entry = ttk.Entry(signup_window, show='*')
    password_entry.grid(row=2, column=1, pady=5, padx=5, sticky='ew')

    ttk.Label(signup_window, text="Confirm your Password:").grid(row=3, column=0, pady=5, sticky='e')
    password_rentry = ttk.Entry(signup_window, show='*')
    password_rentry.grid(row=3, column=1, pady=5, padx=5, sticky='ew')

    ttk.Button(signup_window, text="Submit", bootstyle="success-outline", command=lambda: confirm_psw(signup_window, nickname_entry, password_entry, password_rentry)).grid(row=5, column=0, columnspan=2, pady=10)

    # 调整列的权重以使其可扩展
    signup_window.grid_columnconfigure(1, weight=1)

    # 设置 Entry 控件的焦点
    nickname_entry.focus()

