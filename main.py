import csv

with open('weather_data.csv', mode='r') as csv_data:
    data = csv.reader(csv_data)
    temporary_list = []
    for row in data:
        temp = row[1]
        temporary_list.append(temp)
    temporary_list.remove('temp')
    temperatures = []
    for num in temporary_list:
        converted_num = int(num)
        temperatures.append(converted_num)
    print(temperatures)