from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Cookie:
    def __init__(self):
        self.link="https://orteil.dashnet.org/cookieclicker/"
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
    def open(self):
        self.driver.get( self.link)
        time.sleep(2)
    def language(self):
        self.driver.find_element("id","langSelect-RU").click()
        time.sleep(20)
    def c_click(self):
        self.driver.find_element("id","bigCookie").click()

cookie=Cookie()
cookie.open()
cookie.language()
#options=webdriver.ChromeOptions()
#langSelect-RU
#bigCookie
while True:
    cookie.c_click()