# -*- coding: utf-8 -*-

from config import driver_config
import unittest
import time
from page import login, basetab, startpage
from page import albumplay, albumdetail, Search
from common import base_method


class testcase(unittest.TestCase):
    '''我的页面相关Case'''
    @classmethod
    def setUpClass(cls) -> None:
        driver=driver_config.driver_config()
        cls.driver=driver.get_driver()
        cls.search_song = Search.search(cls.driver)
        cls.album_detial = albumdetail.albumdetail(cls.driver)
        cls.album_play = albumplay.albumplay(cls.driver)
        cls.startpage= startpage.startpage(cls.driver)
        cls.login = login.login_page(cls.driver)
        cls.device= base_method.Base_page(cls.driver)
        cls.basetab= basetab.basetab(cls.driver)
    def setUp(self) -> None:
        print ('start testing')
        self.driver.launch_app()
        self.imgs = []
        self.addCleanup(self.cleanup)
        time.sleep(2)
        try:
            self.startpage.click_adskipbtn()
            print("出现了开屏广告并跳过了它")
        except Exception as e:
            print("未出现开屏广告")
        try:
            self.startpage.get_ad2view_status()
            self.startpage.click_adskipbtn2()
            print("出现了插屏广告并关闭了它")
        except Exception as e:
            print("未出现插屏广告")

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def cleanup(self):
        pass

    def test_01login(self):
        time.sleep(2)
        self.basetab.click_mytab()
        try:
            self.driver.find_element_by_id("com.shinyv.cnr:id/unLogin_btn").is_displayed()
        except Exception as e:
            self.device.swipeUp(n=1)
            time.sleep(2)
            self.driver.find_element_by_id('com.shinyv.cnr:id/other_setting').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.shinyv.cnr:id/tv_logout').click()
            time.sleep(2)
            self.device.swipeDown(n=1)
            time.sleep(2)
        self.driver.find_element_by_id("com.shinyv.cnr:id/unLogin_btn").click()
        self.login.login("15810436915","123456")
        toastname=self.device.get_toast_text()
        print (toastname)
        self.assertEqual(toastname,"登录成功")
        time.sleep(5)
        text1=self.driver.find_element_by_id("com.shinyv.cnr:id/tv_sign").text
        self.assertEqual(text1,"签到","签到按钮文案错误")
        self.add_img()
        print ('alarady stared')

    def tearDown(self) -> None:
        print("Case执行完毕")
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def tearDown(self) -> None:
        print('测试结束')

if __name__=="__main__":
    unittest.main()
