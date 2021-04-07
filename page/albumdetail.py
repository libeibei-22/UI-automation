# -*- coding: utf-8 -*-

from common import base_method
from appium.webdriver.common import mobileby

class albumdetail(base_method.Base_page):
    by=mobileby.MobileBy()
    firstsong=(by.XPATH,"//android.view.ViewGroup[1]")

    def selectfirstsong(self):
        self.find_element(*self.firstsong).click()

