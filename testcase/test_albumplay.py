# -*- coding: utf-8 -*-

from config import driver_config
import unittest
import time
from page import albumplay, albumdetail, Search, login, startpage
from common import base_method

class test_albumplay_case(unittest.TestCase):
    '''播放相关case'''
    @classmethod
    def setUpClass(cls):
        print ('开始测试')
        driver=driver_config.driver_config()
        cls.driver=driver.get_driver()
        cls.search_song = Search.search(cls.driver)
        cls.album_detail= albumdetail.albumdetail(cls.driver)
        cls.album_play= albumplay.albumplay(cls.driver)
        cls.startpage= startpage.startpage(cls.driver)
        cls.login= login.login_page(cls.driver)
        cls.device=base_method.Base_page(cls.driver)

    def setUp(self):
        print('开始执行Case')
        self.imgs = []
        self.addCleanup(self.cleanup)
        self.driver.launch_app()
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

    def test01_playsong(self):
        '''查看专辑是否正确'''
        # time.sleep(10)
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        time.sleep(3)
        self.assertEqual(self.album_play.get_albumtitle(),"测试专辑8")
        self.add_img()

    def test02_play_status(self):
        '''正在播放'''
        # time.sleep(5)
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        time.sleep(3)
        seekbar_begin=self.album_play.get_play_seekbar()
        time.sleep(3)
        seekbar_end=self.album_play.get_play_seekbar()
        self.assertNotEqual(seekbar_begin,seekbar_end)  #验证进度条进度是否一样判断是否播放状态
        self.add_img()
    def test03_play_status(self):
        '''暂停播放'''
        # time.sleep(5)
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        self.album_play.click_play()
        seekbar_begin=self.album_play.get_play_seekbar()
        print(seekbar_begin)
        time.sleep(5)
        seekbar_end=self.album_play.get_play_seekbar()
        print(seekbar_end)
        self.assertEqual(seekbar_begin,seekbar_end)  #验证进度条进度是否一样判断是否播放状态
        self.add_img()

    def test04_play_next_song(self):
        '''播放下一首'''
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        self.album_play.click_next_song()
        self.assertEqual(self.album_play.get_play_song_name(),"4")
        self.add_img()

    def test05_play_previous_song(self):
        '''播放上一首'''
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        self.album_play.click_previous_song()
        self.assertEqual(self.album_play.get_play_song_name(),"2")
        self.add_img()
    def test06_songlist_view(self):
        '''打开播放列表'''
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        self.album_play.click_songlist()
        self.assertTrue(self.album_play.get_songlist_status())
        self.add_img()
    def test07_close_songlist(self):
        '''关闭播放列表'''
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        self.album_play.click_songlist()
        self.album_play.click_songlist_closed()
        time.sleep(3)
        try:
            self.album_play.get_songlist_status()
        except Exception as e:
            return True
        self.add_img()
    def test08_playmode(self):
        '''切换播放模式（循环模式）'''
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        self.album_play.click_songlist()
        self.album_play.click_playmode()
        playmodetext1=self.album_play.get_playmode()
        self.album_play.click_songlist_closed()
        self.album_play.click_playrate()
        playmodetext2=self.album_play.get_playmode()
        self.assertEqual(playmodetext1,playmodetext2)
        self.add_img()

    def test09_playlistsort(self):
        '''播放排序（列表排序）'''
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        self.album_play.click_songlist()
        if self.album_play.get_playsort()=="正序":
            self.album_play.click_playsort()
            time.sleep(3)
            songname=self.album_play.songlistfirstone_get()
            self.assertIn("3",songname)
            self.add_img()
        elif self.album_play.get_playsort()=="倒序":
            self.album_play.click_playsort()
            time.sleep(3)
            songname=self.album_play.songlistfirstone_get()
            self.assertIn("1",songname)
            self.add_img()

    def test10_order(self):
        '''单曲订阅'''
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        orderstatus=self.album_play.get_order_status()
        self.add_img()
        if orderstatus=="订阅":
            print("当前未订阅")
            self.album_play.click_order()
            try:
                self.login.click_enloginpassword()
                self.login.login("14444444441","111111")
                print("未登录状态，已登录成功")
                self.album_play.click_order()
            except Exception as e:
                print("已登录状态")
            self.add_img()
            self.assertEqual(self.album_play.get_order_status(),"已订阅")
        else:
            print("当前已订阅")
            self.album_play.click_order()
            self.assertEqual(self.album_play.get_order_status(),"订阅")
            self.add_img()

    def test11_moredown(self):
        '''更多-下载'''
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        self.album_play.more_click()
        if self.album_play.moredownloadtext_get()=="下载":
            self.add_img()
            self.album_play.moredownload_click()
            toastname=self.device.get_toast_text(self.driver)
            self.assertEqual(toastname,"正在下载...")
            time.sleep(5)
            self.album_play.more_click()
            self.assertEqual(self.album_play.moredownloadtext_get(),"已下载")
            self.add_img()
        elif self.album_play.moredownloadtext_get()=="已下载":
            print("该单曲已下载过")
            self.album_play.moredownload_click()
            toastname=self.device.get_toast_text(self.driver)
            print(toastname)
            self.assertEqual(toastname,"已经添加到下载列表")


    def test12_morecollect(self):
        '''更多-收藏'''
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        self.album_play.more_click()
        collecttext1 = self.album_play.morecollecttext_get()
        self.album_play.morecollect_click()
        try:
            self.login.click_enloginpassword()
            self.login.login("14444444441", "111111")
            print("未登录状态，已登录成功")
            self.album_play.more_click()
            collecttext1=self.album_play.morecollecttext_get()
            self.add_img()
            self.album_play.morecollect_click()
            self.album_play.more_click()
            collecttext2=self.album_play.morecollecttext_get()
            self.add_img()
            self.assertNotEqual(collecttext1,collecttext2)
        except Exception as e:
            self.album_play.more_click()
            collecttext2 = self.album_play.morecollecttext_get()
            self.add_img()
            self.assertNotEqual(collecttext1,collecttext2)
    def test13_hd(self):
        '''切换音质'''
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        if self.album_play.hdtext_get()=="标准":
            self.album_play.hd_click()
            self.album_play.hd2_click()
            self.assertEqual(self.album_play.hdtext_get(),"高品质")
            self.add_img()
        elif self.album_play.hdtext_get()=="高品质":
            self.album_play.hd_click()
            self.album_play.hd1_click()
            self.assertEqual(self.album_play.hdtext_get(),"标准")
            self.add_img()
    def test14_speed(self):
        '''倍速切换'''
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        try:
            self.album_play.speed_click()
            self.album_play.speedv1_click()
            self.add_img()
            self.album_play.speed_click()
            self.album_play.speedv5_click()
            self.add_img()
            return True
        except Exception as e:
            return False
    def test15_speedtochannel(self):
        '''切换倍速后，查看电台回听的倍速，待补充'''
        pass

    def tearDown(self) -> None:
        print("Case执行完毕")
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        print('测试完成')
        cls.driver.quit()



if __name__=="__main__":
    unittest.main()