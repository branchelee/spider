#coding:utf-8
import os,re,urllib,uuid
import urllib
import urllib2
import requests
import random

req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
}
url = 'http://t1.du114.com/uploads/tu/201603/wmm9000/3.jpg'
url2 = 'http://www.rosioo.com/'
req_timeout = 2
req = urllib2.Request(url2,None,req_header)
resp = urllib2.urlopen(req,None,req_timeout)
html = resp.read()
print(html)



urllib.urlretrieve(url,r"/Users/branche/Desktop/tmp/"+"test3"+".jpg")
# f = urllib2.urlopen("http://www.rosiyy.com/")
# print url
# for alnum in range(1310,1319):
# 	for imgnum in range(0,9):
# 		url = "http://www.beautylegmm.com/photo/beautyleg/2016/%d/beautyleg-%d-000%d.jpg" % (alnum,alnum,imgnum)
