# -*- coding: utf-8 -*-

from config import driver_config
import unittest
from page import broadcastpage, radioplay,basetab,startpage,login,albumdetail
from common import base_method
import time

class test_radiopage_case(unittest.TestCase):
    '''电台播放相关case'''
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
        cls.login=login.login_page(cls.driver)
        cls.albumdetail=albumdetail.albumdetail(cls.driver)

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
        result=self.page.radiolist_title_get()
        print(result)
        self.assertEqual(result,enter)
        self.add_img()
    def test02_localRadio(self):
        '''进入本地电台列表'''
        enter="本地台"
        self.page.radioEnter(enter)
        result=self.page.radiolist_title_get()
        self.assertEqual(result,enter)
        self.add_img()
    def test03_cityRadio(self):
        '''进入地方电台列表'''
        enter="地方台"
        city="北京"
        self.page.radioEnter(enter)
        self.page.city_click(city)
        result=self.page.radiolist_title_get()
        self.assertEqual(result,"北京台")
        self.add_img()
    def test04_radiotext(self):
        '''从悬浮球进入播放页'''
        radiotitle=self.page.radiotitle_get()
        programetitle=self.page.livetitle_get()
        self.add_img()
        self.page.playicon_click()
        self.tab.click_playbtn()
        playtitle=self.radioplay.radioTitle_get()
        livetitle=self.radioplay.programTitle_get()
        self.assertEqual(radiotitle,playtitle)
        self.assertIn(livetitle,programetitle)
        self.add_img()
    def test05_playlist(self):
        '''从首页进入节目单'''
        programname=str(self.page.livetitle_get())
        self.page.playicon_click()
        self.page.history_click()
        self.assertTrue(self.device.is_element_exist(programname.split("：")[1]))
        self.add_img()
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
        '''从当天节目单进入回听播放'''
        self.page.playicon_click()
        self.tab.click_playbtn()
        self.radioplay.historyenter_click()
        time.sleep(3)
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
        '''从当天节目单进入直播播放页,定位有问题，待解决'''
        self.page.playicon_click()
        self.tab.click_playbtn()
        time.sleep(3)
        programtitle=str(self.radioplay.programTitle_get())
        print(programtitle)
        self.radioplay.historyenter_click()
        print(self.radioplay.historyname_xpath_get(programtitle))
        self.radioplay.historyname_click(programtitle)   #定位问题，直播项无法定位
        # self.driver.find_element_by_xpath("//*[@resource-id='com.shinyv.cnr:id/tv_column_name'][@text='正午60分']").click()
        # self.driver.find_element_by_xpath(self.radioplay.historyname_xpath_get(programtitle)).click()
        programtitlenew=self.radioplay.programTitle_get()
        print(programtitle)
        print(programtitlenew)
        self.assertEqual(programtitle,programtitlenew)
    def test14_historyradioPre(self):
        '''从昨天的节目单进入回听播放'''
        self.page.playicon_click()
        self.tab.click_playbtn()
        self.radioplay.historyenter_click()
        self.radioplay.historytab_click("昨天")
        time.sleep(3)
        # self.device.swipeDown()
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
    def test15_nostartradio(self):
        '''点击未开始的栏目'''
        self.page.playicon_click()
        self.tab.click_playbtn()
        self.radioplay.historyenter_click()
        time.sleep(5)
        ele = self.driver.find_elements_by_xpath(self.radioplay.historyname)
        historylist = []
        for i in ele:
            m = i.get_attribute("text")
            historylist.append(m)
        print(historylist)
        ele[-1].click()
        toast=self.device.get_toast_text()
        self.add_img()
        self.assertEqual(toast,"节目还未开始")

    def test16_hdselect(self):
        '''切换音质'''
        self.page.playicon_click()
        self.tab.click_playbtn()
        self.add_img()
        self.radioplay.playhd_click()
        self.radioplay.hdselect_click("高品质")
        self.add_img()

    def test17_clock(self):
        '''选择倒计时，查看倒计时文案'''
        self.page.playicon_click()
        self.tab.click_playbtn()
        self.radioplay.playstop_click()
        time.sleep(5)
        self.radioplay.clock_click()
        # self.driver.find_element_by_xpath("//android.widget.RelativeLayout[2]/android.widget.TextView[1]").click()
        self.radioplay.playstop_click()
        self.add_img()
        time1=self.radioplay.time_get()
        self.assertIn("倒计时",time1)
    def test18_order(self):
        '''电台收藏和取消收藏（红心按钮）'''
        self.page.playicon_click()
        self.tab.click_playbtn()
        self.radioplay.radioorder_click()
        try:
            toast = self.device.get_toast_text()
            print("第一次是:"+toast)
        except Exception as e:
            print("用户未登录")
            self.login.click_enloginpassword()
            self.login.login("15810436915","123456")
            self.radioplay.radioorder_click()
            toast=self.device.get_toast_text()
            print("第一次是:"+toast)
        self.add_img()
        if toast=="已收藏":
            self.radioplay.radioorder_click()
            toastnew=self.device.get_toast_text()
            print("第二次是:"+toastnew)
            self.assertEqual(toastnew,"已取消收藏")
        elif toast=="已取消收藏":
            self.radioplay.radioorder_click()
            toastnew=self.device.get_toast_text()
            print("第二次是:"+toastnew)
            self.assertEqual(toastnew,"已收藏")
        self.add_img()
    def test19_pause(self):
        '''回听暂停播放'''
        self.page.playicon_click()
        self.tab.click_playbtn()
        self.radioplay.privious_click()
        time.sleep(2)
        self.radioplay.play_click()
        time1=self.radioplay.starttime_get()
        time.sleep(8)
        time2=self.radioplay.starttime_get()
        self.assertEqual(time1,time2)
    def test20(self):
        '''分享弹框展示正常'''
        self.page.playicon_click()
        self.tab.click_playbtn()
        self.radioplay.more_click()
        time.sleep(3)
        self.add_img()
        self.assertTrue(self.device.is_element_exist("微信好友"))
    def test21_order2(self):
        '''电台收藏和取消收藏（非红心按钮）'''
        self.page.playicon_click()
        self.tab.click_playbtn()
        time.sleep(3)
        self.device.swipeUp(n=1)
        self.radioplay.orderbtb_click()
        try:
            toast = self.device.get_toast_text()
            print("第一次是:"+toast)
        except Exception as e:
            print("用户未登录")
            self.login.click_enloginpassword()
            self.login.login("15810436915","123456")
            self.radioplay.radioorder_click()
            toast=self.device.get_toast_text()
            print("第一次是:"+toast)
        self.add_img()
        if toast=="已收藏":
            self.radioplay.radioorder_click()
            toastnew=self.device.get_toast_text()
            print("第二次是:"+toastnew)
            self.assertEqual(toastnew,"已取消收藏")
        elif toast=="已取消收藏":
            self.radioplay.radioorder_click()
            toastnew=self.device.get_toast_text()
            print("第二次是:"+toastnew)
            self.assertEqual(toastnew,"已收藏")
        self.add_img()
    def test22_order2(self):
        '''听往期跳转'''
        self.page.playicon_click()
        self.tab.click_playbtn()
        programname=str(self.radioplay.programTitle_get()).strip()
        time.sleep(3)
        self.device.swipeUp(n=1)
        self.radioplay.oldradio_click()
        result=str(self.albumdetail.albumName_get()).strip()
        self.assertEqual(programname,result)
        self.add_img()
    def test23_order2(self):
        '''吸顶播放按钮状态,定位有问题，会报错'''
        self.page.playicon_click()
        self.tab.click_playbtn()
        time.sleep(3)
        self.device.swipeUp(n=1)
        result1=self.radioplay.btnplayer_get()
        time.sleep(5)
        self.radioplay.btnplayer_click()
        result2=self.radioplay.btnplayer_get()
        self.assertEqual(result1,"暂停")
        self.assertEqual(result2,"播放")

    def tearDown(self) -> None:
        print("Case执行完毕")
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        print('测试完成')
        cls.driver.quit()

if __name__ == "__main__":
        unittest.main()
