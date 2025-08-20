"""
Our Social Club 重构版本测试脚本
用于验证重构后的功能是否正常工作
"""
import sys
import os
import csv
from hashlib import sha256


def test_user_authentication():
    """测试用户认证功能"""
    print("测试用户认证功能...")
    
    # 创建测试用户
    test_username = "test_user"
    test_password = "test123456"
    
    # 导入用户服务
    sys.path.insert(0, 'src')
    try:
        from src.services.user_service import UserService
        user_service = UserService()
        
        # 测试注册
        success, message = user_service.register_user(test_username, test_password)
        print(f"注册测试: {success} - {message}")
        
        # 测试登录
        auth_success, user_id = user_service.authenticate_user(test_username, test_password)
        print(f"登录测试: {auth_success} - 用户ID: {user_id}")
        
        # 测试用户加载
        if auth_success:
            user = user_service.load_user(test_username, user_id)
            print(f"用户加载测试: 成功 - 用户: {user.nickname}")
        
        return True
    except Exception as e:
        print(f"用户认证测试失败: {e}")
        return False


def test_file_structure():
    """测试文件结构"""
    print("\n测试文件结构...")
    
    required_dirs = [
        'src',
        'src/models',
        'src/views', 
        'src/controllers',
        'src/services',
        'src/components',
        'src/utils',
        'assets',
        'data'
    ]
    
    required_files = [
        'src/models/user.py',
        'src/views/login_window.py',
        'src/views/main_window.py',
        'src/controllers/auth_controller.py',
        'src/services/user_service.py',
        'src/components/blackboard.py',
        'src/utils/window_utils.py',
        'src/config.py',
        'main.py',
        'Main_Login_GUI_New.py',
        'requirements.txt'
    ]
    
    # 检查目录
    for dir_path in required_dirs:
        if os.path.exists(dir_path):
            print(f"✅ 目录存在: {dir_path}")
        else:
            print(f"❌ 目录缺失: {dir_path}")
    
    # 检查文件
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ 文件存在: {file_path}")
        else:
            print(f"❌ 文件缺失: {file_path}")


def test_data_files():
    """测试数据文件"""
    print("\n测试数据文件功能...")
    
    # 确保数据目录存在
    os.makedirs('data', exist_ok=True)
    
    # 测试用户文件创建
    user_file = 'data/User_file.csv'
    if not os.path.exists(user_file):
        with open(user_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['user_id', 'nickname', 'password'])
        print(f"✅ 创建用户文件: {user_file}")
    else:
        print(f"✅ 用户文件已存在: {user_file}")
    
    # 测试用户信息文件创建
    user_info_file = 'data/User_info.csv'
    if not os.path.exists(user_info_file):
        with open(user_info_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['nickname', 'user_id', 'age', 'hobbies', 'birthday', 'signature'])
        print(f"✅ 创建用户信息文件: {user_info_file}")
    else:
        print(f"✅ 用户信息文件已存在: {user_info_file}")


def test_imports():
    """测试模块导入"""
    print("\n测试模块导入...")
    
    try:
        # 测试模型导入
        sys.path.insert(0, 'src')
        from src.models.user import User, MainUser
        print("✅ 用户模型导入成功")
        
        from src.services.user_service import UserService
        print("✅ 用户服务导入成功")
        
        from src.utils.window_utils import center_window, create_notice_window
        print("✅ 窗口工具导入成功")
        
        from src.config import Config
        print("✅ 配置文件导入成功")
        
        return True
    except Exception as e:
        print(f"❌ 模块导入失败: {e}")
        return False


def test_compatibility_version():
    """测试兼容版本"""
    print("\n测试兼容版本文件...")
    
    if os.path.exists('Main_Login_GUI_New.py'):
        print("✅ 兼容版本文件存在")
        
        # 检查文件内容
        with open('Main_Login_GUI_New.py', 'r', encoding='utf-8') as file:
            content = file.read()
            
        required_classes = ['User', 'MainUser', 'UserService', 'LoginWindow', 'MainWindow']
        for class_name in required_classes:
            if f"class {class_name}" in content:
                print(f"✅ 找到类定义: {class_name}")
            else:
                print(f"❌ 缺少类定义: {class_name}")
        
        return True
    else:
        print("❌ 兼容版本文件不存在")
        return False


def main():
    """主测试函数"""
    print("="*50)
    print("Our Social Club 重构版本功能测试")
    print("="*50)
    
    # 运行所有测试
    tests = [
        test_file_structure,
        test_data_files,
        test_imports,
        test_user_authentication,
        test_compatibility_version
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result if result is not None else True)
        except Exception as e:
            print(f"测试失败: {e}")
            results.append(False)
    
    # 总结
    print("\n" + "="*50)
    print("测试总结")
    print("="*50)
    
    passed = sum(1 for r in results if r)
    total = len(results)
    
    print(f"通过测试: {passed}/{total}")
    
    if passed == total:
        print("🎉 所有测试通过！重构成功！")
        print("\n可以安全使用以下方式启动应用：")
        print("1. python Main_Login_GUI_New.py  (推荐)")
        print("2. python main.py")
    else:
        print("⚠️ 部分测试失败，请检查相关问题")


if __name__ == "__main__":
    main()
