from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
import pytest
from tools.read_config import ReadConfig
from conf.project_path import test_config_path
from tools.my_log import MyLog
from PageObj.login_page import LoginPage


driver:WebDriver = None
def common():
    global driver
    url = ReadConfig().read_config(test_config_path, "project", "url")
    # 启动浏览器前置
    MyLog().info("###########################")
    MyLog().info("启动浏览器")
    driver = webdriver.Chrome()
    MyLog().info(f"driver.get({url})")
    MyLog().info(type(url))
    driver.get(url)
    driver.maximize_window()


@pytest.fixture(scope="function")
def in_web():
    common()
    yield driver
    #函数后置
    MyLog().info("关闭浏览器")
    MyLog().info("############################")
    driver.quit()

@pytest.fixture()
def logins_data(request):
    param = request.param       #用来接收登录所用数据
    print(f"账号是：{param['username']},密码是：{param['password']},验证码是{param['code']}")
    return param

#前置登录
@pytest.fixture(scope="session")
def login():
    common()
    LoginPage(driver).login("yang", "123456", "abcd")
    yield driver
    # 类后置
    MyLog().info("关闭浏览器")
    MyLog().info("############################")
    driver.quit()



if __name__ == '__main__':
    common()
