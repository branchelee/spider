# -*- coding: UTF-8 -*-
import re,urllib,urllib2,requests
import ssl,simplejson
#simplejson用于将str格式的{}转为dict格式
from functools import wraps
from PIL import Image
import position12306

#获取12306剩余车票数量

url = 'https://kyfw.12306.cn/otn/lcxxcx/init'



def get12306():
	validpage = 'https://www.xztrt.com/validimg.html'
	url = 'https://kyfw.12306.cn/otn/lcxxcx/init'

	#获取验证码并保存到本地
	# urllib.urlretrieve(validpage,r"valid"+".jpg")
	# Image.open(r"valid.jpg").show()
	#输入验证码
	# validCode = raw_input('please input validcode')
	# validCode = "1234"
	data = {'train_station_name':'重庆北','_to_station_name':'成都东','train_start_date':'2016-07-29'}
	
	#post 换成登录的地址，
	#换成抓取的地址
	data = urllib.urlencode(data)
	print data
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()
	print the_page

	print res.text
def posttest():
	url = 'http://umbra.nascom.nasa.gov/cgi-bin/eit-catalog.cgi'
	values = {'obs_year':'2011','obs_month':'March',
	                             'obs_day':'8','start_year':'2011'
	                             ,'start_month':'March','start_day':'8'
	                             ,'start_hour':'All Hours','stop_year':'2011'
	                             ,'stop_month':'March','stop_day':'8'
	                             ,'stop_hour':'All Hours','xsize':'All'
	                             ,'ysize':'All','wave':'all'
	                             ,'filter':'all','object':'all'
	                             ,'xbin':'all','ybin':'all'
	                             ,'highc':'all'}
	data = urllib.urlencode(values)
	print data
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()
	print the_page
def get_train_list(querydate,from_station,to_station):
	'输入查询日期、起点站、到达站获取列车列表'
	urlget = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=%s&from_station=%s&to_station=%s' %(querydate,from_station,to_station)
	req = requests.get(urlget)
	re1 = r'{.+?}'
	recompile = re.compile(re1)
	#找到网页内所有的车次，从85位字符起读
	# htmluni = req.content[85:-1]
	# htmlutf = htmluni.encode('utf-8')
	html = req.content[85:-1]
	listall = re.findall(recompile,html)
	# print listall[0]
	#把listall里面的转为dict格式方便读写
	for i in range(0,len(listall)):
		listall[i] = simplejson.loads(listall[i])

	return listall
#从list的所有dict中输出序号车次等信息
def output(listall):
	for i in range(0,len(listall)):
		print '序号%d,车次：%s，出发时间：%s，到达时间%s，一等座%s，二等座%s'\
				%	(i,\
					listall[i]['station_train_code'],\
					listall[i]['start_time'],\
					listall[i]['arrive_time'],\
					listall[i]['zy_num'].encode('utf-8'),\
					listall[i]['ze_num'].encode('utf-8'),\
					)

querydate1 = '2016-08-16'
from_station_chn = raw_input('from where:')
print from_station_chn

from_station = position12306.find_position_names(from_station_chn)
print from_station
to_station_chn = raw_input('去哪儿:')
querydate = raw_input('哪天出发，例如2016-08-12:')

from_station = position12306.find_position_names(from_station_chn)
print 'from_station is:',from_station
to_station = position12306.find_position_names(to_station_chn)	
print 'to_station is:',to_station
	# print position_eng
listall = get_train_list(querydate1,from_station,to_station)

output(listall)
'''
station_train_code = '车次'
start_time = '出发时间'
arrive_time = '到达时间'
from_station_name = '出发站'
to_station_name = '到达站'
swz_num = '商务座'
tz_num = '特等座'
zy_num = '一等座'
ze_num = '二等座'
gr_num = '高级软卧'
rw_num = '软卧'
yw_num = '硬卧'
rz_num = '软座'
yz_num = '硬座'
wz_num = '无座'



'''
# validpage = 'https://www.xztrt.com/validimg.html'
# urllib.urlretrieve(validpage,r"valid"+".jpg")
# validpage = requests.get(validpage)
# image = image.open("https://www.xztrt.com/validimg.html")
# image.show()
# print validpage.text






