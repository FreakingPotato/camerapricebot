from parseprice import ParsePrice
import bs4
import requests
from bs4 import BeautifulSoup 

class parseGeorgesPrice(ParsePrice):
    def __init(self,url):
        super().__init__(url)
        
    company = 'Georges'