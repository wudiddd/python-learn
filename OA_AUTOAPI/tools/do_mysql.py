import pymysql
import os
from tools.read_config import ReadConfig
from conf.project_path import test_config_path

db_data = ReadConfig().read_config_section(os.path.join(test_config_path,"case.config"),"DB")
class DB():
    def connect_mysql(self):
        connect = pymysql.connect(
            host = db_data['host'],
            user = db_data['user'],
            password = db_data['password'],
            port = int(db_data['port']),
            database = db_data['database'],
            charset = db_data['charset']
        )
        return connect

    def do_mysql(self,sql,state='all',mode='query'):
        connect = self.connect_mysql()
        cursor = connect.cursor()
        cursor.execute(sql)
        if mode != 'query':
            connect.commit()
        if state == "one":
            res = cursor.fetchone() #元组
        else:
            res = cursor.fetchall() #列表嵌套元组

        cursor.close()
        connect.close()
        return res


if __name__ == '__main__':
    sql = "select * from menu where menu_name='系统管理'"
    data = DB().do_mysql(sql,"one")
    print(data)
