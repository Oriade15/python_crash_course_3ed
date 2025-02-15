from pathlib import Path
import json

print("Store Favorite Number")

favorite_number = int(input("\nYour favorite number: "))

file_path = Path('favorite_number.json')

print("\nSaving favorite number in JSON file...")

file_path.write_text(json.dumps(favorite_number))

print("\nDone!")
