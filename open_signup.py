import ttkbootstrap as ttk
from ttkbootstrap.constants import *  # 导入常量

def open_signup_window(window):
    # 创建一个自定义样式
    style = ttk.Style()
    style.configure('Custom.TButton', font=('Helvetica', 12))

    # 新界面基本内容确定
    signup_window = ttk.Toplevel(window)
    signup_window.title("Sign Up")

    ttk.Label(signup_window, text="Freshman? Just give us your details to let us know!", font=("Helvetica", 14)).pack(pady=10)
    ttk.Entry(signup_window).pack()
    ttk.Button(signup_window, text="Submit", bootstyle=PRIMARY, style='Custom.TButton').pack(pady=10)
