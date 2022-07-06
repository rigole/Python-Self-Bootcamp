import pandas

#data = pandas.read_csv("weather-data.csv")
#print(data["temp"])
#print(type(data))

#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data["temp"].to_list()
#print(len(temp_list))

#temp_mean = data["temp"].mean()

#print(temp_mean)

#print(data[data.temp == data.temp.max()])


#monday = data[data.day == "Monday"]
#print(monday)
"""
    data_dict = {
    "students": ["Rigole", "Michel", "Marie"],
    "scores": [75, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("dictionaire.csv")
    """

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

data_fur_color = data[data["Primary Fur Color"] == "Gray"]
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"]) 
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"]) 
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"]) 


data_dict ={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}



print(data_fur_color)
