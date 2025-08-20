"""
Our Social Club - 兼容性主程序
这个文件可以直接替换原来的Main_Login_GUI.py，保持所有功能正常运行
同时提供了更好的代码组织
"""
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import csv
import uuid
from hashlib import sha256
import os


class Config:
    """配置类"""
    DEFAULT_THEME = 'flatly'
    MAIN_THEME = 'journal'
    WINDOW_SIZE = (1300, 900)
    FONTS = {
        'title': ('Bradley Hand ITC', 20),
        'normal': ('Helvetica', 12),
    }


def center_window(window, width, height):
    """窗口居中"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    window.geometry(f'{width}x{height}+{x}+{y}')


def create_notice_window(parent_window, title, message):
    """创建通知窗口"""
    notice_window = ttk.Toplevel(parent_window)
    center_window(notice_window, 320, 300)
    notice_window.title(title)
    ttk.Label(notice_window, text=message).grid(row=0, column=0, pady=10, padx=10, sticky='nsew')
    close_button = ttk.Button(notice_window, text="关闭", bootstyle="danger", command=notice_window.destroy)
    close_button.grid(row=1, column=0, pady=10)


class User:
    """用户类"""
    def __init__(self, nickname, password):
        self.id = str(uuid.uuid4())
        self.nickname = nickname
        self.password = self.encrypt_password(password)

    def encrypt_password(self, password):
        return sha256(password.encode()).hexdigest()

    def save_to_csv(self, path):
        with open(path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([self.id, self.nickname, self.password])


class MainUser:
    """主用户类"""
    def __init__(self, nickname, user_id, age=None, hobbies=None, birthday=None, signature=None):
        self.nickname = nickname
        self.user_id = user_id
        self.age = age
        self.hobbies = hobbies
        self.birthday = birthday
        self.signature = signature

    def update_info(self, age=None, hobbies=None, birthday=None, signature=None):
        if age is not None:
            self.age = age
        if hobbies is not None:
            self.hobbies = hobbies
        if birthday is not None:
            self.birthday = birthday
        if signature is not None:
            self.signature = signature

    def save_to_csv(self, csv_file):
        updated = False
        data = []
        
        try:
            with open(csv_file, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == self.nickname and row[1] == self.user_id:
                        data.append([self.nickname, self.user_id, self.age, 
                                   self.hobbies, self.birthday, self.signature])
                        updated = True
                    else:
                        data.append(row)
        except FileNotFoundError:
            pass

        if not updated:
            data.append([self.nickname, self.user_id, self.age, 
                        self.hobbies, self.birthday, self.signature])

        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)


class UserService:
    """用户服务"""
    def __init__(self):
        self.user_file = "User_file.csv"
        self.user_info_file = "User_info.csv"

    def authenticate_user(self, nickname, password):
        password_encrypt = sha256(password.encode()).hexdigest()
        try:
            with open(self.user_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for user_id, user_nickname, user_password in reader:
                    if nickname == user_nickname and password_encrypt == user_password:
                        return True, user_id
            return False, None
        except FileNotFoundError:
            return False, None

    def load_user(self, nickname, user_id):
        try:
            with open(self.user_info_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 6 and row[0] == nickname and row[1] == user_id:
                        return MainUser(row[0], row[1], row[2], row[3], row[4], row[5])
        except (FileNotFoundError, ValueError):
            pass
        
        # 创建新用户
        user = MainUser(nickname, user_id)
        user.save_to_csv(self.user_info_file)
        return user

    def register_user(self, nickname, password):
        if self._username_exists(nickname):
            return False, "用户名已存在"
        
        user = User(nickname, password)
        user.save_to_csv(self.user_file)
        return True, "注册成功"

    def _username_exists(self, nickname):
        try:
            with open(self.user_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for _, user_nickname, _ in reader:
                    if nickname == user_nickname:
                        return True
        except FileNotFoundError:
            pass
        return False


class BlackBoard:
    """公告板"""
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.messages_file = "BBmessages.csv"
        self._setup_ui()
        self._load_messages()

    def _setup_ui(self):
        self.title_label = ttk.Label(
            self.parent_frame, 
            text="学生公告板", 
            font=Config.FONTS['title']
        )
        self.title_label.pack()

        self.messages_text = ttk.Text(self.parent_frame, height=10, width=50)
        self.messages_text.pack()

        self.input_text = ttk.Entry(self.parent_frame, width=50)
        self.input_text.pack(pady=5)
        self.input_text.bind("<Return>", lambda event: self._add_message())

        self.submit_button = ttk.Button(
            self.parent_frame, 
            text="提交消息", 
            command=self._add_message
        )
        self.submit_button.pack()

    def _add_message(self):
        message = self.input_text.get().strip()
        if message:
            self.messages_text.insert(ttk.END, f"{message}\n")
            self.messages_text.see(ttk.END)
            self.input_text.delete(0, ttk.END)
            self._save_message(message)

    def _save_message(self, message):
        with open(self.messages_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([message])

    def _load_messages(self):
        try:
            with open(self.messages_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        self.messages_text.insert(ttk.END, f"{row[0]}\n")
        except FileNotFoundError:
            pass


class MainWindow:
    """主窗口"""
    def __init__(self, nickname, user_id):
        self.nickname = nickname
        self.user_id = user_id
        self.user_service = UserService()
        self.current_user = None

    def show(self):
        self.current_user = self.user_service.load_user(self.nickname, self.user_id)
        
        self.window = ttk.Window(themename=Config.MAIN_THEME)
        self.window.title("Our Social Club - 主界面")
        self.window.configure(bg="lightblue")
        center_window(self.window, *Config.WINDOW_SIZE)
        
        self._setup_menu()
        self._setup_ui()
        
        self.window.mainloop()

    def _setup_menu(self):
        main_menu = ttk.Menu(self.window)
        self.window.config(menu=main_menu)

        settings_menu = ttk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="设置", menu=settings_menu)
        settings_menu.add_command(label="退出", command=self.window.quit)
        settings_menu.add_command(label="个性化设置", command=self._show_coming_soon)

        security_menu = ttk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="安全", menu=security_menu)
        security_menu.add_command(label="密保问题", command=self._show_coming_soon)
        security_menu.add_command(label="修改密码", command=self._show_coming_soon)

    def _setup_ui(self):
        # 欢迎标签
        welcome_label = ttk.Label(
            self.window, 
            text=f"欢迎 {self.current_user.nickname} 访问我们的俱乐部！",
            font=('Helvetica', 20)
        )
        welcome_label.place(x=100, y=100)

        # 功能按钮
        self._setup_function_buttons()
        
        # 公告板
        self._setup_blackboard()
        
        # 其他功能
        self._setup_other_features()

    def _setup_function_buttons(self):
        button_frame = ttk.Frame(self.window, padding=10)
        button_frame.pack(expand=False, side='left', padx=100)

        title_label = ttk.Label(button_frame, text="用户功能选择")
        title_label.grid(row=0, column=0, padx=5)

        buttons = [
            ("我的资料", self._show_coming_soon),
            ("添加好友", self._show_coming_soon),
            ("删除好友", self._show_coming_soon),
            ("查看好友", self._show_coming_soon),
            ("任务公告板", self._show_coming_soon)
        ]

        for i, (text, command) in enumerate(buttons, 1):
            button = ttk.Button(button_frame, text=text, command=command)
            button.grid(row=i, column=0, padx=5, pady=2)

    def _setup_blackboard(self):
        blackboard_frame = ttk.Frame(self.window, style='secondary', padding=10)
        blackboard_frame.pack(expand=True, padx=100, pady=50)
        self.blackboard = BlackBoard(blackboard_frame)

    def _setup_other_features(self):
        # 意见箱
        opinion_frame = ttk.Frame(self.window, padding=10)
        opinion_frame.place(x=700, y=800)
        
        ttk.Label(opinion_frame, text="想给我们一些意见吗？").grid(row=0, column=0, padx=5)
        ttk.Button(opinion_frame, text="点击这里！", bootstyle="info-link",
                  command=self._show_coming_soon).grid(row=0, column=1, padx=20)

        # 招聘信息
        recruitment_frame = ttk.Frame(self.window, bootstyle="primary", padding=10)
        recruitment_frame.place(x=100, y=800)
        
        ttk.Label(recruitment_frame, text="招聘信息在这里：").grid(row=0, column=0, padx=20)
        ttk.Button(recruitment_frame, text="发现新机会！",
                  command=self._show_coming_soon).grid(row=0, column=1, padx=20)

        # 文件共享
        fileshare_frame = ttk.Frame(self.window, padding=10)
        fileshare_frame.place(x=100, y=600)
        
        ttk.Label(fileshare_frame, text="文件共享站：").grid(row=0, column=0, padx=10)
        ttk.Button(fileshare_frame, text="进入",
                  command=self._show_coming_soon).grid(row=0, column=1, padx=20)

        # 失物招领
        lost_found_frame = ttk.Frame(self.window, padding=10)
        lost_found_frame.place(x=700, y=700)
        
        ttk.Label(lost_found_frame, text="失物招领区\n在这里寻找：").grid(row=0, column=0, padx=20)
        ttk.Button(lost_found_frame, text="进入",
                  command=self._show_coming_soon).grid(row=0, column=1, padx=20)

    def _show_coming_soon(self):
        create_notice_window(self.window, "提示", "功能正在开发中，敬请期待！")


class AuthController:
    """认证控制器"""
    def __init__(self):
        self.user_service = UserService()

    def handle_login(self, window, nickname, password):
        if not nickname or not password:
            create_notice_window(window, "错误", "请输入用户名和密码")
            return
        
        success, user_id = self.user_service.authenticate_user(nickname, password)
        
        if success:
            create_notice_window(window, "成功", "登录成功！正在跳转...")
            window.after(1000, lambda: [
                MainWindow(nickname, user_id).show(),
                window.destroy()
            ])
        else:
            create_notice_window(window, "错误", "用户名或密码错误")

    def handle_register(self, window, nickname, password, confirm_password):
        if not nickname or not password:
            create_notice_window(window, "错误", "请填写完整信息")
            return
        
        if password != confirm_password:
            create_notice_window(window, "错误", "两次输入的密码不一致")
            return
        
        if len(password) < 6:
            create_notice_window(window, "错误", "密码长度至少6位")
            return
        
        success, message = self.user_service.register_user(nickname, password)
        
        if success:
            create_notice_window(window, "成功", message)
            window.after(2000, window.destroy)
        else:
            create_notice_window(window, "错误", message)


class SignupWindow:
    """注册窗口"""
    def __init__(self):
        self.auth_controller = AuthController()

    def show(self):
        self.window = ttk.Toplevel()
        self.window.title("Our Social Club - 注册")
        center_window(self.window, 400, 300)
        
        self._setup_ui()

    def _setup_ui(self):
        ttk.Label(self.window, text="用户注册", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=20)

        ttk.Label(self.window, text="用户名:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.username_entry = ttk.Entry(self.window)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

        ttk.Label(self.window, text="密码:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.password_entry = ttk.Entry(self.window, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

        ttk.Label(self.window, text="确认密码:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.confirm_password_entry = ttk.Entry(self.window, show="*")
        self.confirm_password_entry.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

        button_frame = ttk.Frame(self.window)
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)

        ttk.Button(button_frame, text="注册", bootstyle="success",
                  command=self._handle_register).pack(side="left", padx=5)
        ttk.Button(button_frame, text="取消", bootstyle="secondary",
                  command=self.window.destroy).pack(side="left", padx=5)

        self.window.grid_columnconfigure(1, weight=1)

    def _handle_register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        self.auth_controller.handle_register(
            self.window, username, password, confirm_password
        )


class LoginWindow:
    """登录窗口"""
    def __init__(self):
        self.auth_controller = AuthController()

    def show(self):
        self.window = ttk.Window(themename=Config.DEFAULT_THEME)
        self.window.title("Our Social Club - 登录")
        center_window(self.window, *Config.WINDOW_SIZE)
        
        self._setup_styles()
        self._setup_background()
        self._setup_ui()
        
        self.window.mainloop()

    def _setup_styles(self):
        style = ttk.Style()
        style.configure('Custom.TLabel', font=Config.FONTS['title'])
        style.configure('Custom.TButton', font=Config.FONTS['normal'])

    def _setup_background(self):
        try:
            # 尝试多个可能的路径
            image_paths = [
                'assets/Background.jpg',
                'Pic/Background.jpg',
                'assets/background.jpg',
                'Pic/background.jpg'
            ]
            
            background_image = None
            for path in image_paths:
                if os.path.exists(path):
                    original_image = Image.open(path)
                    resized_image = original_image.resize(Config.WINDOW_SIZE, Image.Resampling.LANCZOS)
                    background_image = ImageTk.PhotoImage(resized_image)
                    break
            
            if background_image:
                background_label = ttk.Label(self.window, image=background_image)
                background_label.place(x=0, y=0, relwidth=1, relheight=1)
                background_label.image = background_image  # 保持引用
            else:
                self.window.configure(bg="lightblue")
        except Exception:
            self.window.configure(bg="lightblue")

    def _setup_ui(self):
        # 标题
        title_label = ttk.Label(
            self.window, 
            text="                  Our Social Club\nThe Final Frontier for meeting others", 
            style='Custom.TLabel'
        )
        title_label.grid(row=0, column=0, pady=20, columnspan=3)

        # 用户名
        ttk.Label(self.window, text="用户名:").grid(row=1, column=0, padx=10, sticky='e')
        self.username_entry = ttk.Entry(self.window, style='success')
        self.username_entry.grid(row=1, column=1, padx=10, sticky='ew')

        # 密码
        ttk.Label(self.window, text="密码:").grid(row=2, column=0, padx=10, sticky='e')
        self.password_entry = ttk.Entry(self.window, show="*", style='success')
        self.password_entry.grid(row=2, column=1, padx=10, sticky='ew')

        # 登录按钮
        ttk.Button(self.window, text="登录", bootstyle='info',
                  command=self._handle_login).grid(row=3, column=2, padx=10)

        # 注册和找回密码区域
        self._setup_signup_area()

        self.window.grid_columnconfigure(1, weight=1)

    def _setup_signup_area(self):
        signup_frame = ttk.Frame(self.window, bootstyle="secondary")
        signup_frame.place(x=500, y=750)

        ttk.Label(signup_frame, text="还没有账户？", font=("Helvetica", 12)).pack(padx=5)
        ttk.Button(signup_frame, text="注册", bootstyle="secondary", 
                  style='Custom.TButton', command=self._open_signup_window).pack()

        ttk.Label(signup_frame, text="忘记密码？", font=("Helvetica", 12)).pack(padx=5)
        ttk.Button(signup_frame, text="找回密码", bootstyle="warning",
                  command=self._show_forgot_password).pack(padx=5)

    def _handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.auth_controller.handle_login(self.window, username, password)

    def _open_signup_window(self):
        signup_window = SignupWindow()
        signup_window.show()

    def _show_forgot_password(self):
        create_notice_window(self.window, "提示", "找回密码功能正在开发中...")


def main():
    """主函数"""
    try:
        login_window = LoginWindow()
        login_window.show()
    except Exception as e:
        print(f"应用程序启动失败: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
