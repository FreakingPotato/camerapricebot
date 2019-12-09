# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import bs4
import requests
from bs4 import BeautifulSoup

product_dic = {
               'p1' : ['Sony A7 R3',
                       'https://www.georges.com.au/sony-a7r-iii-mirrorless-digital-camera-body-only.html',
                       'https://www.digidirect.com.au/cameras/sony-alpha-a7r-iii-mirrorless-digital-camera-body-only',
                       'https://www.teds.com.au/sony-a7r-mark-3-body',
                       'https://www.camerapro.com.au/sony-alpha-a7r-mark-iii-mirrorless-camera.html'],
               'p2' : ['Sony A7 R4',
                       'https://www.georges.com.au/sony-a7r-mark-iv-body.html',
                       'https://www.digidirect.com.au/cameras/sony-a7r-mark-iv-body',
                       'https://www.teds.com.au/sony-a7r-mark-iv-body',
                       'https://www.camerapro.com.au/sony-a7r-mark-iv-mirrorless-camera-body-only.html'],
               'p3' : ['Sony A7 M3',
                       'https://www.georges.com.au/sony-a7-iii-mirrorless-digital-camera-body-only.html',
                       'https://www.digidirect.com.au/cameras/sony-alpha-a7-iii-mirrorless-digital-camera-body-only',
                       'https://www.teds.com.au/sony-a7-mark-3-body',
                       'https://www.camerapro.com.au/sony-a7-iii-mirrorless-camera-body-only.html'],
               'p4' : ['Sony A9 M1',
                       'https://www.georges.com.au/sony-a9-body.html',
                       'https://www.digidirect.com.au/cameras/sony-alpha-a9-mirrorless-digital-camera-body-only',
                       'https://www.teds.com.au/sony-a9-body',
                       'https://www.camerapro.com.au/sony-a9-mirrorless-camera.html'],
               'p5' : ['Sony A9 M2',
                       'https://www.georges.com.au/sony-alpha-a9-ii-mirrorless-digital-camera-body-only.html',
                       'https://www.digidirect.com.au/sony-alpha-a9-ii-body-only',
                       'https://www.teds.com.au/sony-a9-mark-2-body',
                       'https://www.camerapro.com.au/sony-alpha-a9-mark-ii-camera-body.html']
               }

#imply inheritance

class ParsePrice:
    def __init__(self,url):
        self.url = url        
        
    def parsePrice(self):
        r = requests.get(self.url)
        soup = bs4.BeautifulSoup(r.text,"html")
        price = soup.find_all('span',{'class':'price'})[0].text
        return self.parseString(price)
    
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

class parseGeorgesPrice(ParsePrice):
    def __init(self,url):
        super().__init__(url)
        
    company = 'Georges'
        
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
    
class parseCameraProPrice(ParsePrice):
    def __init(self,url):
        super().__init__(url)
        
    def parsePrice(self):
        r = requests.get(self.url)
        soup = bs4.BeautifulSoup(r.text,"html")
        price = soup.find_all('span',{'data-price-type':'finalPrice'})[0].text
        return self.parseString(price)
        
    company = 'CameraPro'
    
price_dic={}

for product in product_dic.values():
    product_name = product[0]
    price_list=[]
    for x in range(1,5):
        if x == 1:
            parser = parseGeorgesPrice(product[1])
            price_list.append([parser.company, parser.parsePrice()])
        if x == 2:
            parser = parseDigiDirectPrice(product[2])
            price_list.append([parser.company, parser.parsePrice()])
        if x == 3:
            parser = parseTedsPrice(product[3])
            price_list.append([parser.company, parser.parsePrice()])
        if x == 4:
            parser = parseCameraProPrice(product[4])
            price_list.append([parser.company, parser.parsePrice()])
    price_dic[product_name] = price_list
    
print(price_dic)

#find the cheapest price
    
cheapest_dic = {}

for key in price_dic.keys():
    cheapest_dic[key] = ''

for item in price_dic.items():
#    print(item)
    cheapest_shop = [item[1][0][0]]
    cheapest_price = [item[1][0][1]]
    cheapest_list = cheapest_shop + cheapest_price
#    print(cheapest_list)
    for x in item[1]:
        if x[1] < cheapest_price[0]:
            cheapest_price = [x[1]]
            cheapest_shop = [x[0]]
            cheapest_list = cheapest_shop + cheapest_price
    cheapest_dic[item[0]]=cheapest_list
    
print(cheapest_dic)


#
#Problems:
#    1. Trim the data from string to float (data from Teds is different from other website)
        
        
        
        
        