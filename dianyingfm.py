# -*- coding: UTF-8 -*-  
from bs4 import BeautifulSoup
import urllib,csv
#解决编码写入错误的问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#定义母页面

filmdic = {}
def getfilmdic(url):
	#从一个url获取电影基本信息，返回dic
	html = urllib.urlopen(url)
	bsobj = BeautifulSoup(html,'html.parser')

	filmdic['filmurl'] = url
	filmdic['FilmName'] = bsobj.h3.get_text()
	#lstrip为去除左边的空格
	filmdic['Douban'] = bsobj.find('a','fm-green').get_text().lstrip()[3:-1]
	filmdic['IMDB'] = bsobj.find('a','fm-orange').get_text().lstrip()[5:-1]
	#bsobj.findAll('dd')存储影片概要信息，其中0为导演，1为主演,2为出产国，3为上映时间，4为片长，5为其他地区翻译
	filmdic['director'] = bsobj.findAll('dd')[0].get_text()
	filmdic['actors'] = bsobj.findAll('dd')[1].get_text()
	filmdic['country'] = bsobj.findAll('dd')[2].get_text()
	filmdic['oncenimatime'] = bsobj.findAll('dd')[3].get_text()
	filmdic['lenth'] = bsobj.findAll('dd')[4].get_text()
	filmdic['others'] = bsobj.findAll('dd')[5].get_text()
	#filminfo存储影片概要信息，其中0为导演，1为主演,2为出产国，3为上映时间，4为片长，5为其他地区翻译
	info = bsobj.findAll('dd')
	#filmbrief为影片简介
	filmdic['brief'] = bsobj.find('div','fm-summary').get_text()
	return filmdic
def getfilmdiclist(url):
	#从一个url获取电影基本信息，返回list
	html = urllib.urlopen(url)
	bsobj = BeautifulSoup(html,'html.parser')

	filmdic['filmurl'] = url
	filmdic['FilmName'] = bsobj.h3.get_text()
	#lstrip为去除左边的空格
	filmdic['Douban'] = bsobj.find('a','fm-green').get_text().lstrip()[3:-1]
	filmdic['IMDB'] = bsobj.find('a','fm-orange').get_text().lstrip()[5:-1]
	#bsobj.findAll('dd')存储影片概要信息，其中0为导演，1为主演,2为出产国，3为上映时间，4为片长，5为其他地区翻译
	filmdic['director'] = bsobj.findAll('dd')[0].get_text()
	filmdic['actors'] = bsobj.findAll('dd')[1].get_text()
	filmdic['country'] = bsobj.findAll('dd')[2].get_text()
	filmdic['oncenimatime'] = bsobj.findAll('dd')[3].get_text()
	filmdic['lenth'] = bsobj.findAll('dd')[4].get_text()
	filmdic['others'] = bsobj.findAll('dd')[5].get_text()
	#filminfo存储影片概要信息，其中0为导演，1为主演,2为出产国，3为上映时间，4为片长，5为其他地区翻译
	info = bsobj.findAll('dd')
	#filmbrief为影片简介
	filmdic['brief'] = bsobj.find('div','fm-summary').get_text()
	filmdiclist = []
	for key in filmdic:
		filmdiclist.append(filmdic[key])
	return filmdiclist
def getfilminfolist(url):
	filminfo
#调用getfilmdic函数获取到电影信息字典

# filmlist1 = [filmdic]
# dictest = {'Douban':'a', 'filmurl':'a', 'FilmName':'a', 'country':'a', 'others':'a', 'brief':'a', 'director':'a', 'actors':'a', 'oncenimatime':'a', 'IMDB':'a', 'lenth':'a'}


fieldnames = ['Douban', 'filmurl', 'FilmName', 'country', 'others', 'brief', 'director', 'actors', 'oncenimatime', 'IMDB', 'lenth']
#dict_writer方法
def WriteDicToCsv(filmdic):
	#将字典filmdic写入到scan1.csv中,参数为list，格式为[{},{},{}]
	dict_writer = csv.DictWriter(file('./dianyingfm/scan1.csv', 'ab+'), fieldnames=fieldnames)
	# dict_writer.writerow(fieldnames) # CSV第一行需要自己加入
	dict_writer.writerows(filmdic)  
def WriteListToCsv(filmlist):
	writer = csv.writer(open('./dianyingfm/scan1.csv','ab+'))
	# fieldnames = ['Douban', 'filmurl', 'FilmName', 'country', 'others', 'brief', 'director', 'actors', 'oncenimatime', 'IMDB', 'lenth']
	# writer.writerow(fieldnames)
	writer.writerow(filmlist)
def getchildlist(urlparent):
	#从总览页面获取子页面URL LIST
	htmlparent = urllib.urlopen(urlparent)
	bsparent = BeautifulSoup(htmlparent,'lxml')
	filmdicall = []

	# childlist = bsparent.select('.fm-movie-title')
	childlistbs = bsparent.find_all(class_='fm-movie-title')
	for i in childlistbs:
		# print i.a['href']
		urlchild = 'http://dianying.fm' + i.a['href']
		childlist.append(urlchild)
	return childlist
	#用父地址查找子电影地址

#用于写文件头
# WriteListToCsv(fieldnames)

#把该电影写入文件
# filmdic = [getfilmdic(urlchild)]
# WriteDicToCsv(filmdic) 
childlist = []
for p in range(1,100):
	urlparent = 'http://dianying.fm/search/?p=%d&region=美国' % p
	print 'getting',p
	try:
		childlist = getchildlist(urlparent)
	except Exception, e:
		raise
	else:
		pass
	finally:
		pass
	
f = open('urls.txt','wb')

for i in childlist:
	print i,'\n'
	f.write(i+'\n')
f.close()


	
# 写入到文件
# WriteDicToCsv(filmdicall)


