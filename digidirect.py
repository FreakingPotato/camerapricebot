from parseprice import ParsePrice
import bs4
import requests
from bs4 import BeautifulSoup

class parseDigiDirectPrice(ParsePrice):
    def __init(self,url):
        super().__init__(url)
    
    def parsePrice(self):
        if len(self.url) != 0:
            r = requests.get(self.url)
            price_list = []
            soup = bs4.BeautifulSoup(r.text,"lxml")
            price = soup.find_all('div',{'class':'price-box price-final_price'})[0].find_all('span',{'class':'price'})
            for x in price:
                y = self.parseString(x.text)
                price_list.append(y)
            return min(price_list)
        else: 
            return 0
    
    company = 'DigiDirect'