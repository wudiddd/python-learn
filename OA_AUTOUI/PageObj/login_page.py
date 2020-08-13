from PageLoc.login_page_loc import LoginPageLoc as lp
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage

from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver

class LoginPage():
    def __init__(self,driver:WebDriver):
        self.b = BasePage(driver)
    def login(self,username,password,vec):
        # b = BasePage(driver)
        self.b.send_keys(lp.user_input,username)
        self.b.send_keys(lp.psw_input, password)
        self.b.send_keys(lp.vec_input, vec)
        self.b.click(lp.login_but)

    def error_msg(self):
        return self.b.get_text(lp.error_text)

if __name__ == '__main__':
    import time
    driver = webdriver.Chrome()
    driver.get("http://localhost:8089")
    driver.maximize_window()
    LoginPage(driver).login("yan"," 1"," ")
    # time.sleep(3)
    print(LoginPage(driver).error_msg())
    driver.quit()


