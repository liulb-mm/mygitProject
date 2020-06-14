from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWebdriver:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.testerhome.com")
        self.driver.implicitly_wait(10)
        self.driver.switch_to.window()

    def test_case(self):
        self.driver.find_element(By.LINK_TEXT,"MTSC2020 中国互联网测试开发大会议题征集").click()
