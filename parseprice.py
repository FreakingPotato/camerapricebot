import bs4
import requests
from bs4 import BeautifulSoup

class ParsePrice:
    def __init__(self,url):
        self.url = url        
        
    def parsePrice(self):
        if len(self.url) != 0:
            r = requests.get(self.url)
            soup = bs4.BeautifulSoup(r.text,"lxml")
            price = soup.find_all('span',{'class':'price'})[0].text
            return self.parseString(price)
        else:
            return 0
    
    def parseString(self, price_string):
        price_list = []
        price_float = ''
        
        for x in price_string:
            if 48<= ord(x) <= 57:
                price_list.append(x)
        
        price_list.insert(-2, '.')
        
        for item in price_list:
            price_float += item
            
        return float(price_float)