from parseprice import ParsePrice
import bs4
import requests
from bs4 import BeautifulSoup

class parseCameraProPrice(ParsePrice):
    def __init(self,url):
        super().__init__(url)
        
    def parsePrice(self):
        if len(self.url) != 0:
            r = requests.get(self.url)
            soup = bs4.BeautifulSoup(r.text,"lxml")
            price = soup.find_all('span',{'data-price-type':'finalPrice'})[0].text
            return self.parseString(price)
        else:
            return 0
        
    company = 'CameraPro'