import requests
import string
import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen

from datetime import datetime
import sys
import json
import base64

path = "http://lostiempos.com"
client = requests.Session()
# SOLO ÚLTIMAS NOTICIAS #
url = 'http://lostiempos.com/ultimas-noticias'
page = '0'
#page = sys.argv[1]

html = client.get(url+'?page='+page)
soup = BeautifulSoup(html.content, 'html.parser')

news = soup.select(".noticias-lt-block .views-row")
data=[]
for new in news:
	dateNew = new.select(".views-field-field-noticia-fecha .date-display-single")[0].string
	dateNewArray = dateNew.split("-")
	dateNewDate = dateNewArray[0].strip()
	dateNewHour = dateNewArray[1].strip()

	categoryNew = new.select(".views-field-seccion")[0].string
	titleNew = new.select(".views-field-title a")[0]
	titleNewText = titleNew.string
	titleNewUrl = titleNew.get('href')

	resumeNew = new.select(".views-field-field-noticia-sumario .field-content")[0].string
	picNew = new.select(".views-field-field-noticia-fotos .field-content img")[0].get('src')

	newArray = {
		'title':titleNewText,
		'resume':resumeNew,
		'img':picNew,
		'url':titleNewUrl,
		'date-post':dateNewDate,
		'hour-post':dateNewHour,
		'category':categoryNew
	}
	data.append(newArray)
#print(data)
jsonData = json.dumps(data)
print(jsonData)