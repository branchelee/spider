# -*- coding: UTF-8 -*-  
from bs4 import BeautifulSoup
import urllib
#定义母页面
urlparent = 'http://dianying.fm/search/?text=%E9%92%A2%E9%93%81%E4%BE%A0'

urlchild = 'http://dianying.fm/movie/iron-man/'
html = urllib.urlopen(urlchild)
bsobj = BeautifulSoup(html,'html.parser')

FilmName = bsobj.h3.get_text()
#lstrip为去除左边的空格
Douban = bsobj.find('a','fm-green').get_text().lstrip()[2:-1]
IMDB = bsobj.find('a','fm-orange').get_text().lstrip()[4:-1]
director = 1
actors = bsobj.find('dt').next
#filminfo存储影片概要信息，其中0为导演，1为主演,2为出产国，3为上映时间，4为片长，5为其他地区翻译
FilmInfo = bsobj.findAll('dd')
#filmbrief为影片简介
FilmBrief = bsobj.find('div','fm-summary')


print FilmBrief.get_text().encode('UTF-8')
for i in range(0,len(FilmInfo)):
	print i,FilmInfo[i].get_text().encode('UTF-8')
