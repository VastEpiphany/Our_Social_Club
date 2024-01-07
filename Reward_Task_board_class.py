import tkinter as tk
import ttkbootstrap as ttk
from Center_window import center_window
import csv
from datetime import datetime, timedelta


class RewardTaskBoard:
    # 构造函数，初始化 RewardTaskBoard 类的实例
    def __init__(self, parent):
        self.parent = parent  # 父窗口
        self.tasks_file = "RewardTasks.csv"  # 存储任务的 CSV 文件
        self.tasks = self.load_tasks()  # 加载任务
        self.create_window()  # 创建窗口

    def create_window(self):
        # 创建一个顶层窗口
        self.window = ttk.Toplevel(self.parent)
        self.window.title("Reward Tasks")
        #self.window.geometry("1000x1200")  # 设置窗口大小
        center_window(self.window,800,900) #设置窗口大小

        # 创建任务列表区域
        columns = ("Publisher", "Task Description", "Remaining Time", "Publish Time")
        self.tasks_list = ttk.Treeview(self.window, columns=columns, show="headings")
        for col in columns:
            self.tasks_list.heading(col, text=col)
        self.tasks_list.pack(expand=True, fill='both')

        # 创建发布人输入框
        ttk.Label(self.window, text="Publisher:").pack(pady=5)
        self.publisher_entry = ttk.Entry(self.window, width=50)
        self.publisher_entry.insert(0, "Enter your name here")
        self.publisher_entry.pack(pady=5)

        # 创建详细任务描述输入框
        ttk.Label(self.window, text="Task Description:").pack(pady=5)
        self.task_description_entry = ttk.Text(self.window, height=5, width=50)
        self.task_description_entry.pack(pady=10)

        # 创建倒计时选项的单选按钮
        ttk.Label(self.window, text="Select Duration:").pack(pady=5)
        self.duration_var = tk.IntVar(value=72)  # 默认选项为72小时
        ttk.Radiobutton(self.window, text='24 hours', value=24, variable=self.duration_var).pack()
        ttk.Radiobutton(self.window, text='36 hours', value=36, variable=self.duration_var).pack()
        ttk.Radiobutton(self.window, text='72 hours', value=72, variable=self.duration_var).pack()

        # 创建发布任务的按钮
        ttk.Button(self.window, text="Publish Task", command=self.publish_task).pack(pady=10)

        # 更新并显示任务列表
        self.update_tasks_display()
        self.update_remaining_time()  # 开始定时更新任务剩余时间

        # 添加编辑和删除按钮
        ttk.Button(self.window, text="Edit Task", command=self.edit_task).pack(pady=5)
        ttk.Button(self.window, text="Delete Task", command=self.delete_task).pack(pady=5)

        # 为任务列表添加滚动条
        scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=self.tasks_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.tasks_list.configure(yscrollcommand=scrollbar.set)

    # 从 CSV 文件加载任务
    def load_tasks(self):
        try:
            with open(self.tasks_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                return [tuple(row) for row in reader if len(row) == 4]
        except FileNotFoundError:
            return []
        except Exception as e:
            ttk.messagebox.showerror("Error", f"Failed to load tasks: {e}")
            return []

    def update_tasks_display(self):
        self.tasks_list.delete(*self.tasks_list.get_children())

        # 删除过期的任务并检查任务格式
        self.tasks = [task for task in self.tasks if
                      len(task) == 4 and datetime.strptime(task[2], "%Y-%m-%d %H:%M:%S") > datetime.now()]

        for task in self.tasks:
            if len(task) == 4:  # 确保每个任务都有四个元素
                publisher, task_description, deadline, publish_time = task
                remaining_time_str = self.calculate_remaining_time(deadline)
                self.tasks_list.insert('', tk.END,
                                       values=(publisher, task_description, remaining_time_str, publish_time))

    # 计算任务的剩余时间
    def calculate_remaining_time(self, deadline_str):
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M:%S")
        remaining_time = deadline - datetime.now()
        # 如果剩余时间大于0，返回剩余时间，否则返回“Time's up”
        if remaining_time.total_seconds() > 0:
            return str(remaining_time).split('.')[0]  # 去除毫秒部分
        else:
            return "Time's up"


    def publish_task(self):
        # 从发布人的输入框获取文本，并去除首尾空格
        publisher = self.publisher_entry.get().strip()

        # 从任务描述的文本区域获取文本，并去除首尾空格
        task_description = self.task_description_entry.get("1.0", tk.END).strip()

        # 检查发布人和任务描述是否都已填写，如果有任一为空，显示警告框并终止函数
        if not publisher or not task_description:
            ttk.messagebox.showwarning("Warning", "Please fill in all fields")
            return

        # 从单选按钮变量获取倒计时时长
        duration_hours = self.duration_var.get()

        # 如果发布人和任务描述都已填写
        if task_description and publisher:
            # 获取当前时间作为发布时间
            publish_time = datetime.now()

            # 将发布时间格式化为字符串
            publish_time_str = publish_time.strftime("%Y-%m-%d %H:%M:%S")

            # 根据用户选择的倒计时时长，计算任务的截止时间
            deadline = publish_time + timedelta(hours=duration_hours)

            # 将截止时间格式化为字符串
            deadline_str = deadline.strftime("%Y-%m-%d %H:%M:%S")

            # 创建新任务元组
            new_task = (publisher, task_description, deadline_str, publish_time_str)

            # 添加新任务到任务列表并保存
            self.tasks.append(new_task)
            self.save_task(*new_task)  # 正确解构元组以传递给 save_task

            self.task_description_entry.delete("1.0", tk.END)  # 清空任务描述输入区域
            self.update_tasks_display()



    # 将新任务保存到 CSV 文件
    def save_task(self, publisher, task_description, deadline, publish_time):
        with open(self.tasks_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([publisher, task_description, deadline, publish_time])

    # 更新任务的剩余时间显示
    def update_remaining_time(self):
        # 更新任务列表
        self.update_tasks_display()
        # 每分钟调用一次自身，以更新剩余时间
        self.window.after(60000, self.update_remaining_time)
        # 删除过期的任务
        self.tasks = [task for task in self.tasks if datetime.strptime(task[2], "%Y-%m-%d %H:%M:%S") > datetime.now()]

    def edit_task(self):
        # 获取当前选中的任务项
        selected_item = self.tasks_list.selection()
        if selected_item:
            # 获取选中任务的详细信息
            task_values = self.tasks_list.item(selected_item, "values")

            # 创建一个新的顶层窗口用于编辑任务
            edit_window = ttk.Toplevel(self.window)
            edit_window.title("Edit Task")

            # 添加标签和输入框用于编辑发布人
            ttk.Label(edit_window, text="Publisher:").pack(pady=5)
            publisher_entry = ttk.Entry(edit_window, width=50)
            publisher_entry.insert(0, task_values[0])
            publisher_entry.pack(pady=5)

            # 添加标签和文本框用于编辑任务描述
            ttk.Label(edit_window, text="Task Description:").pack(pady=5)
            task_description_entry = ttk.Text(edit_window, height=5, width=50)
            task_description_entry.insert("1.0", task_values[1])
            task_description_entry.pack(pady=10)

            # 添加按钮用于保存更改
            ttk.Button(edit_window, text="Save Changes",
                       command=lambda: self.save_edited_task(selected_item, publisher_entry, task_description_entry,
                                                             task_values[2], task_values[3])).pack(pady=10)

    def save_edited_task(self, item, publisher_entry, task_description_entry, deadline, publish_time):
        new_publisher = publisher_entry.get()
        new_task_description = task_description_entry.get("1.0", tk.END).strip()

        if new_publisher and new_task_description:
            # 更新视图中的任务
            self.tasks_list.item(item, values=(new_publisher, new_task_description, deadline, publish_time))

            # 查找并更新 self.tasks 中的相应任务
            for i, task in enumerate(self.tasks):
                if task[2] == deadline and task[3] == publish_time:
                    self.tasks[i] = (new_publisher, new_task_description, deadline, publish_time)
                    break

            # 更新 CSV 文件
            self.update_csv_file()

    def delete_task(self):
        selected_item = self.tasks_list.selection()
        if selected_item:
            # 获取要删除的任务信息
            task_values = self.tasks_list.item(selected_item, "values")

            # 从视图中删除任务
            self.tasks_list.delete(selected_item)

            # 从 self.tasks 中删除任务
            self.tasks = [task for task in self.tasks if not (task[2] == task_values[2] and task[3] == task_values[3])]

            # 更新 CSV 文件
            self.update_csv_file()

    def update_csv_file(self):
        # 使用 'w' 模式打开文件，确保覆盖原有内容
        with open(self.tasks_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # 遍历更新后的 self.tasks 列表，将每个任务写入文件
            for task in self.tasks:
                writer.writerow(task)
