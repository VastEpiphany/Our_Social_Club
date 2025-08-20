"""
应用程序配置
"""
import os

class Config:
    """应用程序配置类"""
    
    # 基础路径
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    
    # 数据目录
    DATA_DIR = os.path.join(BASE_DIR, "data")
    
    # 资源目录
    ASSETS_DIR = os.path.join(BASE_DIR, "assets")
    
    # 数据文件路径
    USER_FILE = os.path.join(DATA_DIR, "User_file.csv")
    USER_INFO_FILE = os.path.join(DATA_DIR, "User_info.csv")
    BLACKBOARD_FILE = os.path.join(DATA_DIR, "blackboard_messages.csv")
    
    # 图片文件路径
    BACKGROUND_IMAGE = os.path.join(ASSETS_DIR, "Background.jpg")
    MAIN_GUI_BACKGROUND = os.path.join(ASSETS_DIR, "Main_GUI_Background.png")
    SMILE_IMAGE = os.path.join(ASSETS_DIR, "Smile.jpg")
    
    # 窗口配置
    DEFAULT_WINDOW_SIZE = (1300, 900)
    LOGIN_WINDOW_SIZE = (1300, 900)
    DIALOG_WINDOW_SIZE = (400, 300)
    
    # 主题配置
    DEFAULT_THEME = 'flatly'
    MAIN_THEME = 'journal'
    
    # 字体配置
    FONTS = {
        'title': ('Bradley Hand ITC', 20),
        'normal': ('Helvetica', 12),
        'large': ('Helvetica', 16),
        'small': ('Helvetica', 10)
    }
