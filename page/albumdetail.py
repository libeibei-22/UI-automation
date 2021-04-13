# -*- coding: utf-8 -*-
'''
封装专辑详情页

'''
from common import base_method
from appium.webdriver.common import mobileby
import yaml
class albumdetail(base_method.Base_page):
    by=mobileby.MobileBy()
    with open(base_method.Base_page.data_save_address+'/element', 'r', encoding='utf-8') as f:
        result=yaml.load(f.read(),Loader=yaml.FullLoader)["albumdetail"]
    firstsong=result["songlist"]
    albumname=(by.ID,result["albumname"]) #专辑名称

    def selectsong(self, songname):
        songnamestr="'"+songname+"'"
        songnamenew=(self.by.XPATH, self.firstsong+ "[@text={}]".format(songnamestr))
        self.find_element(*songnamenew).click()
    def albumName_get(self):
        return self.find_element(*self.albumname).text

