#-*- coding:utf-8 -*-
import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


f = open("/home/xuna/桌面/res/weibo_list.txt",'w')
sum = 1
for page in range(1,67):
    #http://www.1000t.org/luntan_list.php?page=2
    url = "http://www.1000t.org/weibo_list.php?page="+str(page)
    driver = webdriver.Chrome()
    driver.set_window_size(200,200) #设置浏览器窗口的大小
    driver.get(url)

    for n in range(2,22):#2-21
        #/html/body/div/table/tbody/tr[2]/td[2]/a/html/body/div/table/tbody/tr[21]/td[2]
        name_xpath = '/html/body/div/table/tbody/tr[' + str(n) + ']/td[2]'
        name = driver.find_element_by_xpath(name_xpath).text
        f.write(name + "\n")
        print sum,name
        if sum == 1305:
            break
        sum = sum + 1
    driver.close()
