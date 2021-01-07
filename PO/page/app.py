from appium import webdriver

from PO.page.base_page import BasePage
from PO.page.main_page import mainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:62001"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps["ensureWebviewsHavePages"]= True
            caps['dontStopAppOnReset'] = 'true' # 启动之前不停止app
            caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        else:
            self.driver.launch_app()

        self.driver.implicitly_wait(5)


    def goto_main(self):
        return mainPage(self.driver)