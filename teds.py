from parseprice import ParsePrice
import bs4
import requests
from bs4 import BeautifulSoup

class parseTedsPrice(ParsePrice):
    def __init(self,url):
        super().__init__(url)
    
    def parsePrice(self):
        r = requests.get(self.url)
        soup = bs4.BeautifulSoup(r.text,"html")
        price = soup.find_all('div',{'class':'price-box'})[0].find('meta')['content']
        price = str('$')+str(price)
        return self.parseString(price)

    company = 'Teds'