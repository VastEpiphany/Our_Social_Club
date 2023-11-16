import ttkbootstrap as ttk
from ttkbootstrap.constants import *  # 导入常量，例如 LEFT, RIGHT 等
from open_signup import open_signup_window,center_window
from Login_Authorization import User_Authorization,handle_login
from Center_window import center_window



# 创建窗口，使用 ttkbootstrap 的风格
window = ttk.Window(themename='flatly')  # 可以选择不同的主题
window.title("Our Social Club")
center_window(window,1300,900)

# 创建一个自定义样式 目前测试不一定有效
style = ttk.Style()
style.configure('Custom.TLabel', font=('Bradley Hand ITC', 20)) #本行代码实测有效，能够将标题成功更改
style.configure('Custom.TButton', font=('Helvetica', 12))

# 主题标签
theme_label = ttk.Label(window, text="                  Our Social Club\nThe Final Frontier for meeting others", style='Custom.TLabel')
theme_label.grid(row=0,column=0,pady=20,columnspan=3)

# 创建 与Sign In 有关的entry对话框和按钮
sign_in_label1 = ttk.Label(window,text="User Name:")
sign_in_label1.grid(row=1,column=0,padx=10,sticky='e')

sign_in_label1_entry = ttk.Entry(window,style='success')
sign_in_label1_entry.grid(row=1,column=1,padx=10,sticky='ew')

sign_in_label2 = ttk.Label(window,text="Password:")
sign_in_label2.grid(row=2,column=0,padx=10,sticky='e')

sign_in_label2_entry = ttk.Entry(window,show="*",style='success')
sign_in_label2_entry.grid(row=2,column=1,padx=10,sticky='ew')

sign_in_button = ttk.Button(window, text="Sign In", bootstyle='info',command=lambda:handle_login(window,sign_in_label1_entry.get(),sign_in_label2_entry.get())) #sign in 登录按钮，需要在此按钮上加入Action来验证
sign_in_button.grid(row=3,column=2,padx=10)

# 创建 Sign Up 部分  CAUTION：受限于编程进度，目前用户注册的昵称必须是唯一的
signup_frame = ttk.Frame(window)  # 使用 Frame 来组织内容
signup_frame.grid(row=4,column=0,columnspan=3,pady=10,sticky='ew')

signup_label = ttk.Label(signup_frame, text="Don't have an account yet?", font=("Helvetica", 12))
signup_label.pack(padx=5)  # padx 是水平方向的内边距

sign_up_button = ttk.Button(signup_frame, text="Sign Up", bootstyle=SUCCESS, style='Custom.TButton', command=lambda: open_signup_window(window))
sign_up_button.pack()

# 调整网格列的权重
window.grid_columnconfigure(1, weight=1)

# 运行 GUI 主循环
window.mainloop()
