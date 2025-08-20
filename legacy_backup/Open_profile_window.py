import ttkbootstrap as ttk
from tkinter import messagebox
from Center_window import center_window
from Main_User_Class import Main_User

def on_save_button_clicked(main_user, age_entry, hobbies_entry, birthday_entry, sign_entry):
    """
    当保存按钮被点击时调用此函数
    :param main_user: Main_User 类的实例
    :param age_entry: 年龄输入框
    :param hobbies_entry: 兴趣输入框
    :param birthday_entry: 生日输入框
    :param sign_entry: 个性签名输入框
    """
    # 更新 main_user 对象的信息
    main_user.age = age_entry.get()
    main_user.hobbies = hobbies_entry.get()
    main_user.birthday = birthday_entry.entry.get()
    main_user.sign = sign_entry.get()

    # 保存信息到CSV文件
    main_user.save_to_csv("User_info.csv")
def open_profile_setting_window(front_window,main_user):
    # 设置初始弹出窗口
    window = ttk.Toplevel(front_window)
    window.title("Profile Settings")
    center_window(window, 600, 400)
    # 设置label
    label1 = ttk.Label(window, text="Profile Settings:", font=('Bradley Hand ITC', 18), background='white')
    label1.pack(side="top", anchor='nw')

    # 年龄标签
    age_label = ttk.Label(window, text="Age：", font=('Britannic Bold', 12), background='white')
    age_label.place(x=150,y=100)
    #年龄entry框
    age_entry = ttk.Entry(window,bootstyle='success')
    age_entry.place(x=250,y=100)

    # 兴趣标签
    hobbies_label = ttk.Label(window, text="Hobbies：", font=('Britannic Bold', 12), background='white')
    hobbies_label.place(x=150, y=140)
    # 兴趣entry框
    hobbies_entry = ttk.Entry(window, bootstyle='success')
    hobbies_entry.place(x=250, y=140)

    # 生日标签
    birthday_label = ttk.Label(window, text="birthday：", font=('Britannic Bold', 12), background='white')
    birthday_label.place(x=150, y=180)
    # (特殊 比较有意思)生日Date entry框
    birthday_entry = ttk.DateEntry(window, bootstyle='success')
    birthday_entry.place(x=250,y=180)

    # 个性签名标签
    sign_label = ttk.Label(window, text="Signature：", font=('Britannic Bold', 12), background='white')
    sign_label.place(x=150, y=220)
    # 个性签名entry框
    sign_entry = ttk.Entry(window, bootstyle='success')
    sign_entry.place(x=250, y=220)


    #Save保存按钮
    '''save_button = ttk.Button(window,text="Save",command=
    lambda: [main_user.update_info(age_entry.get(),hobbies_entry.get(),birthday_entry.entry.get(),sign_entry.get()),messagebox.showinfo(title="Success",message="Profile saved."),window.destroy()])'''
    save_button = ttk.Button(window, text='Save', command=lambda: [
        on_save_button_clicked(main_user, age_entry, hobbies_entry, birthday_entry, sign_entry),
        messagebox.showinfo(title="Success", message="Profile saved."), window.destroy()])
    save_button.place(x=490,y=350)



def open_profile_window(front_window,main_user):
    #设置初始弹出窗口
    window = ttk.Toplevel(front_window)
    window.title("My Profile")
    center_window(window,800,600)

    #设置label   注：对于ttk的label函数而言font background函数仍然起作用，故可以美化！
    label1 = ttk.Label(window,text="My Own Profile:",font=('Bradley Hand ITC',18),background='white')
    label1.pack(side="top",anchor='nw')

    #名称标签
    name_label1 = ttk.Label(window,text="My nickname:",font=('Britannic Bold',12),background='white')
    name_label1.place(x=400,y=70)
    #名称具体内容（从main_user对象中获取）
    name = main_user.nickname
    name_label2 = ttk.Label(window,text=name,font=('Arial',12),background='white')
    name_label2.place(x=550,y=70)

    #年龄标签
    age_label1 =ttk.Label(window,text="My age：",font=('Britannic Bold',12),background='white')
    age_label1.place(x=400,y=100)
    #年龄具体内容（从main_user对象中获取）
    age = main_user.age
    age_label2 =  ttk.Label(window,text=age,font=('Arial',12),background='white')
    age_label2.place(x=550,y=100)

    # 兴趣标签
    hobbies_label1 = ttk.Label(window, text="My hobbies：", font=('Britannic Bold', 12), background='white')
    hobbies_label1.place(x=400, y=130)
    # 兴趣具体内容（从main_user对象中获取）
    hobbies = main_user.hobbies
    hobbies_label2 = ttk.Label(window, text=hobbies, font=('Arial', 12), background='white')
    hobbies_label2.place(x=550, y=130)

    # 生日标签
    birthday_label1 = ttk.Label(window, text="My birthday：", font=('Britannic Bold', 12), background='white')
    birthday_label1.place(x=400, y=160)
    # 生日具体内容（从main_user对象中获取）
    birthday = main_user.birthday
    birthday_label2 = ttk.Label(window, text=birthday, font=('Arial', 12), background='white')
    birthday_label2.place(x=550, y=160)

    # 个性签名标签
    sign_label1 = ttk.Label(window, text="My signature：", font=('Britannic Bold', 12), background='white')
    sign_label1.place(x=400, y=190)
    # 个性签名具体内容（从main_user对象中获取）
    sign = main_user.sign
    sign_label2 = ttk.Label(window, text=sign, font=('Arial', 12), background='white')
    sign_label2.place(x=550, y=190)

    #修改个人信息(label加button)
    change_label = ttk.Label(window,text="Still a blank face? Now show yourself!",font=('Eras Light ITC',12),background='white')
    change_label.place(x=100,y=500)
    change_button = ttk.Button(window,text="Change Profile",bootstyle="danger",command=lambda:open_profile_setting_window(window,main_user))
    change_button.place(x=550,y=500)