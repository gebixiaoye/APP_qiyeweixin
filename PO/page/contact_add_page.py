from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from PO.page.base_page import BasePage


class ContactAdd(BasePage):

    """
    成员信息编辑
    """


    def add_contact(self):
        """
        跳转到成员信息录入
        :return:
        """
        # todo

        self.find_send(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/..//*[@text='必填']","aaaaaa")

        self.find_and_click(MobileBy.XPATH,
                                 "//*[contains(@text,'性别')]/..//*[@text='男']")

        self.wait_for(MobileBy.XPATH,"//*[@text='女']")


        self.find_and_click(MobileBy.XPATH,"//*[@text='女']")
        self.find_send(MobileBy.XPATH,
                                 "//*[contains(@text,'手机')]/..//*[@text='手机号']","13711111112")

        self.find_and_click(MobileBy.XPATH,"//*[@text='保存']")

        sleep(1)

        return self.driver.page_source