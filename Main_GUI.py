import ttkbootstrap as ttk
from ttkbootstrap.constants import *  # 导入常量，例如 LEFT, RIGHT 等
from open_signup import open_signup_window

# 创建窗口，使用 ttkbootstrap 的风格
window = ttk.Window(themename='flatly')  # 可以选择不同的主题
window.title("Our Social Club")
window.geometry("1536x900")

# 创建一个自定义样式
style = ttk.Style()
style.configure('Custom.TLabel', font=('Bradley Hand ITC', 18))
style.configure('Custom.TButton', font=('Helvetica', 12))

# 主题标签
theme_label = ttk.Label(window, text="Welcome to Our Social Club!", style='Custom.TLabel')
theme_label.pack(pady=20)

# 创建 Sign In 按钮
sign_in_button = ttk.Button(window, text="Sign In", bootstyle=PRIMARY, style='Custom.TButton')
sign_in_button.pack(pady=10)

# 创建 Sign Up 部分
signup_frame = ttk.Frame(window)  # 使用 Frame 来组织内容
signup_label = ttk.Label(signup_frame, text="Don't have an account yet?", font=("Helvetica", 12))
signup_label.pack(side=LEFT, padx=5)  # padx 是水平方向的内边距
sign_up_button = ttk.Button(signup_frame, text="Sign Up", bootstyle=SUCCESS, style='Custom.TButton', command=lambda: open_signup_window(window))
sign_up_button.pack(side=LEFT)

# 将 Sign Up 部分放置到窗口中
signup_frame.pack(pady=10)

# 运行 GUI 主循环
window.mainloop()
