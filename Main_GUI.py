import tkinter as tk
from open_signup import open_signup_window

#创建窗口
window = tk.Tk()
#设置窗口标题
window.title("Our Social Club")
#设置窗口默认大小
window.geometry("1024x768")


#主题标签
theme_label = tk.Label(window,text="Welcome to Our Social Club!",font=("Bradley Hand ITC",18))
theme_label.pack(pady=20)

# 创建 Sign In 按钮
sign_in_button = tk.Button(window, text="Sign In", font=("Helvetica", 12))
sign_in_button.pack(pady=10)

# 创建 Sign Up 部分
signup_frame = tk.Frame(window)  # 使用 Frame 来组织内容
signup_label = tk.Label(signup_frame, text="Don't have an account yet?", font=("Helvetica", 12))
signup_label.pack(side=tk.LEFT, padx=5)  # padx 是水平方向的内边距
sign_up_button = tk.Button(signup_frame, text="Sign Up", font=("Helvetica", 12),command=lambda:open_signup_window(window))
#说明：sign_up在被点击后将运行sign_up函数弹出新窗口，不能直接将函数open_signup_window(window)传给command否则将直接运行，正确的是借助lambda 创建了一个匿名函数，它在被调用时执行 open_signup_window(window)
sign_up_button.pack(side=tk.LEFT)

# 将 Sign Up 部分放置到窗口中
signup_frame.pack(pady=10)


#运行GUI主循环
window.mainloop()