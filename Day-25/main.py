import pandas

# Extra work
# def average(dlist):
#     # a = sum/len
#     return sum(dlist)/len(dlist)
# Use the pandas library methods


data = pandas.read_csv("./weather_data.csv")
temp_list = data["temp"].to_list()
temp_series = data["temp"]
# # Get the mean of temp
# # print(average(temp_list))
# print(data["temp"].mean())
# # Get the maximum value of temp
# print(temp_series.max())
# print(data.temp.max())

# max_temp = temp_series.max()

# monday = data[data.day == "Monday"]
# print(monday)
# celsius = monday.temp[0]  # Get the value out of the series
# print(celsius)
# fahrenheit = (celsius * 9 / 5) + 32
# print(fahrenheit)
#
# # print(data[data.temp == max_temp])
# # print(data[data.temp == data.temp.max()])
#
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)  # Create a pandas table

print(data)

# ['day', 'temp', 'condition']
# ['Monday', '12', 'Sunny']
# ['Tuesday', '14', 'Rain']
# ['Wednesday', '15', 'Rain']
# ['Thursday', '14', 'Cloudy']
# ['Friday', '21', 'Sunny']
# ['Saturday', '22', 'Sunny']
# ['Sunday', '24', 'Sunny']
