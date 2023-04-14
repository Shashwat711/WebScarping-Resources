
import requests
from bs4 import BeautifulSoup
  
URL = "https://www.guru99.com/web-scraping-tools.html"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())
table = soup.find('div', attrs = {'id':'1-bright-data-formerly-luminati-networks'}) 
print(table)