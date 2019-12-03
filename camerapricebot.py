# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import bs4
import requests
from bs4 import BeautifulSoup

product_dic = {
               'p1' : ['Sony A7 R3','https://www.georges.com.au/sony-a7r-iii-mirrorless-digital-camera-body-only.html','https://www.digidirect.com.au/cameras/sony-alpha-a7r-iii-mirrorless-digital-camera-body-only','https://www.teds.com.au/sony-a7r-mark-3-body'],
               'p2' : ['Sony A7 R4','https://www.georges.com.au/sony-a7r-mark-iv-body.html','https://www.digidirect.com.au/cameras/sony-a7r-mark-iv-body','https://www.teds.com.au/sony-a7r-mark-iv-body'],
               'p3' : ['Sony A7 M3','https://www.georges.com.au/sony-a7-iii-mirrorless-digital-camera-body-only.html','https://www.digidirect.com.au/cameras/sony-alpha-a7-iii-mirrorless-digital-camera-body-only','https://www.teds.com.au/sony-a7-mark-3-body'],
               'p4' : ['Sony A9 M1','https://www.georges.com.au/sony-a9-body.html','https://www.digidirect.com.au/cameras/sony-alpha-a9-mirrorless-digital-camera-body-only','https://www.teds.com.au/sony-a9-body'],
               'p5' : ['Sony A9 M2','https://www.georges.com.au/sony-alpha-a9-ii-mirrorless-digital-camera-body-only.html','https://www.digidirect.com.au/sony-alpha-a9-ii-body-only','https://www.teds.com.au/sony-a9-mark-2-body']
               }

def parseGeorgesPrice(url):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text,"html")
    price = soup.find_all('span',{'class':'price'})[0].text
    return price

def parseDigiDirectPrice(url):
    r = requests.get(url)
    price_list = []
    soup = bs4.BeautifulSoup(r.text,"html")
    price = soup.find_all('div',{'class':'price-box price-final_price'})[0].find_all('span',{'class':'price'})
    for x in price:
        price_list.append(x.text)
    return min(price_list)

def parseTedsPrice(url):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text,"html")
    price = soup.find_all('div',{'class':'price-box'})[0].find('meta')['content']
    price = str('$')+str(price)
    return price

#def parseName():
#    r = requests.get('https://www.georges.com.au/blackmagic-pocket-cinema-camera-6k.html')
#    soup = bs4.BeautifulSoup(r.text,"html")
#    product_name = soup.find_all('h1',{'class':'product-name'})[0].text
#    return product_name

#while True:
#    print('the current price of ' + str(parseName()) + 'is: '+ str(parsePrice()))

price_dic={}

for product in product_dic.values():
    product_name = product[0]
    price_list=[]
    for x in range(1,4):
        if x == 1:
            price_list.append(['Georges', parseGeorgesPrice(product[1])])
        if x == 2:
            price_list.append(['DigiDirect', parseDigiDirectPrice(product[2])])
        if x == 3:
            price_list.append(['Teds', parseTedsPrice(product[3])])
    price_dic[product_name] = price_list
    
print(price_dic)

#find the cheapest price
    
cheapest_dic = {}

for key in price_dic.keys():
    cheapest_dic[key] = ''

for item in price_dic.items():
    cheapest_price = item[1][0][1]
    for x in item[1]:
        if x[1] < cheapest_price[1]:
            cheapest_price = x
    cheapest_dic[item[0]]=cheapest_price
    
print(cheapest_dic)
        
        
        
        
        
        
        
        