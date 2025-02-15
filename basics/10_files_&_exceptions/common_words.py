from pathlib import Path


def count_text_appearances_in_file(word, file_path):
    file_contents = Path(file_path).read_text(encoding='utf-8')

    appearance_count = file_contents.lower().count(word.lower())

    return appearance_count


print("Common Words")

folder_path = 'project_gutenberg/'
file_paths = [
    'David goes to Greenland by David Binney Putnam.txt',
    'Fenella by Henry Longan Stuart.txt',
    "Woman's Voice - An anthology by Josephine Conger-Kaneko.txt",
]

print("\nFinding how many times the text 'the' appears in the texts...")
for file_path in file_paths:
    appearance_count = count_text_appearances_in_file(
        'the ', folder_path + file_path)
    print(f" • {appearance_count} times in '{file_path}'.")

print("\nFinding how many times the text 'the ' appears in the texts...")
for file_path in file_paths:
    appearance_count = count_text_appearances_in_file(
        'the ', folder_path + file_path)
    print(f" • {appearance_count} times in '{file_path}'.")
    