import csv
from datetime import datetime
import matplotlib.pyplot as plt

open_file = open("sitka_weather_2018_simple.csv", "r")

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
lows = []
dates = []

for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)

# print(highs)

fig = plt.figure()

# plot these highs
plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
fig.autofmt_xdate()
plt.title("Daily Temps for 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temp Fahrenheit", fontsize=12)
plt.tick_params(axis="both", labelsize=12)
plt.fill_between(
    dates,
    highs,
    lows,
    color="blue",  # The outline color
    alpha=0.1,  # lighter blue
)

plt.show()

# plot two charts in the same window (subplots)
fig2, a = plt.subplots(2)
a[0].plot(dates, highs, c="red")
a[1].plot(dates, lows, c="blue")

plt.show()
open_file.close()
