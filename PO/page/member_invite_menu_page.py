from appium.webdriver.common.mobileby import MobileBy

from PO.page.base_page import BasePage
from PO.page.contact_add_page import ContactAdd


class MemberInviteMenuPage(BasePage):
    """
    添加成员

    """

    def goto_contactAddPage(self):
        """
        跳转到成员信息录入
        :return:
        """
        #todo 点击手动添加页面
        self.find_and_click(MobileBy.XPATH,"//*[@text='手动输入添加' ]")
        return ContactAdd(self.driver)