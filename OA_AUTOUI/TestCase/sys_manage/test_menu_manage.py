import pytest

from PageObj.home.sysmanage.menu_manage import MenuManagement
from tools.do_mysql import DB
from PageObj.login_page import LoginPage
from tools.read_config import ReadConfig
from conf.project_path import test_config_path


# @pytest.mark.usefixtures("in_web")
@pytest.mark.usefixtures("login")
# @pytest.mark.smoke
class TestMenuManage():
    #要先登录,传参需要用@pytest.mark.parametrize传参
    # parame = [{"name":"测试","url":"/test","sort":"3"},]
    @pytest.mark.parametrize("name,url,sort",[("测试","/test","3")])
    def test_add_menu(self,login,name,url,sort):
        '''
        :param AccessBrowser: fixture返回的值，就是driver
        :param name:
        :param url:
        :param sort:
        :return:
        '''
        #这里不知道能不能复用之前的登录成功用例。直接设置了一个login的fixture使用
        # LoginPage(AccessBrowser).login("yang","123456","abcd")
        MenuManagement(login).add_menu(name,url,sort)
        #里面参数name要用冒号包裹，传值过来的时候只有字符，没有冒号，要自己加冒号
        sql = f"select menu_url from menu where menu_name = '{name}'"
        res = DB().do_sql(sql, 1)
        # 返回是个元组,即('/test',),如果是all的话，返回就是元组嵌套元组，即(('/test',),)
        assert url == res[0]

    def test_dele_menu(self,login):
        # LoginPage(AccessBrowser).login("yang", "123456", "abcd")
        #删除菜单并没有真正的删除，知识将parentid改为999
        MenuManagement(login).delete_menu()
        menu_name = ReadConfig().read_config_as_section(test_config_path, "menu")['menu_name']
        sql = f"select parent_id from menu where menu_name = '{menu_name}'"
        parent_id = DB().do_sql(sql, 1)
        #不知道为什么返回不是999，而是原来的值，再执行一次才会改变
        assert parent_id[0] == 999
