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

monday_data = data[data.day == 'Monday']

monday_temp = monday_data.temp
print(monday_temp)


def celsius_to_fahrenheit(cel_temp):
    return (cel_temp * 9/5) + 32


print(celsius_to_fahrenheit(monday_temp))