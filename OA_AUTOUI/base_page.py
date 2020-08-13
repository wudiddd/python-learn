from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf.project_path import img_path
import os
from tools.my_log import MyLog
import time

class BasePage():
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def find_element(self,loc):
        try:
            MyLog().info(f"查找元素{loc}")
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            MyLog().info(f"查找元素{loc}成功")
            ele = self.driver.find_element(*loc)
        except Exception as e:
            MyLog().error(u"出现的异常是%s"%e)
            #异常截图
            nowTime = time.strftime("%Y%m%d-%H-%M-%S")
            t = self.driver.get_screenshot_as_file(img_path+u'%s.jpg' % nowTime)
            #异常截图的路径
            MyLog().info(u"截图结果为：%s"%t)
        else:
            return ele


    def send_keys(self,loc,para):
        '''
        :param loc: 位置
        :param para: 从数据库读的可能为空，读出来为None
        :return:
        '''
        MyLog().info(f"清空{loc}的值")
        self.find_element(loc).clear()
        if(para == None):
            MyLog().info("从数据库读的值为空")
            self.find_element(loc).send_keys(" ")
        else:
            self.find_element(loc).send_keys(para)



    def click(self,loc):
        MyLog().info(f"点击元素{loc}")
        self.find_element(loc).click()

    def get_text(self, loc):
        MyLog().info(f"获取元素{loc}的值")
        text = self.find_element(loc).text
        MyLog().info(f"值为{text}")
        return text

    def switch_frame(self,loc):
        # MyLog().info(f"等待元素{loc}")
        # # WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(loc))
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        MyLog().info(f"准备进入iframe：{loc}")
        #括号里面应该是一个对象,不用再次等待
        self.driver.switch_to.frame(self.find_element(loc))

    def accept_alert(self):
        MyLog().info("进入确认alert")
        self.driver.switch_to.alert.accept()
    def refuse_alert(self):
        MyLog().info("进入取消alert")
        self.driver.switch_to.alert.dismiss()

    def refresh(self):
        MyLog().info("#########刷新##########")
        self.driver.refresh()