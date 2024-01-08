import ttkbootstrap as ttk
from Center_window import center_window
from Main_User_Class import Main_User
from Load_User import  Load_User
from Open_profile_window import open_profile_window
from Open_Addfriend_window import AddFriend_Window
from Open_Deletefriend_Window import DeleteFriend_Window
from Open_Showfriend_Window import ShowFriend_Window
from Reward_Task_board_class import RewardTaskBoard
from PersonalizationSettings_class import PersonalizationSettings
from Open_OpinionBox_Window import OpinionBox
from Open_RecruitmentMessage_Window import JobPosting
from Open_FileSharing_Window import FileSharingApp
from Open_SQ_main_Window import Main_SQ_Config
from Open_ChangePsw_Main_Window import Main_ChangePsw
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

    # Settings菜单下的第一个功能 - 退出
    setting_menu.add_command(label="Exit", command=lambda: window.quit())

    # Settings菜单下的第二个功能 - 个性化设置
    setting_menu.add_command(label="Personalization", command=lambda: PersonalizationSettings(window))

    # 创建一个Security菜单选项
    security_menu = ttk.Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Security", menu=security_menu)  # 正确地将security_menu添加为main_menu的一个子菜单

    # Security菜单下的第一个功能 - 修改密保设置
    security_menu.add_command(label="Se-Question Change", command=lambda: Main_SQ_Config(window, this_user.nickname))

    # Security菜单下的第二个功能 - 修改用户密码功能
    security_menu.add_command(label="Password Change",command=lambda:Main_ChangePsw(window,this_user))

    # 按钮frame窗口
    button_frame = ttk.Frame(window, padding=10)

    #创建my profile按钮并且执行相关操作
    button_frame.pack(expand=False, side='left', padx=100)
    my_profile_button = ttk.Button(button_frame, text="My Profile",command=lambda: open_profile_window(window,this_user))
    my_profile_button.grid(row=0, column=0, padx=5)

    #创建add friend按钮并且执行相关操作
    add_friend_button = ttk.Button(button_frame,text="Add Friend",command=lambda:AddFriend_Window(window,this_user))
    add_friend_button.grid(row=5,column=0,padx=5)

    #创建delete friend按钮并且执行相关操作
    delete_friend_button = ttk.Button(button_frame,text="Delete Friend",command=lambda:DeleteFriend_Window(window,this_user))
    delete_friend_button.grid(row=6,column=0,padx=5)

    #创建show friend按钮并且执行相关操作
    show_friend_button = ttk.Button(button_frame,text="Show Friend",command=lambda:ShowFriend_Window(window,this_user))
    show_friend_button.grid(row=7,column=0,padx=5)

    #创建Reward Task Board按钮并且执行相关操作
    reward_task_board_button = ttk.Button(button_frame,text="Reward Task Board",command= lambda:RewardTaskBoard(window))
    reward_task_board_button.grid(row=8,column=0,padx=5)

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


    # 添加OpinionBox意见箱功能块
    OpinionBox_frame = ttk.Frame(window, padding=10)
    OpinionBox_frame.place(x=750, y=800)  # 使用 place 布局管理器

    OpinionBox_label = ttk.Label(OpinionBox_frame, text="Wanna give us some opinions?")
    OpinionBox_label.grid(row=0, column=0, padx=5)  # 使用 grid 布局管理器

    OpinionBox_button = ttk.Button(OpinionBox_frame, bootstyle="info-link", text="Click Me!",
                               command=lambda: OpinionBox(window))
    OpinionBox_button.grid(row=0, column=1, padx=20)  # 使用 grid 布局管理器

    #添加学校岗位招聘信息Window功能区
    Recruitment_frame = ttk.Frame(window,bootstyle = "primary",padding=10)
    Recruitment_frame.place(x=100,y=800)

    Recruitment_label = ttk.Label(Recruitment_frame,text="Recruitment message is here:")
    Recruitment_label.grid(row=0,column=0,padx=20)

    Recruitment_button = ttk.Button(Recruitment_frame,text="Discover Something!",command=lambda:JobPosting(window))
    Recruitment_button.grid(row=0,column=1,padx=20)

    #添加文件资源共享站功能区
    FileSharing_frame = ttk.Frame(window,padding=10)
    FileSharing_frame.place(x=100,y=600)

    FileSharing_label = ttk.Label(FileSharing_frame,text="Here's the File Sharing Base:")
    FileSharing_label.grid(row=0,column=0,padx=10)

    FileSharing_button = ttk.Button(FileSharing_frame,text="Enter",command=lambda:FileSharingApp(window))
    FileSharing_button.grid(row=0,column=1,padx=20)



    window.mainloop()