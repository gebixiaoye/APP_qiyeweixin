from appium.webdriver.common.mobileby import MobileBy

from PO.page.address_list_page import addressListPage
from PO.page.base_page import BasePage


class mainPage(BasePage):

    def goto_addressListpage(self):
        """
        跳转到通讯录
        :return:
        """
        self.find_and_click(MobileBy.XPATH,"//*[@text='通讯录' and @resource-id='com.tencent.wework:id/egd']")
        return addressListPage(self.driver)