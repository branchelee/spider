# -*- coding: UTF-8 -*-  
#实现自动抓取网站首页中，链接向XXXX.HTM页面内的图片77tuba
import os,re,urllib,uuid
import urllib
import urllib2
import requests
import random
import bs4

url12 = "http://www.77tuba.com/1058/201608/78268.shtml"


pagenum = 1
pagestart = 1319
pageend = 1300

#当前使用的url
urlnow = url12

#r = requests.get('https://www.google.com')
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
def getImglist(html):
	# global urlnow
    # reg = r'img src="(.+?\.jpg)" pic_ext'  
    reg = r'src=\'(.+?\.jpg)'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    for i in range(0,len(imglist)):   
    	imglist[i] = 'http://www.77tuba.com/'+imglist[i]
    	# print imglist[i]
    return imglist

#html = getHtml(url)
# print r.text
#从某个页面下载页面内的图片，参数为URL
def saveImgFromURL(url):
	r = requests.get(url)
	img = getImglist(r.text)
	print img
	for i in img:
		print i
		filename = random.randrange(1000000,2000000)
		urllib.urlretrieve(i,r"./img77/"+str(filename)+".jpg")
	return url
#从图片list里面批量下载图片
def saveImgFromList(list):
	for i in list:
		print 'downloading',i 
		filename = random.randrange(1000000,2000000)
		urllib.urlretrieve(i,r"./img77/"+str(filename)+".jpg")
#找到当前页面总共有多少个下一页
def getTotalPage(html):
	reg = r'共.+?页'
	regcompile = re.compile(reg)
	TotalPage = re.findall(regcompile,html)
	return TotalPage
html = getHtml(urlnow)
# print html
imglist = getImglist(html)
# TotalPage = getTotalPage(html)
print TotalPage
# for i in imglist:
# 	print i
# 下载当前页面的图片
saveImgFromURL(urlnow)



