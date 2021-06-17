import urllib.request as urllib2
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Vadivelu_filmography"
page = urllib2.urlopen(url)

a = BeautifulSoup(page, "html.parser")

main_text = a.find("table", class_="wikitable sortable")
print(main_text.text)