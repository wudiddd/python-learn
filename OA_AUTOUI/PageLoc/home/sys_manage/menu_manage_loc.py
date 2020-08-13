from selenium.webdriver.common.by import By
from tools.read_config import ReadConfig
from tools.do_mysql import DB
from tools.my_log import MyLog
from conf.project_path import test_config_path

class Dy_para():
    def dele_menu_but(self):

        menu_name = ReadConfig().read_config_as_section(test_config_path, "menu")['menu_name']
        sql = f"select menu_id from menu where menu_name = '{menu_name}'"
        menu_id = DB().do_sql(sql, 1)
        #这个引号嵌套不好写，写不顺
        # del_but = "(By.XPATH,'//td[@class=\"\'menuid\'\"][text()=f\"\'{menu_id}\'\"]/../td/a[contains(@href,\"\'delete\'\")]')"
        # MyLog().info(f"del_but是{del_but}")
        return menu_id

class MenuManage():
    #菜单管理
    menu_manage_loc = (By.XPATH,'//span[text()="菜单管理"]//..//../a')
    #菜单管理iframe
    menu_manage_frame = (By.XPATH,'//iframe[contains(@src,"/menu")]')

    #新增按钮,有两个
    add_but = (By.XPATH,'//a[@href="menuedit"]')
    #名称输入框
    name_input = (By.XPATH,'//input[@name="menuName"]')
    #路径输入框
    url_input = (By.XPATH,'//input[@name="menuUrl"]')
    #排序输入框
    sort_input = (By.XPATH, '//input[@name="sortId"]')
    #保存按钮
    save_but = (By.XPATH,'//input[@id="save"]')
    #取消按钮
    cancel_but = (By.XPATH,'//input[@id="cancel"]')

    #删除菜单按钮，先根据数据库id查询到某个项，再删除
    # menu_sele = (By.XPATH,f'//td[@class="menuid"][text()="{menuid}"]')
    #要删除的菜单,这个menuid怎么处理，目前只能想到的笨处理，再配置文件中配置mennu的名字
    # dele_menu_but = (
    # By.XPATH, f'//td[@class="menuid"][text()="{Dy_para().dele_menu_but()}"]/../td/a[contains(@href,"delete")]')
    dele_menu_but = (By.XPATH,f'//td[@class="menuid"][text()="{Dy_para().dele_menu_but()}"]/../td/a[contains(@href,"delete")]')



if __name__ == '__main__':
    a = 123
    print(a)