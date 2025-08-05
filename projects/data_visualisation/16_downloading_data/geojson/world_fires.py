from pathlib import Path
import csv

import plotly.express as px

# Read data from file in lines
path = Path('fire_data\world_fires_1_day.csv')
lines = path.read_text().splitlines()

# Parse lines to a csv reader, get header row & move to 2nd row
reader = csv.reader(lines)
header_row = next(reader)

# Read values
latitudes, longitudes, brightnesses = [], [], []
for row in reader:
    latitudes.append(float(row[0]))
    longitudes.append(float(row[1]))
    brightnesses.append(float(row[2]))

# Plot map
title = "World Fires"
fig = px.scatter_geo(lat=latitudes, lon=longitudes, size=brightnesses, 
                     title=title, color=brightnesses, 
                     color_continuous_scale='Thermal', 
                     labels={'color':'Brightness'}, 
                     projection='natural earth', 
                     )
fig.show()
