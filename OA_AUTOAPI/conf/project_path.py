import os

#当前项目路径
project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
#配置文件路径
test_config_path = os.path.join(project_path,"conf")
#测试数据路径
test_data_path = os.path.join(project_path,"test_data")
#测试报告路径
test_report_path = os.path.join(project_path,"report")
#日志文件路径
test_log_path = os.path.join(project_path,"log")




if __name__ == '__main__':
    pass