# -*- coding: utf-8 -*-

from src.common import basepage
from appium.webdriver.common import mobileby
import time
class login_page(basepage.Base_page):
    by=mobileby.MobileBy()
    enloginpassword=(by.ID,"com.shinyv.cnr:id/right_txt1") #密码登录入口
    phoneinput=(by.ID,"com.shinyv.cnr:id/login_user_edit") #手机号输入框
    passwordinput=(by.ID,"com.shinyv.cnr:id/login_password_edit") #密码输入框
    loginbutton=(by.ID,"com.shinyv.cnr:id/login_btn") #登录按钮
    ''' 点击账号密码登录入口'''
    def click_enloginpassword(self):
        self.find_element(*self.enloginpassword).click()
    def input_phoneinput(self,phonenumber):
        self.send_keys(phonenumber,*self.phoneinput)
    def input_password(self,password):
        self.send_keys(password,*self.passwordinput)
    '''点击登录按钮'''
    def click_login(self):
        self.find_element(*self.loginbutton).click()
    #手机号密码登录
    def login(self,phone,password):
        self.click_enloginpassword()
        time.sleep(3)
        self.input_phoneinput(phone)
        self.input_password(password)
        self.click_login()



