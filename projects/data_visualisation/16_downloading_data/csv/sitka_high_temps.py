from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Read data from file in lines
path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

# Get an iterator for the lines, get the first row and move to the next row
reader = csv.reader(lines)
header_row = next(reader)

# Extract dates, high temperatures
dates, high_temps = [], []
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    high_temp = int(row[4])
    dates.append(date)
    high_temps.append(high_temp)

# Plot the high & low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, high_temps, color='red', alpha=0.5)

# Format plot.
ax.set_title("Daily High Temperatures, 2021\nSitka Airport, Alaska", 
             fontsize=20, fontweight='bold')
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (⁰F)', fontsize=14)
ax.tick_params(labelsize=12)

# Show plot.
plt.show()
