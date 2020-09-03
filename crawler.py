import requests
from bs4 import BeautifulSoup
import os
import time

def isactual(base_url='http://gimnazy10.ru/index/0-14', url):
	response = requests.get(base_url)
	html_doc = response.text
	soup = BeautifulSoup(html_doc, 'html.parser')
	for link in soup.find_all('a'):
		if (str(link.get('href')).endswith(".pdf")):
			f = SCHEDULE_URL + link.get('href')
			break
	if f != url:
		return True
	else:
		return False