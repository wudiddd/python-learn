from selenium.webdriver.common.by import By

class MenuLoc():
    #系统管理位置
    sys_manage = (By.XPATH,'//span[text()="系统管理"]//..//../a')
    #用户管理位置,有两个，选第一个为父菜单，第二个为子菜单
    user_manage = (By.XPATH,'//span[text()="用户管理"]//..//../a')
    # 角色列表,有两个，选第一个为父菜单，第二个为子菜单
    role_manage = (By.XPATH, '//span[text()="角色列表"]//..//../a')
    # 考勤管理位置,有两个，选第一个为父菜单，第二个为子菜单
    attend_manage = (By.XPATH, '//span[text()="考勤管理"]//..//../a')
    # 流程管理位置,
    project_manage = (By.XPATH, '//span[text()="流程管理"]//..//../a')
    # 邮件管理位置,有两个，选第一个为父菜单，第二个为子菜单
    mail_manage = (By.XPATH, '//span[text()="邮件管理"]//..//../a')
    # 任务管理位置,有两个，选第一个为父菜单，第二个为子菜单
    assign_manage = (By.XPATH, '//span[text()="任务管理"]//..//../a')

