# -*- coding: utf-8 -*-

from common import basepage
from appium.webdriver.common import mobileby
import time
import yaml

class login_page(basepage.Base_page):
    with open('D:/android-sdk_r24.4.1-windows/android-sdk-windows/tools/untitled/data/login.yaml', 'r',
              encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
    by = mobileby.MobileBy()
    enloginpassword=(by.ID,result["enloginpassword"]) #密码登录入口
    phoneinput=(by.ID,result["phoneinput"]) #手机号输入框
    passwordinput=(by.ID,result["passwordinput"]) #密码输入框
    loginbutton=(by.ID,result["loginbutton"]) #登录按钮

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
    '''手机号密码登录'''
    def login(self,phone,password):
        self.click_enloginpassword()
        time.sleep(3)
        self.input_phoneinput(phone)
        self.input_password(password)
        self.click_login()



