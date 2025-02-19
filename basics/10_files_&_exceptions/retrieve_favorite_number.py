from pathlib import Path
import json

print("Retrieve Favorite Number\n")

file_path = Path('favorite_number.json')

print("Reading Favorite number from file...\n")

favorite_number_from_json = json.loads(file_path.read_text())

print(f"I know your favorite number! It's {favorite_number_from_json}.\n")
