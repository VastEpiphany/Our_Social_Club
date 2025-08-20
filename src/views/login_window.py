"""
登录窗口视图
"""
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from ..controllers.auth_controller import AuthController
from ..utils.window_utils import center_window, configure_styles


class LoginWindow:
    """登录窗口类"""
    
    def __init__(self):
        self.auth_controller = AuthController()
        self.window = None
        self.username_entry = None
        self.password_entry = None

    def create_window(self) -> ttk.Window:
        """创建登录窗口"""
        from ..config import Config
        self.window = ttk.Window(themename=Config.DEFAULT_THEME)
        self.window.title("Our Social Club - 登录")
        center_window(self.window, *Config.LOGIN_WINDOW_SIZE)
        
        self._setup_styles()
        self._setup_background()
        self._setup_ui()
        
        return self.window

    def _setup_styles(self) -> None:
        """设置样式"""
        from ..config import Config
        style = ttk.Style()
        style.configure('Custom.TLabel', font=Config.FONTS['title'])
        style.configure('Custom.TButton', font=Config.FONTS['normal'])

    def _setup_background(self) -> None:
        """设置背景图片"""
        from ..config import Config
        try:
            original_image = Image.open(Config.BACKGROUND_IMAGE)
            resized_image = original_image.resize(Config.LOGIN_WINDOW_SIZE, Image.Resampling.LANCZOS)
            background_image = ImageTk.PhotoImage(resized_image)
            
            background_label = ttk.Label(self.window, image=background_image)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            # 保持图片引用
            background_label.image = background_image
        except FileNotFoundError:
            # 如果背景图片不存在，使用默认背景色
            self.window.configure(bg="lightblue")

    def _setup_ui(self) -> None:
        """设置用户界面"""
        # 标题
        title_label = ttk.Label(
            self.window, 
            text="                  Our Social Club\nThe Final Frontier for meeting others", 
            style='Custom.TLabel'
        )
        title_label.grid(row=0, column=0, pady=20, columnspan=3)

        # 用户名输入
        username_label = ttk.Label(self.window, text="用户名:")
        username_label.grid(row=1, column=0, padx=10, sticky='e')
        
        self.username_entry = ttk.Entry(self.window, style='success')
        self.username_entry.grid(row=1, column=1, padx=10, sticky='ew')

        # 密码输入
        password_label = ttk.Label(self.window, text="密码:")
        password_label.grid(row=2, column=0, padx=10, sticky='e')
        
        self.password_entry = ttk.Entry(self.window, show="*", style='success')
        self.password_entry.grid(row=2, column=1, padx=10, sticky='ew')

        # 登录按钮
        login_button = ttk.Button(
            self.window, 
            text="登录", 
            bootstyle='info',
            command=self._handle_login
        )
        login_button.grid(row=3, column=2, padx=10)

        # 注册和找回密码区域
        self._setup_signup_area()

        # 调整网格列权重
        self.window.grid_columnconfigure(1, weight=1)

    def _setup_signup_area(self) -> None:
        """设置注册和找回密码区域"""
        signup_frame = ttk.Frame(self.window, bootstyle="secondary")
        signup_frame.place(x=500, y=750)

        signup_label = ttk.Label(signup_frame, text="还没有账户？", font=("Helvetica", 12))
        signup_label.pack(padx=5)

        signup_button = ttk.Button(
            signup_frame, 
            text="注册", 
            bootstyle="secondary", 
            style='Custom.TButton',
            command=self._open_signup_window
        )
        signup_button.pack()

        forgot_label = ttk.Label(signup_frame, text="忘记密码？", font=("Helvetica", 12))
        forgot_label.pack(padx=5)

        forgot_button = ttk.Button(
            signup_frame, 
            text="找回密码", 
            bootstyle="warning",
            command=self._open_forgot_password_window
        )
        forgot_button.pack(padx=5)

    def _handle_login(self) -> None:
        """处理登录"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.auth_controller.handle_login(self.window, username, password)

    def _open_signup_window(self) -> None:
        """打开注册窗口"""
        from .signup_window import SignupWindow
        signup_window = SignupWindow()
        signup_window.show()

    def _open_forgot_password_window(self) -> None:
        """打开找回密码窗口"""
        from ..utils.window_utils import create_notice_window
        create_notice_window(self.window, "提示", "找回密码功能正在开发中...")

    def show(self) -> None:
        """显示窗口"""
        self.create_window()
        self.window.mainloop()
