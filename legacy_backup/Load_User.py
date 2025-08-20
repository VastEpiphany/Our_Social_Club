import csv
from Main_User_Class import Main_User


def Load_User(nic,uid):
    """

    :param nic: 用户nickname昵称
    :param uid: 用户id
    干什么用的：当用户第一次登录时，创建Main_User类成员并且将其默认属性nickname和id写入文件，留下年龄、爱好、生日等属性为
                空位等待用户后续登录后自己去补充
    """
    try:
        with open("User_info.csv",'r',encoding='utf-8') as file:
            reader = csv.reader(file)
            for nickname,u_id,age,hobbies,birthday,sign in reader:
                if nic == nickname and uid == u_id:
                    return Main_User(nickname,uid,age,hobbies,birthday,sign)
    except ValueError:
        with open("User_info.csv", 'a', newline="",encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([nic, uid, None, None, None, None])
            return Main_User(nic, uid)

    except FileNotFoundError:
        with open("User_info.csv",'a',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([nic,uid,None,None,None,None])
            return Main_User(nic,uid)
