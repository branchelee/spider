#coding:utf-8
import re,urllib,urllib2,requests
import ssl,simplejson
#simplejson用于将str格式的{}转为dict格式
from functools import wraps
from PIL import Image
#获取12306剩余车票数量

url = 'https://kyfw.12306.cn/otn/lcxxcx/init'

def Savetofile(endpage):#保存文件到txt，参数为结束页页号
	global urllist1
	for page in range (1,endpage+1):
		print 'getting page %d' %page
		url = 'https://www.xztrt.com/invest/index.html?page=%d' %page
		urllist1 = urllist1 + list(set(GetProductURL(url)))
	print len(urllist1)
	f = open("trtproduct.txt",'wb')
	for i in urllist1:
		i = 'https://www.xztrt.com/'+i
		f.write(i+'\n')
	f.close
# Savetofile(2)
def logintrt():
	ProductURL = 'https://www.xztrt.com//invest/detail.html?id=b4716901-9d71-47ef-a3c6-40b0047bc367'
	# print requests.get(url11).text
	validpage = 'https://www.xztrt.com/validimg.html'
	loginurl = 'https://www.xztrt.com/user/login.html'

	s = requests.session()
	#获取验证码并保存到本地
	urllib.urlretrieve(validpage,r"valid"+".jpg")
	Image.open(r"valid.jpg").show()
	#输入验证码
	validCode = raw_input('please input validcode')
	# validCode = "1234"
	data = {'user':'test111','password':'lxyx520123','validCode':validCode}
	
	#post 换成登录的地址，
	res=s.post(loginurl,data)
	#换成抓取的地址
	
	req = s.get(ProductURL)
	print req.text
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
	listall = re.findall(recompile, req.content[85:-1])
	# print listall[0]
	#把listall里面的转为dict格式方便读写
	for i in range(0,len(listall)):
		listall[i] = simplejson.loads(listall[i])

	return listall
querydate = '2016-07-29'
from_station = 'CUW'
to_station = 'ICW'
listall = get_train_list(querydate,from_station,to_station)

print listall[4]['station_train_code']

# validpage = 'https://www.xztrt.com/validimg.html'
# urllib.urlretrieve(validpage,r"valid"+".jpg")
# validpage = requests.get(validpage)
# image = image.open("https://www.xztrt.com/validimg.html")
# image.show()
# print validpage.text






