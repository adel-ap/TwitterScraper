from BeautifulSoup import BeautifulSoup

import urllib2 
url = urllib2.urlopen("http://www.varzesh3.com")

content = url.read()

soup = BeautifulSoup(content)

links = soup.findAll("a")
print links
