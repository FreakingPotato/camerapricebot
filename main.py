from digidirect import parseDigiDirectPrice
from georges import parseGeorgesPrice
from teds import parseTedsPrice
from camerapro import parseCameraProPrice
from file_handling import record_price
from file_handling import get_url
import time
import smtplib
import datetime

def scrapper():
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

    return price_dic

def send_email():
    #setup the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #login details
    server.login('dk941012@gmail.com', 'uqjocqueklgyquis')

    info = cheapest_price(scrapper())
    timestamp = datetime.datetime.now()

    #format the email
    subject = 'Price report'
    body = f"{timestamp} \n Check the price below: \n {info}"
    msg = f"Subject: {subject} \n\n {body}"

    #email direction from...to...
    server.sendmail(
        'dk941012@gmail.com',
        'stark@askstudioact.com',
        msg
    )

    print('Hey Email has been sent!')
    
    #quit the server
    server.quit()


#find the cheapest price
def cheapest_price(price_dic):
    cheapest_dic = {}

    for key in price_dic.keys():
        cheapest_dic[key] = ''

    for item in price_dic.items():
        cheapest_shop = [item[1][0][0]]
        cheapest_price = [item[1][0][1]]
        cheapest_list = cheapest_shop + cheapest_price
        for x in item[1]:
            # some store may don't have the target product which price is zero
            if x[1] < cheapest_price[0] and x[1] != 0:
                cheapest_price = [x[1]]
                cheapest_shop = [x[0]]
                cheapest_list = cheapest_shop + cheapest_price
        cheapest_dic[item[0]]=cheapest_list

    return cheapest_dic

while True:

    #record the price_dic 
    record_price(scrapper())

    #send email
    send_email()

    time.sleep(60*5)
