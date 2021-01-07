from PO.page.base_page import BasePage
from PO.page.member_invite_menu_page import MemberInviteMenuPage


class addressListPage(BasePage):
    """
        通讯录页面
    """

    def click_addmember(self):
        """
        添加成员
        :return:
        """
        self.scroll_find_click("添加成员")

        return MemberInviteMenuPage(self.driver)