from selenium.webdriver.remote.webdriver import WebDriver

from PageLoc.home_page_menu_loc import MenuLoc as menuloc
from PageLoc.home.sys_manage.menu_manage_loc import MenuManage as menu
from base_page import BasePage
from tools.my_log import MyLog


class MenuManagement():
    def __init__(self,driver:WebDriver):
        self.b = BasePage(driver)
    def in_menu_manage(self):
        self.b.click(menuloc.sys_manage)
        self.b.click(menu.menu_manage_loc)
        self.b.switch_frame(menu.menu_manage_frame)

    def add_menu(self,name,url,sort):
        self.in_menu_manage()
        self.b.click(menu.add_but)
        self.b.send_keys(menu.name_input,name)
        self.b.send_keys(menu.url_input,url)
        self.b.send_keys(menu.sort_input,sort)
        self.b.click(menu.save_but)

    def delete_menu(self):
        self.b.refresh()#刷新
        self.in_menu_manage()
        MyLog().info(f"按钮位置:{menu.dele_menu_but}")
        self.b.click(menu().dele_menu_but)
        self.b.accept_alert()

