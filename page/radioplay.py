# -*- coding: utf-8 -*-
'''
封装了频率播放页
各个元素的定位
大部分元素的点击和获取文本的方法
'''
from common import base_method
from appium.webdriver.common import mobileby
import yaml
class radioplay(base_method.Base_page):
    by=mobileby.MobileBy()
    with open(base_method.Base_page.data_save_address+'/element', 'r', encoding='utf-8') as f:
        result=yaml.load(f.read(),Loader=yaml.FullLoader)["radioPlay"]

    historyenter=(by.ID,result["historyenter"])   # 回听入口列表
    playHd=(by.ID,result["playHd"])  # 音质切换
    playStop=(by.ID,result["playStop"])  # 定时停止
    programTitle=(by.ID,result["programTitle"])  # 当前节目名称
    programTime=(by.ID,result["programTime"]) # 当前节目播放时段
    startTime=(by.ID,result["startTime"])  # 开始时间 text:15:18:50
    endTime=(by.ID,result["endTime"])  # 结束时间
    seekbar=(by.ID,result["seekbar"])  # 播放进度条 text:8330.0
    previous=(by.ID,result["previous"]) # 上个节目
    next=(by.ID,result["next"])  # 下个节目
    play=(by.ID,result["play"])  # 播放/暂停
    back=(by.ID,result["back"])  # 左上角返回按钮
    radioTitle=(by.ID,result["radioTitle"])  # 顶部频道名称
    more=(by.ID,result["more"])  # 右上角更多按钮
    radioOrder=(by.ID,result["radioOrder"])# 收藏按钮，红心按钮
    oldRadio=(by.ID,result["oldRadio"]) # 听往期按钮
    choicProgram=(by.ID,result["choicProgram"])  # 推荐栏目
    choicRadio=(by.ID,result["choicRadio"])  # 推荐电台
    historyname=result["historyname"]  # xpath, 回听节目单名称
    historytab=result["historytab"]  # xpath, 回听节目单tab，例如“今天”，“昨天”
    speedid=result["speed"] # 倍速按钮的resourseid
    speed=(by.ID,result['speed']) #倍速按钮
    hd=result["hd"] # xpath，音质选择项，标准，高音质
    clockname=(by.XPATH,result["clockname"])  # xpath, 倒计时选项，10分，20分
    timename=(by.ID,result['timename'])  # xpath, 倒计时时间，“倒计时xx分xx秒”
    orderbtn=(by.ID,result["order"]) #收藏按钮，非红心按钮
    btnplayer=(by.ID,result["btnplayer"])  # 播放页顶部悬浮播放按钮

    def radioTitle_get(self):
        '''播放页顶部频道标题'''
        result=self.find_element(*self.radioTitle).text
        return result
    def programTitle_get(self):
        '''栏目名称'''
        result=self.find_element(*self.programTitle).text
        return result
    def next_click(self):
        self.find_element(*self.next).click()
    def privious_click(self):
        self.find_element(*self.previous).click()
    def play_click(self):
        self.find_element(*self.play).click()
    def historyname_xpath_get(self,name):
        historynamenew=(self.historyname+"[@text={}]".format("'"+name+"'"))
        return historynamenew
    def historytab_click(self,tabname):
        tabnamenew=(self.by.XPATH,self.historytab+"[@text={}]".format("'"+tabname+"'"))
        self.find_element(*tabnamenew).click()
    def historyenter_click(self):
        self.find_element(*self.historyenter).click()
    def playhd_click(self):
        self.find_element(*self.playHd).click()
    def hdselect_click(self,hdname):
        hdnew=(self.by.XPATH,self.hd+"[@text={}]".format("'"+hdname+"'"))
        self.find_element(*hdnew).click()
    def playstop_click(self):
        self.find_element(*self.playStop).click()
    def clock_click(self):
        self.find_element(*self.clockname).click() #点击10分钟倒计时
    def time_get(self):
        timename=self.find_element(*self.timename).text
        return timename
    def radioorder_click(self):
        self.find_element(*self.radioOrder).click()
    def starttime_get(self):
        result=self.find_element(*self.startTime).text
        return result
    def more_click(self):
        self.find_element(*self.more).click()
    def orderbtb_click(self):
        self.find_element(*self.orderbtn).click()
    def oldradio_click(self):
        self.find_element(*self.oldRadio).click()
    def btnplayer_click(self):
        self.find_element(*self.btnplayer).click()
    def btnplayer_get(self):
        result=self.find_element(*self.btnplayer).text
        return result
