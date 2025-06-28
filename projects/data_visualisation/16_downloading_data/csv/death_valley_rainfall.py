from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Read data from file in lines
path = Path('weather_data\death_valley_2021_full.csv')
lines = path.read_text().splitlines()

# Parse lines to a csv reader, get header row & move to 2nd row
reader = csv.reader(lines)
header_row = next(reader)

# Read dates and precipitation values
dates, prcp_values = [], []
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        prcp_value = float(row[3])
    except ValueError:
        print(f"Missing value for {date}.")
    else:
        dates.append(date)
        prcp_values.append(prcp_value)

# Plot data
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcp_values, color='blue', alpha=0.6)

# Format plot
title = "Daily Rainfall, 2021\nDeath Valley National Park, California"
ax.set_title(title, fontweight='bold', fontsize=20)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel('Rainfall', fontsize=14)
ax.tick_params(labelsize=12)

# Show plot
plt.show()
