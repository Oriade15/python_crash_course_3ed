from pathlib import Path


def read_file(file_path):
    file = Path(file_path)
    file_content = file.read_text().rstrip()
    
    return file_content


def print_file_content(file_content, line_by_line=False):
    if line_by_line == True:
        for line in file_content.splitlines():
            print(line)
    else:
        print(file_content)

print("Learning Python\n")

print("\nPrinting the file's content all at once\n")

print_file_content(read_file('learning_python.txt'))

print("\nPrinting the file's content line by line\n")

print_file_content(read_file('learning_python.txt'), line_by_line=True)