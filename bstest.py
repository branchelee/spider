# -*- coding: UTF-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib2
url = 'https://www.xztrt.com/invest/index.html?sState=all&sApr=all&sLimit=all&sAccount=all&search=union'
html = urllib2.urlopen(url)
bsobj = BeautifulSoup(html.read())
print bsobj.body
