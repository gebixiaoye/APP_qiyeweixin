from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self,driver:WebDriver = None):
        self.driver = driver


    def find(self,by,locator):
        return self.driver.find_element(by,locator)

    def find_and_click(self,by,locator):
        return self.driver.find_element(by,locator).click()

    def scroll_find(self,text):
        #滚动查找
        return self.driver.find_element(MobileBy.
                                         ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().'
                                                             'scrollable(true).instance(0)).'
                                                             'scrollIntoView(new UiSelector().'
                                                             f'text("{text}").instance(0));')

    def scroll_find_click(self, text):
        # 滚动查找
        return self.scroll_find(text).click()

    def find_send(self,by,locator,text):
        return self.find(by,locator).send_keys(text)

    def wait_for(self,by,locator):
        def wait_ele_for(driver:WebDriver):
            eles = driver.find_elements(by,locator)
            return len(eles) > 0

        return WebDriverWait(self.driver,10).until(wait_ele_for)