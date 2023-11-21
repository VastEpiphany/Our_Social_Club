import csv
from Main_User_Class import Main_User


def Load_User(nic,uid):
    try:
        with open("User_info.csv",'r',encoding='utf-8') as file:
            reader = csv.reader(file)
            for nickname,u_id,age,hobbies,birthday,sign in reader:
                if nic == nickname and uid == u_id:
                    Main_User(nickname,uid,age,hobbies,birthday,sign)
                    return Main_User
            with open("User_info.csv", 'a', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([nic, uid, None, None, None, None])
                return Main_User(nic, uid)

    except FileNotFoundError:
        with open("User_info.csv",'a',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([nic,uid,None,None,None,None])
