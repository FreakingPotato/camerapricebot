from digidirect import parseDigiDirectPrice
from georges import parseGeorgesPrice
from teds import parseTedsPrice
from camerapro import parseCameraProPrice
from file_handling import record_price
from file_handling import get_url

product_dic = get_url()
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
    
# print(price_dic)

#record the price_dic 
record_price(price_dic)

#find the cheapest price
    
cheapest_dic = {}

for key in price_dic.keys():
    cheapest_dic[key] = ''

for item in price_dic.items():
    cheapest_shop = [item[1][0][0]]
    cheapest_price = [item[1][0][1]]
    cheapest_list = cheapest_shop + cheapest_price
    for x in item[1]:
        if x[1] < cheapest_price[0]:
            cheapest_price = [x[1]]
            cheapest_shop = [x[0]]
            cheapest_list = cheapest_shop + cheapest_price
    cheapest_dic[item[0]]=cheapest_list
    
# print(cheapest_dic)
