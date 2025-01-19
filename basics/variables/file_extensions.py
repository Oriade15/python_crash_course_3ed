filename = 'python_notes.txt'

print("File Extensions")

print(f"• Original file name: '{filename}'")

# Not supported in python v3.8.10
# print(f"• File name without extension: '{filename.removesuffix('.txt')}'")

print(f"• File name without extension: '{filename.rstrip('.txt')}'")