#coding:utf-8
import pymysql,sys,os,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pyvirtualdisplay import Display #配置无界面chrome用
import sys
reload(sys)
sys.setdefaultencoding("utf8")

"""
http://yyssxx.cn/
"""
def  get_data():

    f = open("yyssxx.cn.txt",'w')
    sum = 1
    url = "http://yyssxx.cn/"
    print(url)
    display = Display(visible=0, size=(800, 600))
    display.start()
    driver = webdriver.Chrome()
    driver.set_window_size(800,600) #设置浏览器窗口的大小
    driver.get(url)
    print("begin")

    for n in range(2,46):
        try:
            print(n)
            title = driver.find_element_by_xpath('//*[@id="body"]/table/tbody/tr[' + str(n) + ']/td[1]/div/font').text
            price = driver.find_element_by_xpath('//*[@id="body"]/table/tbody/tr[' + str(n) + ']/td[2]').text
            stock = driver.find_element_by_xpath('//*[@id="body"]/table/tbody/tr[' + str(n) + ']/td[3]/font').text
            tmp_str = title + "_&_" + price + "_&_" + stock + "\n"
            f.write(tmp_str )
            print sum,title,price,stock
        except Exception,e:
            print(e)
            pass
        sum = sum + 1
    driver.close()
    f.close()


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
                       host = '127.0.0.1',
                       port = 3306,  #注意端口号为数字类型，其余都为字符串
                       user = '***',
                       passwd = '*****',
                       db = '****',
                       charset = 'utf8'
                       )
    cur = conn.cursor()
    print "1"
    f1 = open(file_name,'r')
    f = f1.readlines()
    for line in f :
        if line !="\n" != -1:
            st = line.split("_&_")

            id = time.strftime("%Y%m%d", time.localtime()).encode('utf-8')
            title_str = st[0]
            max_num = st[2].replace("个","")
            price = st[1].replace("元","")
            remark = url
            use_day = ""
            factory = ""
            num_class = ""
            use_day,factory,num_class = def_find(title_str)
            sql_insert = "insert into kameng values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(id, title_str, max_num, price, remark, use_day, factory,num_class)
            print(sql_insert)
            cur.execute(sql_insert)

    f1.close()
    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    get_data()
    install_mysql("yyssxx.cn.txt","http://yyssxx.cn/")
