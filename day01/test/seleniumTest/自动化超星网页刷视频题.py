from selenium import webdriver as wd
import time

def main():
    #打开chrome浏览器
    a = wd.Chrome()
    #用浏览器访问url
    a.get("https://mooc1-1.chaoxing.com/mycourse/studentstudy?chapterId=165007921&courseId=215575849&clazzid=34620761&enc=328b1c3d379e9efc5c7e5bdd608148d1")
    
    time.sleep(10)
    
    b = a.find_elements_by_class_name("ncells")
    start = 30
    end = len(b)-1
    for i in range(start+1,end):
        try:
            time.sleep(1)
            cc = a.find_elements_by_class_name("ncells")
            ccc = cc[i]
            print(i)
            print(ccc.find_element_by_tag_name("h4").find_elements_by_tag_name("span")[1].text)
            time.sleep(1)
            ccc.click()
            if len(ccc.find_element_by_tag_name("h4").find_elements_by_tag_name("span")[1].text) == 1:
                # time.sleep(2)
                a.find_elements_by_class_name("ncells")[i].click()
                # a.find_elements_by_class_name("ncells")[i].double_click()#双击
                # time.sleep(2)
                # print(a.find_element_by_id("iframe").size["width"])
                # print(a.find_element_by_id("iframe").size["height"])
                time.sleep(5)
                a.find_element_by_id("iframe").click()
                time.sleep(480)
                continue
            else:
                continue
        except:
            print("error")
            continue



    
    #退出浏览器
    #a.quit()

main()

import os
os.system("pause")