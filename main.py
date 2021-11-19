import csv
import pandas

# with open('weather_data.csv', mode='r') as csv_data:
#     data = csv.reader(csv_data)
#     temperatures = []
#     for row in data:
#         temp_num = row[1]
#         if temp_num != 'temp':
#             temperatures.append(int(temp_num))

data = pandas.read_csv('weather_data.csv')

# data_dict = data.to_dict()
# print(data_dict)

list_of_temps = data['temp'].to_list()
print(list_of_temps)

