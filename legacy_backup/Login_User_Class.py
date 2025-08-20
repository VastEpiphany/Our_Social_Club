import csv
import uuid
from hashlib import sha256

class User:
    def __init__(self,nickname,psw):
        self.id =uuid.uuid4()
        self.nick_name = nickname
        self.password = self.encrypt_password(psw)

    def encrypt_password(self,psw):
        """对用户密码进行加密"""
        return sha256(psw.encode()).hexdigest()

    def save_to_csv(self,path):
        with open(path,'a',newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([self.id, self.nick_name, self.password])
