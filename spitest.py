# -*- coding: UTF-8 -*-  
#实现自动抓取网站首页中，链接向XXXX.HTM页面内的图片77tuba
import os,re,urllib,uuid
import urllib
import urllib2
import requests
import random
url1 = "https://mm.taobao.com/json/request_top_list.htm?page=1"
url2 = "http://tieba.baidu.com/p/2166231880"
url3 = "http://www.rosiyy.com/xiaoxiaona/rosi1629.html"
url4 = "https://www.baidu.com/"
url5 = "http://tech.hexun.com/2016-07-16/184966921.html"
url6 = "https://www.zhihu.com/question/19647535"
url7 = "http://www.cqjjnet.com/"
url8 = "http://www.beautylegmm.com/"
url9 = "https://www.twitter.com"
url10 = "http://www.beautylegmm.com/Dora/beautyleg-1319.html"
url11 = "http://www.beautylegmm.com/"
url12 = "http://www.77tuba.com/1047/20160529/77611.shtml"

pagenum = 1
pagestart = 1319
pageend = 1300

#当前使用的url
urlnow = url11

# r = requests.get('https://www.google.com')
#print r.text
filename = 1
#获取页面html内容
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
#获取当前页面的URL列表,
def geturllist(html):
	#获取结尾为4位数字的HTML链接
	regurl = r'href="(.+?[0-9]{4}\.html)"'
	urlre = re.compile(regurl)
	urllist = re.findall(urlre,html)
	return urllist
#获取页面内图片链接
def getImg(html):
	# global urlnow
    # reg = r'img src="(.+?\.jpg)" pic_ext'  
    reg = r'src="(.+?\.jpg)"'
    # reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    for i in range(0,len(imglist)):   
    	imglist[i] = urlnow+imglist[i]
    	print imglist[i]
    return imglist

#html = getHtml(url)
# print r.text
#从某个页面下载页面内的图片，参数为URL
def saveImgFromURL(url):
	r = requests.get(url)
	img = getImg(r.text)
	print img
	for i in img:
		print i
		filename = random.randrange(1000000,2000000)
		urllib.urlretrieve(i,r"./"+str(filename)+".jpg")
	return url
#从图片list里面批量下载图片
def saveImgFromList(list):
	for i in list:
		print i
		filename = random.randrange(1000000,2000000)
		urllib.urlretrieve(i,r"./"+str(filename)+".jpg")
	return url

#下载指定URL的图片程序
for n in range(1250,1350):
	url11 = "http://www.beautylegmm.com/Dora/beautyleg-%d.html" %pagestart
	print "trying to fetch page %d"%n
	saveImgFromURL(url11)







