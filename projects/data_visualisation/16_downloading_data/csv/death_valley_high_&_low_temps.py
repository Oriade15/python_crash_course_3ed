from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


def convert_temp_F_to_C(temp):
    """ Converts temperature values from Farenheit tp Celsius """
    return 5 * (temp - 32)/9


# Read data from file in lines
path = Path('weather_data\death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

# Get an iterator for the lines, get the first row and move to the next row
reader = csv.reader(lines)
header_row = next(reader)

# Get the indexes for high and low temperatures AUTOMATICALY
for index in range(0, len(header_row)):
    if header_row[index] == "TMAX":
        high_temp_index = index
    elif header_row[index] == "TMIN":
        low_temp_index = index

# Extract station name, dates, high & low temperatures (in Celsius Scale)
station_name = ""
dates, high_temps, low_temps = [], [], []
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high_temp = int(row[high_temp_index])
        low_temp = int(row[low_temp_index])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates.append(date)
        # Convert temperature to Celsius
        high_temps.append(convert_temp_F_to_C(high_temp))
        low_temps.append(convert_temp_F_to_C(low_temp))
    if station_name != row[1]:
        station_name = row[1]

# Plot the high & low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, high_temps, color='red', alpha=0.5)
ax.plot(dates, low_temps, color='blue', alpha=0.5)
ax.fill_between(dates, high_temps, low_temps, facecolor='blue', alpha=0.1)

# Format plot.
title = f"Daily High and Low Temperatures, 2021\n{station_name}"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (⁰C)', fontsize=14)
ax.tick_params(labelsize=12)

# Show plot.
plt.show()
