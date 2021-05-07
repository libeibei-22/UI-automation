# -*- coding: utf-8 -*-
'''
封装了听广播tab首页，和二级页电台列表
各个元素的定位
大部分元素的点击和获取文本的方法
'''
from common import base_method
from appium.webdriver.common import mobileby
import yaml
class broadcastpage(base_method.Base_page):
    by=mobileby.MobileBy()
    with open(base_method.Base_page.data_save_address+'/element', 'r', encoding='utf-8') as f:
        result=yaml.load(f.read(),Loader=yaml.FullLoader)["broadcastPage"]
    with open(base_method.Base_page.data_save_address + '/element', 'r', encoding='utf-8') as f:
        result2 = yaml.load(f.read(), Loader=yaml.FullLoader)["broadcastlist"]
    playicon=(by.ID,result["playicon"])  # 顶部播放按钮
    playtitle=(by.ID,result["playtitle"])   # 正在播放的频道
    programlive=(by.ID,result["programlive"])   # 当前播放的节目名称
    historybtn=(by.ID,result["historybtn"])   # 节目单入口
    tvname=result["tvname"]  # xpath,当前页内容入口，比如”国家台“
    tvlogo=(by.ID,result["tvlogo"])   # 顶部电台logo
    title=result2["title"]   # xpath,电台列表标题：国家台、地方台
    titleget=(by.ID,result2["titleget"]) #id，电台列表标题：国家台、地方台
    radioName=result2["radioName"]  # xpath,电台名称
    radioDes=result2["radioDes"]  # xpath,当前正在播放的栏目描述
    cityname=result2["cityname"]  #xpath,地方台，城市名称
    back=(by.ID,result2["back"])   # 返回按钮
    radioIcon=(by.ID,result2["radioIcon"]) #电台图标
    def playicon_click(self):
        self.find_element(*self.playicon).click()

    #点击首页电台内容入口，例如，国家台，地方台等
    def radioEnter(self, name):
        tvnamenew=(self.by.XPATH,self.tvname + "[@text={}]".format("'"+name+"'"))
        self.find_element(*tvnamenew).click()
    def city_click(self,name):
        citynamenew=(self.by.XPATH,self.cityname+"[@text={}]".format("'"+name+"'"))
        self.find_element(*citynamenew).click()
    #获取电台列表顶部的标题
    def radiotitle_get(self):
        result=self.find_element(*self.titleget).text
        return result
    def radioname_click(self,name):
        radionamenew=(self.by.XPATH,self.radioName+"[@text={}]".format("'"+name+"'"))
        self.find_element(*radionamenew).click()
    #获取频道名称
    def radiotitle_get(self):
        result=self.find_element(*self.playtitle).text
        return result
    #获取栏目名称
    def livetitle_get(self):
        result=self.find_element(*self.programlive).text
        return result
    #节目单入口
    def history_click(self):
        self.find_element(*self.historybtn).click()






