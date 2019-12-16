#function record the data into a csv file named price_data.csv
import csv
import datetime

#current method is not extendable 
def record_price(price_dic):
    try:
        with open('price_data.csv', 'a') as csv_file:
            myFields = ['Date','Camera model','Georges','DigiDirect','Teds','CameraPro']
            csv_writer = csv.DictWriter(csv_file, fieldnames=myFields)
            if not has_header('price_data.csv'):
                csv_writer.writeheader()
            if get_date('price_data.csv') != False:
                #insert an empty line in the end
                csv_writer.writerow({'Camera model': "",'Georges': "",'DigiDirect':"",'Teds': "",'CameraPro': ""})
                csv_writer.writerow({'Date': get_date('price_data.csv')})
                for model, price in price_dic.items():
                    csv_writer.writerow({'Camera model': model,
                                        'Georges': price[0][1],
                                        'DigiDirect':price[1][1],
                                        'Teds': price[2][1],
                                        'CameraPro': price[3][1]})


    except IOError:
        print("File not accessible")

#avoid adding redundent information based on the fact that the price won't change twice in a day
def get_date(file):
    x = datetime.datetime.now()
    date = x.strftime('%x')
    with open(file,'r') as csv_file:
        for row in csv_file:
            if date in row:
                return False

    return date

#avoid adding redundent header
def has_header(file):
    header = ['Date','Camera model','Georges','DigiDirect','Teds','CameraPro']
    with open(file,'r') as csv_file:
        for row in csv_file:
            if header[0] in row:
                return True
    return False

#get the url information from the url_data.csv
def get_url():
    try:
        price_dic={}
        with open('url_data.csv','r') as csv_file:
            csv_reader  = csv.DictReader(csv_file)
            for row in csv_reader:
                price_dic[row['Product_Number']] = [row['Product_Name'],row['Georges_url'],row['DigiDirect_url'],row['Teds_url'],row['CameraPro_url']]
            return price_dic
    except IOError:
        print("url not accessible")

