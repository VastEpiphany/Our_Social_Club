"""
主窗口视图
"""
import ttkbootstrap as ttk
from ..services.user_service import UserService
from ..utils.window_utils import center_window
from ..models.user import MainUser


class MainWindow:
    """主窗口类"""
    
    def __init__(self, nickname: str, user_id: str):
        self.nickname = nickname
        self.user_id = user_id
        self.user_service = UserService()
        self.current_user = None
        self.window = None

    def create_window(self) -> ttk.Window:
        """创建主窗口"""
        # 加载用户信息
        self.current_user = self.user_service.load_user(self.nickname, self.user_id)
        
        self.window = ttk.Window(themename='journal')
        self.window.title("Our Social Club - 主界面")
        self.window.configure(bg="lightblue")
        center_window(self.window, 1300, 900)
        
        self._setup_menu()
        self._setup_ui()
        
        return self.window

    def _setup_menu(self) -> None:
        """设置菜单栏"""
        main_menu = ttk.Menu(self.window)
        self.window.config(menu=main_menu)

        # 设置菜单
        settings_menu = ttk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="设置", menu=settings_menu)
        settings_menu.add_command(label="退出", command=self.window.quit)
        settings_menu.add_command(label="个性化设置", command=self._open_personalization)

        # 安全菜单
        security_menu = ttk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="安全", menu=security_menu)
        security_menu.add_command(label="密保问题", command=self._open_security_question)
        security_menu.add_command(label="修改密码", command=self._open_change_password)

    def _setup_ui(self) -> None:
        """设置用户界面"""
        # 欢迎标签
        welcome_label = ttk.Label(
            self.window, 
            text=f"欢迎 {self.current_user.nickname} 访问我们的俱乐部！",
            font=('Helvetica', 20)
        )
        welcome_label.place(x=100, y=100)

        # 功能按钮区域
        self._setup_function_buttons()
        
        # 公告板区域
        self._setup_blackboard()
        
        # 其他功能区域
        self._setup_other_features()

    def _setup_function_buttons(self) -> None:
        """设置功能按钮区域"""
        button_frame = ttk.Frame(self.window, padding=10)
        button_frame.pack(expand=False, side='left', padx=100)

        # 标题
        title_label = ttk.Label(button_frame, text="用户功能选择")
        title_label.grid(row=0, column=0, padx=5)

        # 功能按钮
        buttons = [
            ("我的资料", self._open_profile),
            ("添加好友", self._open_add_friend),
            ("删除好友", self._open_delete_friend),
            ("查看好友", self._open_show_friends),
            ("任务公告板", self._open_task_board)
        ]

        for i, (text, command) in enumerate(buttons, 1):
            button = ttk.Button(button_frame, text=text, command=command)
            button.grid(row=i, column=0, padx=5, pady=2)

    def _setup_blackboard(self) -> None:
        """设置公告板"""
        blackboard_frame = ttk.Frame(self.window, style='secondary', padding=10)
        blackboard_frame.pack(expand=True, padx=100, pady=50)
        
        from ..components.blackboard import BlackBoard
        self.blackboard = BlackBoard(blackboard_frame)

    def _setup_other_features(self) -> None:
        """设置其他功能区域"""
        # 意见箱
        opinion_frame = ttk.Frame(self.window, padding=10)
        opinion_frame.place(x=700, y=800)
        
        opinion_label = ttk.Label(opinion_frame, text="想给我们一些意见吗？")
        opinion_label.grid(row=0, column=0, padx=5)
        
        opinion_button = ttk.Button(
            opinion_frame, 
            text="点击这里！", 
            bootstyle="info-link",
            command=self._open_opinion_box
        )
        opinion_button.grid(row=0, column=1, padx=20)

        # 招聘信息
        recruitment_frame = ttk.Frame(self.window, bootstyle="primary", padding=10)
        recruitment_frame.place(x=100, y=800)
        
        recruitment_label = ttk.Label(recruitment_frame, text="招聘信息在这里：")
        recruitment_label.grid(row=0, column=0, padx=20)
        
        recruitment_button = ttk.Button(
            recruitment_frame, 
            text="发现新机会！",
            command=self._open_recruitment
        )
        recruitment_button.grid(row=0, column=1, padx=20)

        # 文件共享
        fileshare_frame = ttk.Frame(self.window, padding=10)
        fileshare_frame.place(x=100, y=600)
        
        fileshare_label = ttk.Label(fileshare_frame, text="文件共享站：")
        fileshare_label.grid(row=0, column=0, padx=10)
        
        fileshare_button = ttk.Button(
            fileshare_frame, 
            text="进入",
            command=self._open_file_sharing
        )
        fileshare_button.grid(row=0, column=1, padx=20)

        # 失物招领
        lost_found_frame = ttk.Frame(self.window, padding=10)
        lost_found_frame.place(x=700, y=700)
        
        lost_found_label = ttk.Label(lost_found_frame, text="失物招领区\n在这里寻找：")
        lost_found_label.grid(row=0, column=0, padx=20)
        
        lost_found_button = ttk.Button(
            lost_found_frame, 
            text="进入",
            command=self._open_lost_found
        )
        lost_found_button.grid(row=0, column=1, padx=20)

    # 事件处理方法
    def _open_profile(self) -> None:
        """打开个人资料"""
        from ..utils.window_utils import create_notice_window
        create_notice_window(self.window, "提示", "个人资料功能正在开发中...")

    def _open_add_friend(self) -> None:
        """打开添加好友"""
        from ..utils.window_utils import create_notice_window
        create_notice_window(self.window, "提示", "添加好友功能正在开发中...")

    def _open_delete_friend(self) -> None:
        """打开删除好友"""
        from ..utils.window_utils import create_notice_window
        create_notice_window(self.window, "提示", "删除好友功能正在开发中...")

    def _open_show_friends(self) -> None:
        """打开查看好友"""
        from ..utils.window_utils import create_notice_window
        create_notice_window(self.window, "提示", "查看好友功能正在开发中...")

    def _open_task_board(self) -> None:
        """打开任务公告板"""
        from ..utils.window_utils import create_notice_window
        create_notice_window(self.window, "提示", "任务公告板功能正在开发中...")

    def _open_personalization(self) -> None:
        """打开个性化设置"""
        from ..utils.window_utils import create_notice_window
        create_notice_window(self.window, "提示", "个性化设置功能正在开发中...")

    def _open_security_question(self) -> None:
        """打开密保问题设置"""
        from ..utils.window_utils import create_notice_window
        create_notice_window(self.window, "提示", "密保问题功能正在开发中...")

    def _open_change_password(self) -> None:
        """打开修改密码"""
        from ..utils.window_utils import create_notice_window
        create_notice_window(self.window, "提示", "修改密码功能正在开发中...")

    def _open_opinion_box(self) -> None:
        """打开意见箱"""
        from ..utils.window_utils import create_notice_window
        create_notice_window(self.window, "提示", "意见箱功能正在开发中...")

    def _open_recruitment(self) -> None:
        """打开招聘信息"""
        from ..utils.window_utils import create_notice_window
        create_notice_window(self.window, "提示", "招聘信息功能正在开发中...")

    def _open_file_sharing(self) -> None:
        """打开文件共享"""
        from ..utils.window_utils import create_notice_window
        create_notice_window(self.window, "提示", "文件共享功能正在开发中...")

    def _open_lost_found(self) -> None:
        """打开失物招领"""
        from ..utils.window_utils import create_notice_window
        create_notice_window(self.window, "提示", "失物招领功能正在开发中...")

    def show(self) -> None:
        """显示窗口"""
        self.create_window()
        self.window.mainloop()
