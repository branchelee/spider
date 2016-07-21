#coding:utf-8
import re,urllib,urllib2,requests
import ssl
from functools import wraps
from PIL import Image
#获取投融通投资列表页面中的产品URL
page = 1
urllist1 = []
url = 'https://www.xztrt.com/invest/index.html?page=%d' %page
def GetProductURL(url): #从URL里面找到产品列表URLlist
	req = requests.get(url)
	# req1 = urllib2.urlopen(url)
	html = req.text
	startstr = 'listmain clearfix'#从这个文字后面开始zhao
	endstr = u'转到'#从这个前面找
	startposition = html.find(startstr)
	endposition = html.find(endstr)
	# print startposition,endposition
# print html[startposition:endposition]
	reg = r'<a href="(.+?)"+?'
	regcompile = re.compile(reg)
	urllist = re.findall(regcompile, html[startposition:endposition])
	return urllist
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
logintrt()
# validpage = 'https://www.xztrt.com/validimg.html'
# urllib.urlretrieve(validpage,r"valid"+".jpg")
# validpage = requests.get(validpage)
# image = image.open("https://www.xztrt.com/validimg.html")
# image.show()
# print validpage.text






