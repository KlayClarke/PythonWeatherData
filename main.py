import csv

with open('weather_data.csv', mode='r') as csv_data:
    csv_data_list = csv_data.readlines()
    print(csv_data_list)