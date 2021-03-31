# -*- coding: utf-8 -*-

from src.common import basepage
from appium.webdriver.common import mobileby
import time

class search(basepage.Base_page):
    by=mobileby.MobileBy()
    #搜索框
    searchButton=(by.ID,"com.shinyv.cnr:id/layout_search")
    #点击搜索框后的框
    etsearch=(by.ID,"com.shinyv.cnr:id/et_search")
    #搜索按钮
    beginsearchbutton=(by.ID,"com.shinyv.cnr:id/search_top_text")
    #搜索结果第一个位置
    firstresult=(by.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]")

    def searchbuttonclick(self):
        self.find_element(*self.searchButton).click()
    #输入搜索词
    def inputsearchkey(self,keyword):
        self.send_keys(keyword,*self.etsearch)
    #开始搜索
    def beginsearch(self):
        self.find_element(*self.beginsearchbutton).click()
    #选择搜索结果第一个
    def selectfirstone(self):
        self.find_element(*self.firstresult).click()
    #包装，搜索关键词并对结果选择
    def searchkeywords_firstone(self,keywords):
        self.searchbuttonclick()
        time.sleep(2)
        self.inputsearchkey(keywords)
        time.sleep(2)
        self.beginsearch()
        time.sleep(3)
        self.selectfirstone()

