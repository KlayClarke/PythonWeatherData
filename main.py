import csv

with open('weather_data.csv', mode='r') as csv_data:
    data = csv.reader(csv_data)
    temperatures = []
    for row in data:
        temp_num = row[1]
        if temp_num != 'temp':
            temperatures.append(int(temp_num))


print(temperatures)
