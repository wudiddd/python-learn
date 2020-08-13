from selenium.webdriver.common.by import By

class LoginPageLoc():
    #用户名输入框
    user_input = (By.NAME,"userName")
    # 密码输入框
    psw_input = (By.NAME, "password")
    # 验证码输入框
    vec_input = (By.NAME, "code")
    #登录按钮
    login_but = (By.XPATH,"//form/div/button")
    #错误文本
    error_text = (By.XPATH,"//div[@role='alert']/span")