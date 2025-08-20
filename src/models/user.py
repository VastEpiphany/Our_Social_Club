"""
用户模型类
包含基础用户类和完整用户类的定义
"""
import csv
import uuid
from hashlib import sha256
from typing import Optional


class User:
    """基础用户类，用于登录验证"""
    
    def __init__(self, nickname: str, password: str):
        self.id = str(uuid.uuid4())
        self.nickname = nickname
        self.password = self.encrypt_password(password)

    def encrypt_password(self, password: str) -> str:
        """对用户密码进行加密"""
        return sha256(password.encode()).hexdigest()

    def save_to_csv(self, path: str) -> None:
        """保存用户信息到CSV文件"""
        with open(path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([self.id, self.nickname, self.password])


class MainUser(User):
    """主用户类，用于登录后的用户信息管理"""
    
    def __init__(self, nickname: str, user_id: str, age: Optional[str] = None, 
                 hobbies: Optional[str] = None, birthday: Optional[str] = None, 
                 signature: Optional[str] = None):
        """
        初始化主用户对象
        
        Args:
            nickname: 用户昵称
            user_id: 用户ID
            age: 年龄
            hobbies: 爱好
            birthday: 生日
            signature: 个性签名
        """
        self.nickname = nickname
        self.user_id = user_id
        self.age = age
        self.hobbies = hobbies
        self.birthday = birthday
        self.signature = signature

    def update_info(self, age: Optional[str] = None, hobbies: Optional[str] = None, 
                   birthday: Optional[str] = None, signature: Optional[str] = None) -> None:
        """
        更新用户信息
        
        Args:
            age: 年龄
            hobbies: 爱好
            birthday: 生日
            signature: 个性签名
        """
        if age is not None:
            self.age = age
        if hobbies is not None:
            self.hobbies = hobbies
        if birthday is not None:
            self.birthday = birthday
        if signature is not None:
            self.signature = signature

    def save_to_csv(self, csv_file: str) -> None:
        """
        保存用户信息到CSV文件
        
        Args:
            csv_file: CSV文件路径
        """
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

    def to_dict(self) -> dict:
        """转换为字典格式"""
        return {
            'nickname': self.nickname,
            'user_id': self.user_id,
            'age': self.age,
            'hobbies': self.hobbies,
            'birthday': self.birthday,
            'signature': self.signature
        }
