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
                csv_writer.writerow({'model': x,
                                     'Georges': y[0][1],
                                     'DigiDirect':y[1][1],
                                     'Teds': y[2][1],
                                     'CameraPro': y[3][1]})
    except IOError:
        print("File not accessible")
