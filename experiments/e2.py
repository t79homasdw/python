import csv

with open("csv/weather.csv", "r") as file:
    reader = list(csv.reader(file))

city = input("Enter city name: ")
for row in reader[1:]:
    if row[0] == city:
        print(f"City: {city} weather on {row[2]}: MaxTemp={row[3]}, MinTemp={row[4]}, Weather={row[5]}")
        exit()
else:
    print(f"No weather data found for {city}")