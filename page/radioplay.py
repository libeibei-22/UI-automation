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
    playColl=(by.ID,result["playColl"]) # 电台收藏
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
    radioOrder=(by.ID,result["radioOrder"])  # 收藏按钮
    oldRadio=(by.ID,result["oldRadio"]) # 听往期按钮
    choicProgram=(by.ID,result["choicProgram"])  # 推荐栏目
    choicRadio=(by.ID,result["choicRadio"])  # 推荐电台
    historyname=result["historyname"]  # xpath, 回听节目单名称
    historytab=result["historytab"]  # xpath, 回听节目单tab，例如“今天”，“昨天”
    speedid=result["speed"] # 倍速按钮的resourseid
    speed=(by.ID,result['speed']) #倍速按钮

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
    def historyname_click(self, name):
        historynamenew=(self.by.XPATH,self.historyname+"[@text={}]".format("'"+name+"'"))
        self.find_element(*historynamenew).click()
    def historytab_click(self,tabname):
        tabnamenew=(self.by.XPATH,self.historytab+"[@text={}]".format("'"+tabname+"'"))
        self.find_element(*tabnamenew).click()
    def historyenter_click(self):
        self.find_element(*self.historyenter).click()