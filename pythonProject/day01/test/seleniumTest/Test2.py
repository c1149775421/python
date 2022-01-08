#coding=utf-8
from selenium import webdriver
import os,time
a = webdriver.Chrome()#启动谷歌浏览器
url="https://mooc1-1.chaoxing.com/mycourse/studentstudy?chapterId=165007921&courseId=215575849&clazzid=34620761&enc=328b1c3d379e9efc5c7e5bdd608148d1"
a.get(url)#访问百度
time.sleep(10)
bb = a.find_elements_by_class_name("ncells")
lenn=len(bb)
for i in range(lenn):
    a.find_elements_by_class_name("ncells")[i].click()
    cc = a.find_elements_by_class_name("ncells")
    ccc=cc[i]
    if len(ccc.find_element_by_tag_name("h4").find_elements_by_tag_name("span")[1].text)==1:
        select.click()
    else:
        continue

time.sleep(3)#等待3秒点击
select=a.find_element_by_id("iframe")
