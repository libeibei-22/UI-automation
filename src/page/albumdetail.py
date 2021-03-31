# -*- coding: utf-8 -*-

from src.common import basepage
from appium.webdriver.common import mobileby

class albumdetail(basepage.Base_page):
    by=mobileby.MobileBy()
    firstsong=(by.XPATH,"//android.view.ViewGroup[1]")

    def selectfirstsong(self):
        self.find_element(*self.firstsong).click()

