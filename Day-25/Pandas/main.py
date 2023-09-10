import pandas

# Create a DataFrame with the data
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Take data: Fur color, Count
fur_color = data["Primary Fur Color"]
print(fur_color.tolist())

# Count how many colors of fur are
black_fur = len(data[fur_color == "Black"])
cinnamon_fur = len(data[fur_color == "Cinnamon"])
gray_fur = len(data[fur_color == "Gray"])

print(black_fur)
print(cinnamon_fur)
print(gray_fur)
# # Build the new DataFrame
# fur_color_dictionary = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [gray_fur, cinnamon_fur, black_fur],
# }
#
# data_count = pandas.DataFrame(data=fur_color_dictionary)
# data_count.to_csv("squirrel_count.csv")
# print(data_count)
#
# print(fur_color_dictionary)
#
# # print(data)
#
#
# print(fur_color.value_counts())
#
# new_data = fur_color.value_counts().to_csv()
# print(new_data)
