import pymysql
from conf.project_path import test_config_path
from tools.read_config import ReadConfig
from tools.my_log import MyLog

#返回字典
db_data = ReadConfig().read_config_as_section(test_config_path,"DB")
class DB():
    # @staticmethod
    def connect_mysql(self):
        #配置从配置文件中读
        con = pymysql.connect(
            host = db_data['host'],
            user = db_data['user'],
            password = db_data['password'],
            port = int(db_data['port']),
            database = db_data['database'],
            charset = db_data['charset']

        )
        return con

    #查询操作
    def do_sql(self,sql,state='all',mode = 'query'):
        '''

        :param sql:
        :param state: 返回多条还是单挑
        :param mode: 查询还是其他操作，查询不需要commit，其他操作需要
        :return:
        '''
        #创建游标
        cursor = self.connect_mysql().cursor()
        #写sql语句
        MyLog().info(f"执行sql语句：{sql}")
        cursor.execute(sql)
        res = None
        if state == 'all':
            res = cursor.fetchall() #返回列表嵌套元组，多条数据
        if state == 1:
            res = cursor.fetchone()
        if mode is not 'query':
            self.connect_mysql().commit()
        #关闭游标
        cursor.close()
        #关闭连接
        self.connect_mysql().close()
        MyLog().info(f"执行完成sql语句，返回为：{res}")
        if res is not None:
            res = res[0]
        return res

if __name__ == '__main__':
    menu_name = ReadConfig().read_config_as_section(test_config_path, "menu")['menu_name']
    print(menu_name)
    sql = f"select menu_id from menu where menu_name = '{menu_name}'"
    res = DB().do_sql(sql, 1)
    print(res)