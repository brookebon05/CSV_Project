import csv
import matplotlib.pyplot as plt

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)  # skips header row

# enumerate returns both index of each itema and the value of each item.

for index, column_header in enumerate(header_row):
    print("index: ", index, "Column name:", column_header)

highs = []

for row in csv_file:
    highs.append(int(row[5]))

# print(highs)

# plot these highs
plt.plot(highs, c="red")
# plot is a line graph
plt.title("Daily Temps, July 2018", fontsize=16)
plt.xlabel("", fontsize=16)
plt.ylabel("Temp Fahrenheit", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()