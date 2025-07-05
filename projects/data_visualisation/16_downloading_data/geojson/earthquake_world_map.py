from pathlib import Path
import json

import plotly.express as px

# Read the GeoJSON file and handle potential encoding issues.
path = Path("earthquake_data\eq_data_30_day_m1.geojson")
try:
    with path.open(encoding="utf-8") as f:
        all_earthquake_data = json.load(f)
    print("File loaded successfully!")
except UnicodeDecodeError as e:
    print(f"UnicodeDecodeError: {e}")
except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e}")

# Examine all earthquakes in the dataset.
all_earthquake_dictionaries = all_earthquake_data['features']

magnitudes, longitudes, latitudes, titles = [], [], [], []
for dictionary in all_earthquake_dictionaries:
    magnitudes.append(dictionary['properties']['mag'])
    longitudes.append(dictionary['geometry']['coordinates'][0])
    latitudes.append(dictionary['geometry']['coordinates'][1])
    titles.append(dictionary['properties']['title'])

title = all_earthquake_data['metadata']['title']
fig = px.scatter_geo(lat=latitudes, lon=longitudes, size=magnitudes, 
                     title=title, color=magnitudes, 
                     color_continuous_scale='Viridis', 
                     labels={'color':'Magnitude'}, 
                     projection='natural earth', 
                     hover_name=titles, 
                     )
fig.show()
