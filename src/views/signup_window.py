"""
注册窗口视图
"""
import ttkbootstrap as ttk
from ..controllers.auth_controller import AuthController
from ..utils.window_utils import center_window


class SignupWindow:
    """注册窗口类"""
    
    def __init__(self):
        self.auth_controller = AuthController()
        self.window = None
        self.username_entry = None
        self.password_entry = None
        self.confirm_password_entry = None

    def create_window(self) -> ttk.Toplevel:
        """创建注册窗口"""
        self.window = ttk.Toplevel()
        self.window.title("Our Social Club - 注册")
        center_window(self.window, 400, 300)
        
        self._setup_ui()
        return self.window

    def _setup_ui(self) -> None:
        """设置用户界面"""
        # 标题
        title_label = ttk.Label(self.window, text="用户注册", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # 用户名
        username_label = ttk.Label(self.window, text="用户名:")
        username_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        
        self.username_entry = ttk.Entry(self.window)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

        # 密码
        password_label = ttk.Label(self.window, text="密码:")
        password_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        
        self.password_entry = ttk.Entry(self.window, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

        # 确认密码
        confirm_label = ttk.Label(self.window, text="确认密码:")
        confirm_label.grid(row=3, column=0, padx=10, pady=5, sticky='e')
        
        self.confirm_password_entry = ttk.Entry(self.window, show="*")
        self.confirm_password_entry.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

        # 按钮
        button_frame = ttk.Frame(self.window)
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)

        register_button = ttk.Button(
            button_frame, 
            text="注册", 
            bootstyle="success",
            command=self._handle_register
        )
        register_button.pack(side="left", padx=5)

        cancel_button = ttk.Button(
            button_frame, 
            text="取消", 
            bootstyle="secondary",
            command=self.window.destroy
        )
        cancel_button.pack(side="left", padx=5)

        # 调整列权重
        self.window.grid_columnconfigure(1, weight=1)

    def _handle_register(self) -> None:
        """处理注册"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        self.auth_controller.handle_register(
            self.window, username, password, confirm_password
        )

    def show(self) -> None:
        """显示窗口"""
        self.create_window()
        self.window.mainloop()
