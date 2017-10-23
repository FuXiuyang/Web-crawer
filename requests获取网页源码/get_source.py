#-*- coding:utf-8 -*-

import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

file = open("/home/xuna/桌面/code/尤飞赌博网站.txt","r")
temp = open("/home/xuna/桌面/code/temp.txt","w")
n = 1
for url in file:
    try:
        t = url
        print url
        save_name ="/home/xuna/桌面/res/"+ url+".html"
        url = "http://" + url.replace("\r\n", "")
        html = requests.get(url)
        print n

        out = open(save_name,"w")
        s = str((html.text))

        out.write(s)

        n = n + 1
    except:
        temp.write(t)
