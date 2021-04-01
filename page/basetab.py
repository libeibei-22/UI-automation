# -*- coding: utf-8 -*-

from common import basepage
from appium.webdriver.common import mobileby
import yaml
class basetab(basepage.Base_page):
    by=mobileby.MobileBy()
    with open('D:/android-sdk_r24.4.1-windows/android-sdk-windows/tools/untitled/data/basetab', 'r', encoding='utf-8') as f:
        result=yaml.load(f.read(),Loader=yaml.FullLoader)  #此处修改成本地路径哈哈
    firsttab=(by.ID,result["firsttab"])  #听精品tab
    livetab=(by.ID,result["livetab"])  #听广播tab
    tvtab=(by.ID,result["tvtab"])  #听电视tab
    mytab=(by.ID,result["mytab"]) #我的tab
    playbtn=(by.ID,result["playbtn"])  #悬浮球播放器

    '''点击听精品tab'''
    def click_firsttab(self):
        self.find_element(*self.firsttab).click()
    '''点击听广播tab'''
    def click_livetab(self):
        self.find_element(*self.livetab).click()
    '''点击听电视tab'''
    def click_tvtab(self):
        self.find_element(*self.tvtab).click()
    '''点击我的tab'''
    def click_mytab(self):
        self.find_element(*self.mytab).click()
    '''点击悬浮球'''
    def click_playbtn(self):
        self.find_element(*self.playbtn).click()


