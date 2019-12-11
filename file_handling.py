#function record the data into a csv file named price_data.csv
import csv

#current method is not extendable 
def record_price(price_dic):
    try:
        with open('price_data.csv', 'w') as csv_file:
            myFields = ['Camera model','Georges','DigiDirect','Teds','CameraPro']
            csv_writer = csv.DictWriter(csv_file, fieldnames=myFields)
            csv_writer.writeheader()
            for x,y in price_dic.items():
                csv_writer.writerow({'Camera model': x,
                                     'Georges': y[0][1],
                                     'DigiDirect':y[1][1],
                                     'Teds': y[2][1],
                                     'CameraPro': y[3][1]})
    except IOError:
        print("File not accessible")

def get_url():
    try:
        price_dic={}
        with open('url_data.csv','r') as csv_file:
            csv_reader  = csv.DictReader(csv_file)
            for row in csv_reader:
                price_dic[row['Product_Number']] = [row['Product_Name'],row['Georges_url'],row['DigiDirect_url'],row['Teds_url'],row['CameraPro_url']]
            return price_dic
    except IOError:
        print("File not accessible")

