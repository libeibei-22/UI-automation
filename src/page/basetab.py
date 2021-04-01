# -*- coding: utf-8 -*-

from src.common import basepage
from appium.webdriver.common import mobileby
import time
class login_page(basepage.Base_page):
    by=mobileby.MobileBy()
    firsttab = (by.ID, "com.shinyv.cnr:id/tab_1_parent")  # 听精品tab
    livetab = (by.ID, "com.shinyv.cnr:id/tab_2_parent")  # 听广播tab
    tvtab = (by.ID, "com.shinyv.cnr:id/tab_3_parent")  # 听电视tab
    mytab=(by.ID,"com.shinyv.cnr:id/tab_4_parent") #我的tab
    playbtn=(by.ID,"com.shinyv.cnr:id/play_btn")  #悬浮球播放器

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


