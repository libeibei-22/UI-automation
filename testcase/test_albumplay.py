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
        self.search_song.searchkeywords_selectone("测试", "测试哈哈")
        self.album_detail.selectsong("短1")
        self.assertEqual(self.album_play.get_albumtitle(),"测试哈哈")
        self.add_img()

    def test02_play_status(self):
        '''正在播放'''
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("3")
        time.sleep(3)
        seekbar_begin=self.album_play.get_play_seekbar()
        time.sleep(3)
        seekbar_end=self.album_play.get_play_seekbar()
        self.assertNotEqual(seekbar_begin,seekbar_end)  #验证进度条进度是否一样判断是否播放状态
        self.add_img()
    def test03_play_status(self):
        '''暂停播放'''
        # time.sleep(5)
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("3")
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
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("3")
        self.album_play.click_next_song()
        self.assertEqual(self.album_play.get_play_song_name(),"4")
        self.add_img()

    def test05_play_previous_song(self):
        '''播放上一首'''
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("3")
        self.album_play.click_previous_song()
        self.assertEqual(self.album_play.get_play_song_name(),"2")
        self.add_img()
    def test06_songlist_view(self):
        '''打开播放列表'''
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("3")
        self.album_play.click_songlist()
        self.assertTrue(self.album_play.get_songlist_status())
        self.add_img()
    def test07_close_songlist(self):
        '''关闭播放列表'''
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("3")
        self.album_play.click_songlist()
        self.album_play.click_songlist_closed()
        time.sleep(3)
        try:
            result=self.album_play.get_songlist_status()
        except Exception as e:
            self.assertFalse(False)
        else:
            self.assertFalse(result)
        self.add_img()
    def test08_playmode(self):
        '''切换播放模式（循环模式）'''
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("3")
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
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("3")
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
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("3")
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
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("3")
        self.album_play.more_click()
        if self.album_play.moredownloadtext_get()=="下载":
            self.add_img()
            self.album_play.moredownload_click()
            toastname=self.device.get_toast_text()
            self.assertEqual(toastname,"正在下载...")
            time.sleep(5)
            self.album_play.more_click()
            self.assertEqual(self.album_play.moredownloadtext_get(),"已下载")
            self.add_img()
        elif self.album_play.moredownloadtext_get()=="已下载":
            print("该单曲已下载过")
            self.album_play.moredownload_click()
            toastname=self.device.get_toast_text()
            self.assertEqual(toastname,"已经添加到下载列表")


    def test12_morecollect(self):
        '''更多-收藏'''
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("3")
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
        except Exception as e:
            self.album_play.more_click()
            collecttext2 = self.album_play.morecollecttext_get()
            self.add_img()
            self.assertNotEqual(collecttext1,collecttext2)
        else:
            self.assertNotEqual(collecttext1, collecttext2)
    def test13_hd(self):
        '''切换音质'''
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("3")
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
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("3")
        try:
            self.album_play.speed_click()
            self.album_play.speedv1_click()
            self.add_img()
            self.album_play.speed_click()
            self.album_play.speedv5_click()
            self.add_img()
        except Exception as e:
            print(e)
    def test15_speedtochannel(self):
        '''切换倍速后，查看电台回听的倍速，待补充'''
        pass

    def test16_replysend(self):
        '''发送评论'''
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("3")
        self.album_play.replyenter_click()
        try:
            self.login.click_enloginpassword()
            self.login.login("15810436915", "123456")
            print("未登录状态，已登录成功")
            self.album_play.replyenter_click()
        except Exception as e:
            self.album_play.replyedit_input("测试评论")
            self.album_play.replysend_click()
            print(self.device.get_toast_text())
            self.assertEqual(self.device.get_toast_text(),"评论已发出，审核后显示")
    def test17_paopaoisDisplay(self):
        '''泡泡条展示'''
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("3")
        title=self.album_play.paopaoTitle_get()
        des=self.album_play.paopaoDes_get()
        self.assertEqual(title,"我是标题")
        self.assertEqual(des,"我是描述")
        self.add_img()

    def test18_paopaoisDotDisplay(self):
        '''泡泡条不展示'''
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("3")
        self.album_play.click_next_song()
        try:
            result=self.album_play.paopaoview_Display()
        except Exception as e:
            self.assertFalse(False)
        else:
            self.add_img()
            self.assertFalse(result)
            print("出现了泡泡条")

    def test19_paopaoClick(self):
        '''泡泡条跳转'''
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("3")
        self.album_play.paopao_click()
        self.add_img()
        self.assertEqual(self.album_detail.albumName_get(),"测试专辑014")
    def test20_paopaoSwitch(self):
        '''切换单曲泡泡条要更新'''
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("2")
        self.add_img()
        title1=self.album_play.paopaoTitle_get()
        self.album_play.click_next_song()
        self.add_img()
        title2=self.album_play.paopaoTitle_get()
        self.assertNotEqual(title1,title2)
    def test21_zhuchuangname(self):
        '''关注/取消关注主创'''
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("2")
        time.sleep(2)
        self.device.swipeUp(n=2)
        time.sleep(2)
        self.album_play.XZP_click("主创")
        self.add_img()
        self.album_play.zhuchuangfocus_click()
        try:
            result = self.device.get_toast_text()
        except Exception as e:
            self.login.click_enloginpassword()
            self.login.login("15810436915","123456")
            self.album_play.zhuchuangfocus_click()
            result=self.device.get_toast_text()
        self.add_img()
        self.assertIn("关注",result)

    def test22_zhuchuangdes(self):
        '''获取主创描述'''
        self.search_song.searchkeywords_selectone("测试专辑8", "测试专辑8")
        self.album_detail.selectsong("2")
        self.device.swipeUp(n=2)
        time.sleep(2)
        self.album_play.XZP_click("主创")
        self.add_img()
        self.assertEqual(self.album_play.zhuchangdes_get(),u"我是UMC哈哈哈")
    def tearDown(self) -> None:
        print("Case执行完毕")
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        print('测试完成')
        cls.driver.quit()



if __name__=="__main__":
    unittest.main()