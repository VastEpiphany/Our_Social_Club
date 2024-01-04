import tkinter

import ttkbootstrap as ttk
from Center_window import center_window
import csv

class AddFriend_Window:

    #初始化类，在这里进行了很多有关于窗口的操作以及成员变量的申请
    def __init__(self, window, this_user):
        self.file = "User_info.csv"
        self.window = ttk.Toplevel(window)
        self.myname = this_user.nickname

        self.window.title("Add Friends & Friends Recommendation")
        center_window(self.window, 800, 600)

        recommended_friends = self.friend_recommendation(this_user)

        # 检查是否有推荐的朋友,对应不同情况采取不同显示内容
        if recommended_friends == ["Hmm... Seems that no person has to become your friend TAT"]:
            message = "Hmm... Seems that no person has to become your friend TAT"
        else:
            message = "Below are friends that you might want to greet with: " + ', '.join(recommended_friends)
            button1 = ttk.Button(self.window, text="Add them",
                                 command=lambda: self.add_recommend_friend_notify(recommended_friends))
            button1.place(x=300,y=80)

        text = ttk.Label(self.window, text=message, font=('Bradley Hand ITC', 15))
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

    def friend_add(self, nickname):
        try:
            with open("user_friend.csv", "a", newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([self.myname, nickname])  # 分别写入当前用户昵称和朋友昵称
        except Exception as e:
            print("Error occurred while adding friend:", e)

    def add_recommend_friend_notify(self,recommend_friend):
        flag = True
        for friend_nickname in recommend_friend:
            try:
                self.friend_add(friend_nickname)
            except Exception as e:
                flag = False
                tkinter.messagebox.showerror("Error", f"Failed to add {friend_nickname}: {e}")
                break
        if flag:
            tkinter.messagebox.showinfo("Success", "All friends added successfully!")


    def friend_get(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                friendlist = []
                for row in reader:
                    # 确保行中有足够的元素
                    if len(row) >= 2:
                        myname, friendname = row
                        if myname == self.myname:
                            friendlist.append(friendname)
                return friendlist
        except FileNotFoundError:
            return "Error! File not found."
        except ValueError:
            return "Error! Incorrect file format."
        except Exception as e:
            return f"An error occurred: {e}"
