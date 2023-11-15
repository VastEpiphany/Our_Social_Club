def center_window(win, width, height):
    """
    该函数用于计算并设置窗口中心位置，需要与tkinter或ttk共同配合使用
    :param win: window窗口，即为tkinter的root操作对象
    :param width: 目标设置宽度
    :param height: 目标设置高度
    :return: 无需返回，函数直接操作设置
    """
    # 获取屏幕尺寸
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # 计算 x, y 位置
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)

    # 设置窗口位置
    win.geometry(f'{width}x{height}+{x}+{y}')