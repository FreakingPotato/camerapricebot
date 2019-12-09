from parseprice import ParsePrice
import bs4
import requests
from bs4 import BeautifulSoup

class parseDigiDirectPrice(ParsePrice):
    def __init(self,url):
        super().__init__(url)
    
    def parsePrice(self):
        r = requests.get(self.url)
        price_list = []
        soup = bs4.BeautifulSoup(r.text,"html")
        price = soup.find_all('div',{'class':'price-box price-final_price'})[0].find_all('span',{'class':'price'})
        for x in price:
            price_list.append(x.text)
        return self.parseString(min(price_list))
    
    company = 'DigiDirect'