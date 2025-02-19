from pathlib import Path
import json


def get_number_from_json_file(file_path):
    if file_path.exists():
        number = json.loads(file_path.read_text())
        return number
    else:
        return None


favorite_number_file_path = Path('favorite_number.json')
favorite_number = get_number_from_json_file(favorite_number_file_path)

if favorite_number:
    print(f"\nI know your favorite number! It's {favorite_number}.")
else:
    favorite_number = int(input("\nYour favorite number: "))
    print("\nSaving favorite number in JSON file...")
    favorite_number_file_path.write_text(json.dumps(favorite_number))
    print("\nDone!")
