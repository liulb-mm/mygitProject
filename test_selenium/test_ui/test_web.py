from selenium import webdriver


class TestAuto:
    def test_setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)

    def test_case(self):
