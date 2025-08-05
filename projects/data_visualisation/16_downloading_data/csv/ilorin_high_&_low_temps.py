from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


def convert_temp_F_to_C(temp):
    """ Converts temperature values from Farenheit tp Celsius """
    return 5 * (temp - 32)/9


# Read data from file in lines.
path = Path('weather_data\ilorin_01_2025_to_06_2025.csv')
lines = path.read_text().splitlines()

# Create reader object from lines, get the first row of the reader &
# move to next row.
reader = csv.reader(lines)
header_row = next(reader)

# Extract dates, high and low temperatures
dates, high_temps, low_temps = [], [], []
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high_temp = int(row[4])
        low_temp = int(row[5])
    except ValueError:
        print(f"Missing temperature data for {date}")
    else:
        dates.append(date)
        # Convert temperature to Celsius due to region.
        high_temps.append(convert_temp_F_to_C(high_temp))
        low_temps.append(convert_temp_F_to_C(low_temp))

# Plot the high & low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, high_temps, color='red', alpha=0.5)
ax.plot(dates, low_temps, color='blue', alpha=0.5)
ax.fill_between(dates, high_temps, low_temps, facecolor='blue', alpha=0.1)

# Format plot
title = "Daily High and Low Temperatures, 2025\nIlorin, Kwara State, Nigeria"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (⁰C)', fontsize=14)
ax.tick_params(labelsize=12)

# Show plot
plt.show()
