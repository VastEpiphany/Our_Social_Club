import tkinter as tk
import ttkbootstrap as ttk
from Center_window import center_window
from ttkbootstrap.constants import *

class PersonalizationSettings:
    def __init__(self, parent):
        self.parent = parent  # 保存父窗口引用
        self.create_settings_window()  # 创建个性设置窗口

    def create_settings_window(self):
        self.settings_window = ttk.Toplevel(self.parent)
        self.settings_window.title("Personalization Settings")
        #self.settings_window.geometry("300x500")
        center_window(self.settings_window,300,500)

        # 字体大小选项
        ttk.Label(self.settings_window, text="Font Size:").pack(pady=5)
        self.font_size_var = tk.StringVar(value="12")
        ttk.Combobox(self.settings_window, textvariable=self.font_size_var, values=["10", "12", "14", "16", "18"]).pack(pady=5)

        # 字体颜色选项
        ttk.Label(self.settings_window, text="Font Color:").pack(pady=5)
        self.font_color_var = tk.StringVar(value="black")
        ttk.Combobox(self.settings_window, textvariable=self.font_color_var, values=["black", "red", "blue", "green"]).pack(pady=5)


        # 应用设置按钮
        ttk.Button(self.settings_window, text="Apply Settings", command=self.apply_settings).pack(pady=10)


    def apply_settings(self):
        # 应用用户选择的设置
        font_size = self.font_size_var.get()
        font_color = self.font_color_var.get()

        # 示例：根据设置改变样式
        style = ttk.Style()
        style.configure('.', font=('Helvetica', int(font_size)), foreground=font_color)  # 更新字体大小和颜色






