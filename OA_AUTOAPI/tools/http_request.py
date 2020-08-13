import requests

from tools.my_log import MyLog

my_logger=MyLog()
class HttpRequest():
    def http_request(self,url,data,method,cookie=None,header=None):
        try:
            if method.upper() == 'GET':
                res = requests.get(url, params=data, cookies=cookie, headers=header)
            elif method.upper() == 'POST':
                res = requests.post(url=url, data=data, cookies=cookie, headers=header)
            else:
                my_logger.info("请求方法出错")
        except Exception as e:
            my_logger.error("请求出错了：{0}".format(e))
            raise e
        else:
            return res
