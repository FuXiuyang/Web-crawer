#coding:utf-8
import pymysql,sys,os,time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

"""
http://www.yiduoxiaohua.com/
"""
def yiduoxiaohua():
    f = open("韦小宝工作室.txt",'w')
    sum = 1
    url = "http://www.yiduoxiaohua.com/"
    driver = webdriver.Chrome()
    driver.set_window_size(400,400) #设置浏览器窗口的大小
    driver.get(url)

    for n in range(3,41):#2-21
        try:
            title = driver.find_element_by_xpath('//*[@id="goods"]/table/tbody/tr[' + str(n) + ']/td[1]').text
            price = driver.find_element_by_xpath('//*[@id="goods"]/table/tbody/tr[' + str(n) + ']/td[2]').text
            stock = driver.find_element_by_xpath('//*[@id="goods"]/table/tbody/tr[' + str(n) + ']/td[3]').text

            tmp_str = title + "_&_" + price + "_&_" + stock + "\n"
            f.write(tmp_str + "\n")
            print sum,title,price,stock
        except:
            pass
        sum = sum + 1
    driver.close()

"""
http://muzexi.51ddyx.com/index.action
"""
def muzexi():
    f = open("沐泽熙发卡网.txt",'w')
    sum = 1
    url = "http://muzexi.51ddyx.com/index.action"
    driver = webdriver.Chrome()
    driver.set_window_size(400,400) #设置浏览器窗口的大小
    driver.get(url)
    for n in range(1,36):#2-21
        try:
            title = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[' + str(n) + ']/td[1]').text
            price = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[' + str(n) + ']/td[2]').text
            stock = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[' + str(n) + ']/td[3]').text

            tmp_str = title + "_&_" + price + "_&_" + stock + "\n"
            f.write(tmp_str + "\n")
            print sum,title,price,stock
        except:
            print "cuowu"
        sum = sum + 1
    driver.close()

"""
http://py.shiguangka.com/
"""
def shiguangka():

    f = open("时光，影视.txt",'w')
    sum = 1
    url = "http://py.shiguangka.com/"
    driver = webdriver.Chrome()
    driver.set_window_size(400,400) #设置浏览器窗口的大小
    driver.get(url)

    for n in range(1,44):#2-21
        try:
            title = driver.find_element_by_xpath('//*[@id="goods"]/table/tbody/tr[' + str(n) + ']/td[1]').text
            price = driver.find_element_by_xpath('//*[@id="goods"]/table/tbody/tr[' + str(n) + ']/td[2]').text
            stock = driver.find_element_by_xpath('//*[@id="goods"]/table/tbody/tr[' + str(n) + ']/td[3]').text

            tmp_str = title + "_&_" + price + "_&_" + stock + "\n"
            f.write(tmp_str + "\n")
            print sum,title,price,stock
        except:
            print "cuowu"
        sum = sum + 1
    driver.close()


def def_find(tmp):
    use_day = ""
    factory = ""
    num_class = "号"
    if tmp.find("1天") != -1:  use_day = "1天"
    if tmp.find("3天") != -1:  use_day = "3天"
    if tmp.find("7天") != -1:  use_day = "7天"
    if tmp.find("10天") != -1:  use_day = "10天"
    if tmp.find("一月") != -1:  use_day = "1月"
    if tmp.find("1月") != -1:  use_day = "1月"
    if tmp.find("35天") != -1:  use_day = "35天"
    if tmp.find("31天") != -1:  use_day = "31天"
    if tmp.find("30天") != -1:  use_day = "30天"
    if tmp.find("32天") != -1:  use_day = "32天"
    if tmp.find("3月") != -1:  use_day = "3月"
    if tmp.find("6月") != -1:  use_day = "6月"
    if tmp.find("1年") != -1:  use_day = "1年"


    if tmp.find("乐视") != -1: factory = "乐视"
    if tmp.find("腾讯") != -1: factory = "腾讯"
    if tmp.find("搜狐") != -1: factory = "搜狐"
    if tmp.find("芒果") != -1: factory = "芒果"
    if tmp.find("TX") != -1: factory = "腾讯"
    if tmp.find("爱奇") != -1: factory = "爱奇艺"
    if tmp.find("优酷") != -1: factory = "优酷"
    if tmp.find("PPTV") != -1: factory = "PPTV"
    if tmp.find("CDK") != -1: num_class = "CDK"
    if tmp.find("cdk") != -1: num_class = "CDK"

    return use_day,factory,num_class

def install_mysql(file_name,url):

    conn = pymysql.connect(
                       host = '****',
                       port = 3306,  #注意端口号为数字类型，其余都为字符串
                       user = '****',
                       passwd = '******',
                       db = '****',
                       charset = 'utf8'
                       )
    cur = conn.cursor()
    f = open(file_name,'r')
    f = f.readlines()
    for line in f :
        if line !="\n" != -1:
            st = line.split("_&_")

            id = time.strftime("%Y%m%d", time.localtime()).encode('utf-8')
            title_str = st[0]
            max_num = st[2]
            price = st[1]
            remark = url
            use_day = ""
            factory = ""
            num_class = ""
            use_day,factory,num_class = def_find(title_str)
            sql_insert = "insert into kameng values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(id, title_str, max_num, price, remark, use_day, factory,num_class)
            print(sql_insert)
            cur.execute(sql_insert)


    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    yiduoxiaohua()
    shiguangka()
    muzexi()
    install_mysql("韦小宝工作室.txt","http://www.yiduoxiaohua.com/")
    install_mysql("时光，影视.txt","http://py.shiguangka.com/")
    install_mysql("沐泽熙发卡网.txt","http://muzexi.51ddyx.com/index.action")
