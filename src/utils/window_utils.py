"""
窗口工具函数
包含窗口居中、样式配置等实用功能
"""
from typing import Any


def center_window(window: Any, width: int, height: int) -> None:
    """
    将窗口居中显示
    
    Args:
        window: tkinter或ttkbootstrap窗口对象
        width: 窗口宽度
        height: 窗口高度
    """
    # 获取屏幕尺寸
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 计算居中位置
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)

    # 设置窗口位置和大小
    window.geometry(f'{width}x{height}+{x}+{y}')


def configure_styles() -> dict:
    """
    配置常用的样式
    
    Returns:
        样式配置字典
    """
    return {
        'title_font': ('Bradley Hand ITC', 20),
        'normal_font': ('Helvetica', 12),
        'large_font': ('Helvetica', 16),
        'small_font': ('Helvetica', 10)
    }


def create_notice_window(parent_window: Any, title: str, message: str) -> None:
    """
    创建通知窗口
    
    Args:
        parent_window: 父窗口
        title: 窗口标题
        message: 通知消息
    """
    import ttkbootstrap as ttk
    
    notice_window = ttk.Toplevel(parent_window)
    center_window(notice_window, 320, 300)
    notice_window.title(title)
    
    ttk.Label(notice_window, text=message).grid(row=0, column=0, pady=10, padx=10, sticky='nsew')
    close_button = ttk.Button(notice_window, text="Close", bootstyle="danger", 
                             command=notice_window.destroy)
    close_button.grid(row=1, column=0, pady=10)
