# -*- coding: utf-8 -*-

from common import base_method
from appium.webdriver.common import mobileby
import time
import yaml

class search(base_method.Base_page):
    by=mobileby.MobileBy()
    with open(base_method.Base_page.data_save_address+'/element','r',encoding='utf-8') as f:
        result=yaml.load(f.read(),Loader=yaml.FullLoader)['search']

    #搜索框
    searchenter=(by.ID,result['searchenter'])
    #点击搜索框后的框
    etsearch=(by.ID,result['etsearch'])
    #搜索按钮
    beginsearchbutton=(by.ID,result['beginsearchbutton'])
    #搜索结果选项，需要匹配text使用
    firstresult=result['firstresult']
    #搜索结果tab:精选、专辑、单曲...
    resultTab=result['resultTab']

    def searchbuttonclick(self):
        self.find_element(*self.searchenter).click()
    #输入搜索词
    def inputsearchkey(self,keyword):
        self.send_keys(keyword,*self.etsearch)
    #开始搜索
    def beginsearch(self):
        self.find_element(*self.beginsearchbutton).click()
    def resultTab_click(self,tab="精选"):
        resultnew=(self.by.XPATH,self.resultTab + "[@text={}]".format("'"+tab+"'"))
        self.find_element(*resultnew).click()
    #选择搜索结果中带有m的结果项
    def selectfirstone(self,m):
        m_str="'"+m+"'"
        firstresult1 = (self.by.XPATH, self.firstresult + "[@text={}]".format(m_str))
        self.find_element(*firstresult1).click()
    #搜索关键词并对指定tab的结果选择，默认tab是精选
    def searchkeywords_selectone(self,searchwords,selectitem,tab="精选"):
        self.searchbuttonclick()
        self.inputsearchkey(searchwords)
        self.beginsearch()
        self.resultTab_click(tab)
        self.selectfirstone(selectitem)

