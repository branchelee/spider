# coding:utf-8
import os,re,urllib,uuid
import urllib
import urllib2
import requests
import random

url = "http://www.runoob.com/"
#获取URL页面内链接的HTML页面列表，返回list
def geturllist(url):

	html = requests.get(url)
	# print html.text
	urlre = r'href="(http.{0,100}\.html)"'
	urlrecompile = re.compile(urlre)
	urllist = re.findall(urlrecompile,html.text)
	urllist = list(set(urllist))
	return urllist

list1 = geturllist(url)
listall = []
for n in list1:
	print "getting ",n
	listtmp = geturllist(n)
	listall = listall + listtmp
listall = list(set(listall))
	
print len(listall)
