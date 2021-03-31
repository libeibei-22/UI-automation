# -*- coding: utf-8 -*-

from src.common import basepage
from appium.webdriver.common import mobileby
import time

class startpage(basepage.Base_page):
    by=mobileby.MobileBy()
    '''包含启动页，开屏广告，插屏广告，个性化选择页'''
    enterbtn=(by.ID,"com.shinyv.cnr:id/btn_enter")  #启动图，进入app按钮
    skipbtn=(by.ID,"com.shinyv.cnr:id/skip_btn")  #启动图，跳过按钮
    jumpbtn=(by.ID,"com.shinyv.cnr:id/jump_tv")  #个性话选择页，跳过按钮
    adskipbtn=(by.ID,"com.shinyv.cnr:id/delet")  #开屏广告，跳过按钮
    adskipbtn2=(by.ID,"com.shinyv.cnr:id/iv_close") #插屏广告，关闭按钮
    ad2view=(by.ID,"com.shinyv.cnr:id/iv_ad")  #插屏广告view

    def click_enterbtn(self):
        self.find_element(*self.enterbtn).click()

    def click_skipbtn(self):
        self.find_element(*self.skipbtn).click()

    def click_jumpbtn(self):
        self.find_element(*self.jumpbtn).click()

    def click_adskipbtn(self):
        self.find_element(*self.adskipbtn).click()

    def click_adskipbtn2(self):
        self.find_element(*self.adskipbtn2).click()
    def click_ad2view(self):
        self.find_element(*self.ad2view).click()
    def get_ad2view_status(self):
        return self.find_element(*self.ad2view).is_displayed()






