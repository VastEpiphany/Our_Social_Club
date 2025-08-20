"""
Our Social Club - 主程序入口
重构后的社交俱乐部应用程序

运行此文件启动应用程序
"""
import sys
import os

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.views.login_window import LoginWindow


def main():
    """主函数"""
    try:
        # 创建并显示登录窗口
        login_window = LoginWindow()
        login_window.show()
    except Exception as e:
        print(f"应用程序启动失败: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
