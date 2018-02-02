from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Base():
    def __init__(self,driver):
        self.driver = driver
    def find_element(self,loc,timeout=10,pult=0.5):
        '''

        :param loc: loc 为元组类型，格式(By.xx，xx属性值）
        :param timeout: 为最长等待时间
        :param pult: 多长时间定位一次
        :return: 返回值
        '''
        return WebDriverWait(self.driver,timeout,pult).until(lambda x: x.find_element(*loc))
    def click_element(self,loc):
        '''

        :param loc: 为find_element的loc,
        :return:
        '''
        self.find_element(loc).click()

    def send_element(self,loc,text):
        el = self.find_element(loc)
        el.clear()
        el.send_keys(text)