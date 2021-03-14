import csv
from datetime import datetime
import matplotlib.pyplot as plt

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)  # skips header row

# enumerate returns both index of each itema and the value of each item.

for index, column_header in enumerate(header_row):
    print("index: ", index, "Column name:", column_header)

# converting the date
"""
my_date = '2018-07-01'
converted = datetime.strptime(my_date,'%Y-%m-%d')
"""

highs = []
dates = []

for row in csv_file:
    highs.append(int(row[5]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)


fig = plt.figure()

# plot these highs
plt.plot(dates, highs, c="red")
fig.autofmt_xdate()
plt.title("Daily Temps, July 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temp Fahrenheit", fontsize=12)
plt.tick_params(axis="both", labelsize=12)

plt.show()
open_file.close()
