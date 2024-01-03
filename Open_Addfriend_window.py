import ttkbootstrap as ttk
from Center_window import center_window
import csv

class AddFriend_Window:

    #初始化类，在这里进行了很多有关于窗口的操作以及成员变量的申请
    def __init__(self, window, this_user):
        self.file = "User_info.csv"
        self.window = ttk.Toplevel(window)

        self.window.title("Add Friends")
        center_window(self.window, 600, 400)

        recommended_friends = self.friend_recommendation(this_user)

        # 检查是否有推荐的朋友,对应不同情况采取不同显示内容
        if recommended_friends == ["Hmm... Seems that no person has to become your friend TAT"]:
            message = "Hmm... Seems that no person has to become your friend TAT"
        else:
            message = "Below are friends that you might want to greet with: " + ', '.join(recommended_friends)

        text = ttk.Label(self.window, text=message, font=('Bradley Hand ITC', 10))
        text.place(x=100, y=50)

    def friend_recommendation(self, this_user):
        recommended_friends = []  # 创建一个空列表来保存推荐的朋友
        try:
            with open(self.file, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    # 检查行是否为空
                    if not row or len(row) < 6:
                        continue  # 跳过空行或不完整的行

                    # 解包每行数据
                    nickname, u_id, age, hobbies, birthday, sign = row

                    # 转换数据类型（如果需要的话，但是目前暂时好像还不需要）
                    # 比如说：age = int(age), hobbies = hobbies.split(',') 什么的  暂时先放在这占个位

                    # 比较条件
                    if this_user.nickname != nickname and (this_user.age == age or this_user.hobbies == hobbies or this_user.birthday == birthday):
                        recommended_friends.append(nickname)  # 添加匹配的朋友到列表
        except FileNotFoundError:
            recommended_friends.append("Error Occurred since User_info file is missing.")

        if not recommended_friends:  # 如果列表为空
            return ["Hmm... Seems that no person has to become your friend TAT"]
        return recommended_friends

