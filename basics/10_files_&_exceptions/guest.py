from pathlib import Path

print("Guest\n")
file_path = Path('guest.txt')

guest_name =  input("What is your name?\nName: ")

print("Saving your name to 'guest.txt' ...")
file_path.write_text(guest_name)
print("Done!")
