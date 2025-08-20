"""
公告板组件
学生公告板功能
"""
import csv
import os
import ttkbootstrap as ttk


class BlackBoard:
    """公告板类"""
    
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.messages_file = os.path.join("data", "blackboard_messages.csv")
        self._ensure_data_file()
        self._setup_ui()
        self._load_messages()

    def _ensure_data_file(self) -> None:
        """确保数据文件存在"""
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(self.messages_file):
            with open(self.messages_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['message', 'timestamp'])

    def _setup_ui(self) -> None:
        """设置用户界面"""
        # 标题
        self.title_label = ttk.Label(
            self.parent_frame, 
            text="学生公告板", 
            font=('Bradley Hand ITC', 16)
        )
        self.title_label.pack()

        # 消息显示区域
        self.messages_text = ttk.Text(self.parent_frame, height=10, width=50)
        self.messages_text.pack()

        # 输入框
        self.input_text = ttk.Entry(self.parent_frame, width=50)
        self.input_text.pack(pady=5)
        
        # 绑定回车键
        self.input_text.bind("<Return>", lambda event: self._add_message())

        # 提交按钮
        self.submit_button = ttk.Button(
            self.parent_frame, 
            text="提交消息", 
            command=self._add_message
        )
        self.submit_button.pack()

    def _add_message(self) -> None:
        """添加消息"""
        message = self.input_text.get().strip()
        if message:
            # 添加到显示区域
            self.messages_text.insert(ttk.END, f"{message}\n")
            self.messages_text.see(ttk.END)  # 滚动到最底部
            
            # 清空输入框
            self.input_text.delete(0, ttk.END)
            
            # 保存到文件
            self._save_message(message)

    def _save_message(self, message: str) -> None:
        """保存消息到文件"""
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(self.messages_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([message, timestamp])

    def _load_messages(self) -> None:
        """加载历史消息"""
        try:
            with open(self.messages_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # 跳过标题行
                for row in reader:
                    if row:  # 确保行不为空
                        message = row[0]
                        self.messages_text.insert(ttk.END, f"{message}\n")
        except FileNotFoundError:
            pass  # 文件不存在时不做任何操作
