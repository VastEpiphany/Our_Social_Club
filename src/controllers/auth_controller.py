"""
认证控制器
处理登录、注册等认证相关功能
"""
from typing import Any
from ..services.user_service import UserService
from ..utils.window_utils import create_notice_window


class AuthController:
    """认证控制器"""
    
    def __init__(self):
        self.user_service = UserService()

    def handle_login(self, window: Any, nickname: str, password: str) -> None:
        """
        处理用户登录
        
        Args:
            window: 登录窗口
            nickname: 用户昵称
            password: 密码
        """
        if not nickname or not password:
            create_notice_window(window, "错误", "请输入用户名和密码")
            return
        
        success, user_id = self.user_service.authenticate_user(nickname, password)
        
        if success:
            create_notice_window(window, "成功", "登录成功！正在跳转...")
            # 延迟跳转到主界面
            from ..views.main_window import MainWindow
            window.after(1000, lambda: [
                MainWindow(nickname, user_id).show(),
                window.destroy()
            ])
        else:
            create_notice_window(window, "错误", "用户名或密码错误")

    def handle_register(self, window: Any, nickname: str, password: str, confirm_password: str) -> None:
        """
        处理用户注册
        
        Args:
            window: 注册窗口
            nickname: 用户昵称
            password: 密码
            confirm_password: 确认密码
        """
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
