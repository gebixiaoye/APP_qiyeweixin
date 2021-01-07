from PO.page.app import App


class Test_case:


    def test_add_member(self):
        main = App()
        main.start()
        res = main.goto_main().goto_addressListpage().click_addmember().goto_contactAddPage().add_contact()
        # print(res)
        # assert "添加成功" in res