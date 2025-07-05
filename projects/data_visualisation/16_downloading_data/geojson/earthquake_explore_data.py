from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object.
# path = Path('.\earthquake_data\eq_data_1_day_m1.geojson')
# contents = path.read_text()
# all_earthquake_data = json.loads(contents)

# Read the GeoJSON file and handle potential encoding issues.
path = Path("earthquake_data\eq_data_1_day_m1.geojson")
try:
    with path.open(encoding="utf-8") as f:
        all_earthquake_data = json.load(f)
    print("File loaded successfully!")
except UnicodeDecodeError as e:
    print(f"UnicodeDecodeError: {e}")
except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e}")

# Create a more readable version of the data file.
# new_path = Path('earthquake_data\eq_data_1_day_m1_readable.geojson')
# readable_contents = json.dumps(all_earthquake_data, indent=4)
# new_path.write_text(readable_contents, encoding="utf-8")

# Examine all earthquakes in the dataset.
all_earthquake_dictionaries = all_earthquake_data['features']

magnitudes, longitudes, latitudes = [], [], []
for dictionary in all_earthquake_dictionaries:
    magnitude = dictionary['properties']['mag']
    longitude = dictionary['geometry']['coordinates'][0]
    latitude = dictionary['geometry']['coordinates'][1]
    magnitudes.append(magnitude)
    longitudes.append(longitude)
    latitudes.append(latitude)

print(magnitudes[:10])
print(longitudes[:5])
print(latitudes[:5])
