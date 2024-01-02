from Login_User_Class import User
import csv

class Main_User(User):
    """
    Main_User类，用来在用户登录后创建相应对象并进行相关信息操作的类，继承自用于登录的User类
    """
    def __init__(self,nic,uid,age=None,hobbies=None,birthday=None,sign=None):
        """
        构造函数，初始默认用户只有名称和id这两种属性，后续属性需要用户自己去添加故默认为None
        :param nic:
        :param uid:
        :param age:
        :param hobbies:
        :param birthday:
        :param sign:
        """
        self.nickname = nic
        self.mid = uid
        self.age = age
        self.hobbies = hobbies
        self.birthday = birthday
        self.sign = sign

    def update_info(self,age=None,hobbies=None,birthday=None,sign=None):
        """
        用于更新某一特定信息的函数
        :param age: 年龄
        :param hobbies: 爱好
        :param birthday: 生日
        :param sign: 个性签名
        :return: 啥玩意儿也不返回
        """
        if age is not None:
            self.age = age
        if hobbies is not None:
            self.hobbies = hobbies
        if birthday is not None:
            self.birthday = birthday
        if sign is not None:
            self.sign = sign



    def save_to_csv(self, csv_file):
        '''
        Saves the current user's information to a specified CSV file.
        :param csv_file: Path to the CSV file
        '''
        updated = False
        data = []
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == self.nickname and row[1] == self.mid:
                    data.append([self.nickname, self.mid, self.age, self.hobbies, self.birthday, self.sign])
                    updated = True
                else:
                    data.append(row)

        if not updated:
            data.append([self.nickname, self.mid, self.age, self.hobbies, self.birthday, self.sign])

        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
