# -*- coding: utf-8 -*-

from common import base_method
from appium.webdriver.common import mobileby
import yaml
class albumplay(base_method.Base_page):
    by=mobileby.MobileBy()
    with open(base_method.Base_page.data_save_address+'/element', 'r', encoding='utf-8') as f:
        result=yaml.load(f.read(),Loader=yaml.FullLoader)["albumplay"]
    playbtn=(by.ID,result["playbtn"]) #播放按钮
    nextbtn=(by.ID,result["nextbtn"]) #下一首
    previousbtn=(by.ID,result["previousbtn"])  #上一首
    playlist=(by.ID,result["playlist"]) #播放列表入口
    alarm=(by.ID,result["alarm"]) #定时关闭
    speed=(by.ID,result["speed"]) #倍速
    hd=(by.ID,result["hd"])  #音质
    rate=(by.ID,result["rate"]) #音质右侧的按钮
    more=(by.ID,result["more"]) #右上角更多按钮
    songback=(by.ID,result["songback"]) #返回按钮
    albumtitle=(by.ID,result["albumtitle"]) #专辑名称
    playsongname=(by.ID,result["playsongname"])  #单曲名称
    playseekbar=(by.ID,result["playseekbar"]) #播放进度条
    orderbtn=(by.ID,result["orderbtn"]) #订阅按钮
    songlist=(by.ID,result["songlist"]) #播放列表
    songlistfirstone=(by.ID,result["songlistfirstone"])  # 播放列表中，第一个位置
    playmode=(by.ID,result["playmode"]) #播放模式：顺序，随机，单曲循环
    songlistsort=(by.ID,result["songlistsort"]) #播放列表排序
    songlist_closedbtn=(by.ID,result["songlist_closedbtn"]) #播放列表关闭按钮
    songlistitme=(by.XPATH,result["songlistitem"]) #播放列表选项
    moreclose=(by.ID,result["moreclose"]) #更多弹框，关闭按钮
    moredownload=(by.ID,result["moredownload"]) #更多弹框，下载按钮
    moreviewalbum=(by.ID,result["moreviewalbum"]) # 更多弹框，查看专辑
    morecllect=(by.ID,result["morecllect"]) # 更多弹框，收藏按钮
    hd1=(by.XPATH, result["hd1"])  # 标准音质选项
    hd2=(by.XPATH, result["hd2"]) # 高品质音质选项
    replyenter=(by.ID,result["replyenter"])  # 底部评论入口
    replybtn=(by.ID,result["replybtn"])  # 底部评论按钮
    replyedit=(by.ID,result["replyedit"])  # 评论输入框
    replysend=(by.ID,result["replysend"])  # 评论发送按钮
    speedv5=(by.ID,result["speedv5"]) #5倍速选项
    speedv0 = (by.ID,result["speedv0"])  # 0.5倍速选项
    #点击播放按钮
    def click_play(self):
        self.find_element(*self.playbtn).click()
    #获取专辑名称
    def get_albumtitle(self):
        title=self.find_element(*self.albumtitle).text
        return title
    #获取单曲名称
    def get_play_song_name(self):
        name=self.find_element(*self.playsongname).text
        return name
    def click_next_song(self):
        self.find_element(*self.nextbtn).click()
    def click_previous_song(self):
        self.find_element(*self.previousbtn).click()
    #获取播放进度（单位是秒，120.0）
    def get_play_seekbar(self):
        seekbar12=self.find_element(*self.playseekbar).text
        return seekbar12
    #获取订阅状态
    def get_order_status(self):
        status=self.find_element(*self.orderbtn).text
        return status
    #点击订阅按钮
    def click_order(self):
        self.find_element(*self.orderbtn).click()

    #点击播放列表
    def click_songlist(self):
        self.find_element(*self.playlist).click()
    #播放列表是否展示
    def get_songlist_status(self):
        return self.find_element(*self.songlist).is_displayed()
    #关闭播放列表
    def click_songlist_closed(self):
        self.find_element(*self.songlist_closedbtn).click()
    #切换播放模式
    def click_playmode(self):
        self.find_element(*self.playmode).click()
    #获取播放模式
    def get_playmode(self):
        status=self.find_element(*self.playmode).text
        return status
    #点击音质右侧按钮
    def click_playrate(self):
        self.find_element(*self.rate).click()
    #点击排序按钮
    def click_playsort(self):
        self.find_element(*self.songlistsort).click()
    #获取排序状态
    def get_playsort(self):
        sort=self.find_element(*self.songlistsort).text
        return sort
    def click_songlistitem(self):
        self.find_element(*self.songlistitme).click()
    def songlistfirstone_get(self):
        return self.find_element(*self.songlistfirstone).text
    def more_click(self):
        self.find_element(*self.more).click()
    def moredownload_click(self):
        self.find_element(*self.moredownload).click()
    def moredownloadtext_get(self):
        return self.find_element(*self.moredownload).text
    def morecollect_click(self):
        self.find_element(*self.morecllect).click()
    def morecollecttext_get(self):
        return self.find_element(*self.morecllect).text
    def moreviewalbum_click(self):
        self.find_element(*self.moreviewalbum).click()
    def hd_click(self):
        self.find_element(*self.hd).click()
    def hdtext_get(self):
        return self.find_element(*self.hd).text
    def hd1_click(self):
        self.find_element(*self.hd1).click()
    def hd2_click(self):
        self.find_element(*self.hd2).click()
    def speed_click(self):
        self.find_element(*self.speed).click()
    def speedv5_click(self):
        self.find_element(*self.speedv5).click()
    def speedv1_click(self):
        self.find_element(*self.speedv0).click()











