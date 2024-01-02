import ttkbootstrap as ttk
from Center_window import center_window
from Main_User_Class import Main_User
from Load_User import  Load_User
from Open_profile_window import open_profile_window
from Student_BlackBoard import StudentBlackBoard

def main(nicname,uid):
#用户个人信息载入
    this_user = Load_User(nicname,uid)
#用户个人主界面显示初始化
    window = ttk.Window(themename='journal')
    window.title("Our Social Club")
    center_window(window, 1300, 900)

# 创建一个主菜单栏
    main_menu = ttk.Menu(window)
    window.config(menu=main_menu)
    # 创建一个Settings菜单选项
    setting_menu = ttk.Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Settings", menu=setting_menu)
    setting_menu.add_command(label="Exit", command=lambda: window.quit())

    # 按钮frame窗口
    button_frame = ttk.Frame(window, padding=10)

    button_frame.pack(expand=False, side='left', padx=100)
    my_profile_button = ttk.Button(button_frame, text="My Profile",command=lambda: open_profile_window(window,this_user))
    my_profile_button.grid(row=0, column=0, padx=5)

    # 创建一个 Frame 作为 blackboard
    blackboard_frame = ttk.Frame(window,style='secondary', padding=10)

    # 使用 pack 来定位 Frame
    # 这里将 Frame 放置在窗口的中间，使其水平居中
    blackboard_frame.pack(expand=True, padx=100, pady=50)

    # 在 blackboard_frame 中添加一些小部件来显示信息
    blackboard = StudentBlackBoard(blackboard_frame)
    # 例如，使用 Text 小部件来显示留言
    #messages_text = ttk.Text(blackboard_frame, height=10, width=50)
    #messages_text.pack()

    # 添加更多的小部件，如需要


    window.mainloop()