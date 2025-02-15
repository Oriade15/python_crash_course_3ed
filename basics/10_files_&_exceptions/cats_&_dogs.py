from pathlib import Path

def print_file_contents(file_path):
    try:
        file_contents = Path(file_path).read_text()
    except FileNotFoundError:
        print(f"\nOops! It seems like the file '{file_path}' does not exist in this directory.")
    else:
        print(f"\nPrinting contents in '{file_path}'...\n")
        print(file_contents)

print("Cats & Dogs\n")

print_file_contents('dogs.txt')
print_file_contents('cats.txt')
print_file_contents('birds.txt')