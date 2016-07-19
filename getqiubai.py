#coding:utf-8
import re,urllib2,requests
req = requests.get('http://www.qiushibaike.com/')
f = open('qiushibaike.txt','wb')
# print req.text
str1 = "asdfasd<div class=\"content\">teststr1测试中文转码</div>asdfasdf"
print str1
reg = r'<div class="content">\n*(.+)\n*</div>'
urlre = re.compile(reg)
list1 = re.findall(urlre,str1)
listall = []
for page in range(1,12):
	print "getting page %d" %page
	url = "http://www.qiushibaike.com/8hr/page/%d/?s=4896305" %page
	req = requests.get(url)
	list2 = re.findall(urlre,req.text)
	listall = listall + list2
# print req.text
for i in listall:
	# i = i.decode('ascii')
	i = i.encode('utf-8')
	# print "list2 is ",i 
	f.write(i+"\n")
f.close()
