# -*- coding: UTF-8 -*-  
#实现自动抓取网站首页中，链接向XXXX.HTM页面内的图片meinv58
import os,re,urllib,uuid,time
import urllib
import urllib2
import requests
import random
from bs4 import BeautifulSoup
 #子页面


url12 = "http://www.77tuba.com/1058/201608/78268.shtml"
urlchild = 'http://www.meinv58.com/xinggan/2907'
urlparent = 'http://www.meinv58.com/tag/刘飞儿'

pagenum = 1
pagestart = 1319
pageend = 1300

#当前使用的url
urlnow = urlchild

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
	regurl = r'href=\'(.+?)\''
	# href="http://www.meinv58.com/xinggan/3007" class="imageLink image"
	urlre = re.compile(regurl)
	urllist = re.findall(urlre,html)
	return urllist
#获取页面内图片链接
def getImglist(html):
	# global urlnow
    # reg = r'img src="(.+?\.jpg)" pic_ext'  
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    for i in range(0,len(imglist)):   
    	imglist[i] = imglist[i]
    	# print imglist[i]
    return imglist

#html = getHtml(url)
# print r.text
#从某个页面下载页面内的图片，参数为URL，在0:15000内下载是为了不下载sidebar内容
def saveImgFromURL(url):
	r = requests.get(url)
	img = getImglist(r.text[0:15000])
	print img
	for i in img:
		# print i
		filename = random.randrange(1000000,2000000)
		urllib.urlretrieve(i,r"./img58/3/"+str(filename)+".jpg")
	return url
def saveImgFromURL_BS(url,filenamestart,filename):
	#用beautiful库下载图片
	r = urllib.urlopen(url)
	bsobj = BeautifulSoup(r,'lxml')
	imglist = bsobj.findAll('img',width='700')
	for i in imglist:
		# print i
		# filename = random.randrange(100,200)

		try:
			urllib.urlretrieve(i['src'],r"./img58/3/"+str(filenamestart)+'_'+str(filename)+".jpg")

		except Exception, e:
			raise

		
	return url
#从图片list里面批量下载图片
def saveImgFromList(list):
	for i in list:
		# print 'downloading',i 
		filename = random.randrange(1000000,2000000)
		urllib.urlretrieve(i,r"./img58/3/"+str(filename)+".jpg")
#找到当前页面总共有多少个下一页
def getTotalPage(html):
	reg = r'共.+?页'
	regcompile = re.compile(reg)
	TotalPage = re.findall(regcompile,html)
	return TotalPage

# print html
# imglist = getImglist(html[0:15000])
# for i in imglist:
# 	print i
# TotalPage = getTotalPage(html)
# print TotalPage

# # 下载当前页面的图片,取8000:33000是为了不要前面的和后面的sidebar的内容
urlparent = 'http://www.meinv58.com/tag/刘飞儿'
urlparent1 = 'http://www.meinv58.com/xinggan/page/1'
urlparent2 = 'http://www.meinv58.com/xinggan/page/2'
urlparent3 = 'http://www.meinv58.com/tag/熊吖bobo'
urlparent4 = 'http://www.meinv58.com/xinggan/page/4'

for totalpage in range(2400,2990):
	for childpagenum in range (1,11):
		urlnow = 'http://www.meinv58.com/xinggan/%d/%d' % (totalpage,childpagenum)

		print 'downloading',urlnow
		try:
			filename = childpagenum
			saveImgFromURL_BS(urlnow,totalpage,filename)
			time.sleep(0.1)
		except Exception, e:
			pass
		else:
			pass
		finally:
			pass
		




