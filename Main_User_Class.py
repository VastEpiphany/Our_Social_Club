from Login_User_Class import User

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


    def save_user_info(self,file_path):
        pass

    def load_user_info(self,file_path):
        pass