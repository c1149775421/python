#coding=utf-8
from selenium import webdriver
import os,time
a = webdriver.Chrome()#启动谷歌浏览器
a.get("http://www.baidu.com")#访问百度
a.find_element_by_id("kw").send_keys("hello")#输入搜索内容
# a.find_element_by_class("ans-videoquiz-opts")[0].click()
time.sleep(3)#等待3秒点击
a.find_element_by_id('su').click()#点击搜索
time.sleep(5)#等待5秒关闭
a.quit()