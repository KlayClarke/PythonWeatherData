import csv

with open('weather_data.csv', mode='r') as csv_data:
    data = csv.reader(csv_data)
    for row in data:
        print(row)