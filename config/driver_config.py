# -*- coding: utf-8 -*-

from appium import webdriver
import time
import os
class driver_config():

    def get_driver(self):
        try:
            # self.desired_caps={}
            # self.desired_caps['deviceName']="A0001"
            # self.desired_caps['platformVersion']="8.1.0"
            # self.desired_caps['appPackage'] = "com.shinyv.cnr"
            # self.desired_caps['appActivity'] = "com.shinyv.cnr.StartActivity"
            # self.desired_caps['unicodeKeyboard'] = 'true'
            # self.desired_caps['resetKeyboard'] = "true"
            # self.desired_caps['newCommandTimeout'] = "5000"
            # self.desired_caps['platformName'] = "Android"
            # self.desired_caps['noReset'] = "true"
            # self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desired_caps)

            self.desired_caps={}
            self.desired_caps['deviceName']="127.0.0.1:21503 device"
            self.desired_caps['platformVersion']="7.1.2"
            self.desired_caps['appPackage'] = "com.shinyv.cnr"
            self.desired_caps['appActivity'] = "com.shinyv.cnr.StartActivity"
            self.desired_caps['unicodeKeyboard'] = 'true'
            self.desired_caps['resetKeyboard'] = "true"
            self.desired_caps['newCommandTimeout'] = "5000"
            self.desired_caps['platformName'] = "Android"
            self.desired_caps['noReset'] = "true"
            self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desired_caps)
            return self.driver
        except Exception as e:
            raise e



