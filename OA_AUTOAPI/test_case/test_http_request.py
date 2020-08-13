import pytest
import os

from conf import project_path
from tools.my_log import MyLog
from tools.http_request import HttpRequest
from tools.get_cookies import GetCookies
from tools.read_excel import ReadExel

my_logger = MyLog()

login_path = os.path.join(project_path.test_data_path,"test.xlsx")
@pytest.mark.usefixtures("login_data")
class TestHttpRequest():
    # data = []
    # data.append(ReadExel(login_path).get_data())
    data = ReadExel(login_path).get_data()
    @pytest.mark.parametrize("login_data",data,indirect=True)

    def test_api(self,login_data):
        #登录
        res = HttpRequest().http_request(login_data["url"],eval(login_data["data"]), login_data["method"], getattr(GetCookies, "COOKIES"),getattr(GetCookies, "headers"))
        my_logger.info("响应的html代码是：{}".format(res.text))
        test_result = None
        if res.cookies:
            setattr(GetCookies,"COOKIES",res.cookies)
            print(getattr(GetCookies,"COOKIES"))

        try:
            assert 200 == res.status_code
            # assert login_data["expected"] ==
            test_result = 'PASS'
            my_logger.info("执行用例通过")
        except AssertionError as e:
            test_result = "Failed"
            my_logger.error("执行用例出错：{0}".format(e))
            raise e
        finally:
            ReadExel(login_path).write_data(int(login_data["case_id"])+1,login_data["sheet_name"],res.status_code,test_result)
            my_logger.info("获取到的结果是：{}".format(res.status_code))
