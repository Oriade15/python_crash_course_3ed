from pathlib import Path


def read_file(file_path):
    file = Path(file_path)
    file_content = file.read_text().rstrip()

    return file_content

print("Learning C\n")

file_content = read_file('learning_python.txt')

print("Replacing Python in C from the file content and printing it ...\n")
print(file_content.replace('Python', 'C'))
