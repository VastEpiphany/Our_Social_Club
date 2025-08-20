"""
用户服务类
处理用户相关的业务逻辑
"""
import csv
import os
from hashlib import sha256
from typing import Optional, Tuple
from ..models.user import MainUser


class UserService:
    """用户服务类"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.user_file = os.path.join(data_dir, "User_file.csv")
        self.user_info_file = os.path.join(data_dir, "User_info.csv")
        self._ensure_data_files()

    def _ensure_data_files(self) -> None:
        """确保数据文件存在"""
        os.makedirs(self.data_dir, exist_ok=True)
        
        # 创建用户登录文件
        if not os.path.exists(self.user_file):
            with open(self.user_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['user_id', 'nickname', 'password'])
        
        # 创建用户信息文件
        if not os.path.exists(self.user_info_file):
            with open(self.user_info_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['nickname', 'user_id', 'age', 'hobbies', 'birthday', 'signature'])

    def authenticate_user(self, nickname: str, password: str) -> Tuple[bool, Optional[str]]:
        """
        验证用户登录
        
        Args:
            nickname: 用户昵称
            password: 密码
            
        Returns:
            (验证结果, 用户ID)
        """
        password_encrypt = sha256(password.encode()).hexdigest()
        
        try:
            with open(self.user_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # 跳过标题行
                for user_id, user_nickname, user_password in reader:
                    if nickname == user_nickname and password_encrypt == user_password:
                        return True, user_id
            return False, None
        except FileNotFoundError:
            return False, None

    def load_user(self, nickname: str, user_id: str) -> MainUser:
        """
        加载用户信息
        
        Args:
            nickname: 用户昵称
            user_id: 用户ID
            
        Returns:
            MainUser对象
        """
        try:
            with open(self.user_info_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # 跳过标题行
                for row in reader:
                    if len(row) >= 6 and row[0] == nickname and row[1] == user_id:
                        return MainUser(row[0], row[1], row[2], row[3], row[4], row[5])
        except (FileNotFoundError, ValueError):
            pass
        
        # 如果用户不存在，创建新用户
        user = MainUser(nickname, user_id)
        self._save_user_info(user)
        return user

    def _save_user_info(self, user: MainUser) -> None:
        """
        保存用户信息到文件
        
        Args:
            user: MainUser对象
        """
        user.save_to_csv(self.user_info_file)

    def register_user(self, nickname: str, password: str) -> Tuple[bool, str]:
        """
        注册新用户
        
        Args:
            nickname: 用户昵称
            password: 密码
            
        Returns:
            (注册结果, 消息)
        """
        # 检查用户名是否已存在
        if self._username_exists(nickname):
            return False, "用户名已存在"
        
        from ..models.user import User
        user = User(nickname, password)
        user.save_to_csv(self.user_file)
        
        return True, "注册成功"

    def _username_exists(self, nickname: str) -> bool:
        """
        检查用户名是否存在
        
        Args:
            nickname: 用户昵称
            
        Returns:
            是否存在
        """
        try:
            with open(self.user_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # 跳过标题行
                for _, user_nickname, _ in reader:
                    if nickname == user_nickname:
                        return True
        except FileNotFoundError:
            pass
        return False
