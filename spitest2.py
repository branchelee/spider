#encoding:utf-8
import os,re,urllib,uuid
import urllib
import urllib2
import requests
import random
#用地址组装的方法下载图片
alnum = 1318
imgnum = 0
url = "http://www.beautylegmm.com/photo/beautyleg/2016/%d/beautyleg-%d-000%d.jpg" % (alnum,alnum,imgnum)

print url
for alnum in range(1250,1301):
	for imgnum in range(0,10):
		url = "http://www.beautylegmm.com/photo/beautyleg/2016/%d/beautyleg-%d-000%d.jpg" % (alnum,alnum,imgnum)
		print "downloading ",url
		urllib.urlretrieve(url,r"/Users/branche/Desktop/tmp/"+str(alnum)+str(imgnum)+".jpg")