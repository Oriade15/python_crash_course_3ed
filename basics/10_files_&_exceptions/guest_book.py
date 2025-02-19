from pathlib import Path

print("Guest Book")

file_path = Path('guest_book.txt')
guest_names = ""
print("Enter your name to save it to the Guest Book.")

while True:
    guest_name = input("\nName: ")
    guest_names += guest_name + "\n"

    quit_choice = input("Do you want to enter another name (enter 'x' if not): ")
    if quit_choice == 'x':
        break

print(f"\nAdding the entered names to the Guest Book...\n")
file_path.write_text(guest_names)
print("Done!")
