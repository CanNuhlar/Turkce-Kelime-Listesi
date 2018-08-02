# -*- coding: utf-8 -*-
import requests
from HTMLParser import HTMLParser
import re

class PageNumParser(HTMLParser):
	def handle_data(self, data):
		if "sayfanın" in data:
			getContent(int(re.search(r'\d+', data).group()))
class wordParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
	        if tag == "a" and len(attrs) == 1:
			for attr in attrs:
				word = re.search(r"kelime=(.*)&cesit", attr[1])
				print word.group(1)

def getContent(totalPageCount):
	currentPage = 0
	while totalPageCount > currentPage/60:
		pageURL = "http://tdk.gov.tr/index.php?option=com_yazimkilavuzu&view=yazimkilavuzu&kelime1=z&kategori1=yazim_listeli&ayn1=bas&konts=" + str(currentPage)
		response = requests.get(pageURL, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}, timeout=15)
		wordParser.feed(response.content.split('<table border="1" cellspacing="0" width="100%">')[1].split("</table>")[0])
		currentPage = currentPage + 60

pageNumParser = PageNumParser()
wordParser = wordParser()

pageURL = "http://tdk.gov.tr/index.php?option=com_yazimkilavuzu&view=yazimkilavuzu&kelime1=z&kategori1=yazim_listeli&ayn1=bas&konts=0"
response = requests.get(pageURL, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}, timeout=15)
pageNumParser.feed(response.content.split('<span class="comicm">')[1].split("</span>")[0])

