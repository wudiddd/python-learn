import logging
from conf import project_path

class MyLog():
    def my_log(self,msg,level):
        #定义日志收集器，
        my_logger = logging.getLogger("my_logger")
        #设定默认级别
        my_logger.setLevel("DEBUG")
        #设定输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        #创建一个输出渠道
        #控制台输出
        ch = logging.StreamHandler()
        ch.setLevel("DEBUG")
        ch.setFormatter(formatter)

        #文件输出
        fh = logging.FileHandler(project_path.log_path,encoding='utf-8')
        fh.setLevel("DEBUG")
        fh.setFormatter(formatter)

        #对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        # 收集日志
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'ERROR':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)
        # 关闭日志收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def warning(self, msg):
        self.my_log(msg, 'WARNING')

    def error(self, msg):
        self.my_log(msg, 'ERROR')

    def critical(self, msg):
        self.my_log(msg, 'CRRTICAL')
