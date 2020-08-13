import os

'''读取路径的值'''
#项目路径：D:\pycharm\projects\OA_AUTOUI
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#测试数据路径
test_data_path = os.path.join(project_path,"TestData")
#配置文件路径
test_config_path = os.path.join(project_path,"conf","config.config")
#日志路径
log_path = os.path.join(project_path,"report","log","log.txt")
#截图路径
img_path = os.path.join(project_path,"report","image")
if __name__ == '__main__':
    print(project_path)