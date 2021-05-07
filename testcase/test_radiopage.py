# -*- coding: utf-8 -*-

from config import driver_config
import unittest
from page import broadcastpage, radioplay,basetab,startpage
from common import base_method
import time

class test_radiopage_case(unittest.TestCase):
    '''播放相关case'''
    @classmethod
    def setUpClass(cls):
        print ('开始测试')
        driver=driver_config.driver_config()
        cls.driver=driver.get_driver()
        cls.startpage=startpage.startpage(cls.driver)
        cls.page = broadcastpage.broadcastpage(cls.driver)
        cls.radioplay=radioplay.radioplay(cls.driver)
        cls.tab=basetab.basetab(cls.driver)
        cls.device=base_method.Base_page(cls.driver)

    def setUp(self):
        print('开始执行Case')
        self.imgs = []
        self.addCleanup(self.cleanup)
        self.driver.launch_app()
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
        self.tab.click_livetab()
    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def cleanup(self):
        pass

    def test01_stateRadio(self):
        '''进入国家台列表'''
        enter="国家台"
        self.page.radioEnter(enter)
        result=self.page.radiotitle_get()
        self.assertEqual(result,enter)
        self.add_img()
    def test02_localRadio(self):
        '''进入本地电台列表'''
        enter="本地台"
        self.page.radioEnter(enter)
        result=self.page.radiotitle_get()
        self.assertEqual(result,enter)
        self.add_img()
    def test03_cityRadio(self):
        '''进入地方电台列表'''
        enter="地方台"
        city="北京"
        self.page.radioEnter(enter)
        self.page.city_click(city)
        result=self.page.radiotitle_get()
        self.assertEqual(result,"北京台")
        self.add_img()
    def test04_radiotext(self):
        '''从悬浮球进入播放页'''
        radiotitle=self.page.radiotitle_get()
        programetitle=self.page.livetitle_get()
        self.page.playicon_click()
        self.tab.click_playbtn()
        playtitle=self.radioplay.radioTitle_get()
        livetitle=self.radioplay.programTitle_get()
        self.assertEqual(radiotitle,playtitle)
        self.assertIn(livetitle,programetitle)
    def test05_playlist(self):
        '''从首页进入节目单'''
        programname=str(self.page.livetitle_get())
        self.page.playicon_click()
        self.page.history_click()
        self.assertTrue(self.device.is_element_exist(programname.split("：")[1]))
    def test06_radiopage(self):
        '''进入频率主页，待补充'''
        pass
    def test07_state_radio(self):
        '''从国家台入口，进入频率主页,待补充'''
        pass
    def test08_locao_radio(self):
        '''从本地台入口，进入频率播放页'''
        enter="本地台"
        program="河北新闻广播"
        self.page.radioEnter(enter)
        self.page.radioname_click(program)
        self.assertEqual(self.radioplay.programTitle_get(),program)
        self.add_img()
    def test09_city_radio(self):
        '''从地方台入口，进入频率播放页'''
        enter="地方台"
        city="北京"
        program="北京新闻广播"
        self.page.radioEnter(enter)
        self.page.city_click(city)
        self.page.radioname_click(program)
        self.assertEqual(self.radioplay.programTitle_get(),program)
        self.add_img()
    def test10_playnextnull(self):
        '''正在直播，点击下一首'''
        self.page.playicon_click()
        self.tab.click_playbtn()
        self.radioplay.next_click()
        self.add_img()
        result=self.device.get_toast_text()
        self.assertEqual(result,"没有下一个了~")
    def test11_playprivious(self):
        '''正在直播，切换上一首'''
        self.page.playicon_click()
        title=str(self.page.livetitle_get())
        self.tab.click_playbtn()
        if title=="暂无节目单":
            self.radioplay.privious_click()
            self.assertEqual(self.device.get_toast_text(),"没有上一个了~")
            self.add_img()
        else:
            self.radioplay.privious_click()
            time.sleep(3)
            self.add_img()
            self.assertTrue(self.device.is_element_exist(self.radioplay.speedid)) #通过倍速按钮是否展示，判断是否从直播切换到了回听
    def test12_historyradio(self):
        '''当天节目单回听'''
        self.page.playicon_click()
        self.tab.click_playbtn()
        self.radioplay.historyenter_click()
        self.device.swipeDown()
        ele=self.driver.find_elements_by_xpath(self.radioplay.historyname)
        historylist=[]
        for i in ele:
            m=i.get_attribute("text")
            historylist.append(m)
        print(historylist)
        programtitle=historylist[0]
        ele[0].click()
        self.add_img()
        time.sleep(3)
        self.assertEqual(programtitle,self.radioplay.programTitle_get())
    def test13_historylive(self):
        '''当天节目单直播'''
        self.page.playicon_click()
        self.tab.click_playbtn()
        time.sleep(3)
        programtitle=str(self.radioplay.programTitle_get())
        print(programtitle)
        self.radioplay.historyenter_click()
        time.sleep(5)
        self.radioplay.historyname_click(programtitle)
        # self.driver.find_element_by_xpath("//*[@resource-id='com.shinyv.cnr:id/tv_column_name'][@text='新闻进行时']").click()
        programtitlenew=self.radioplay.programTitle_get()
        print(programtitle)
        print(programtitlenew)
        self.assertEqual(programtitle,programtitlenew)


    def tearDown(self) -> None:
        print("Case执行完毕")
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        print('测试完成')
        cls.driver.quit()

if __name__ == "__main__":
        unittest.main()
