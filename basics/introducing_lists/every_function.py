print("Every Function")

languages = ['English', 'Arabic', 'Yoruba', 'Igbo', 'Hausa']

print(f"\n• My Original list: \n\t{languages}")

print("• Using the `append()` method to add 'Chinese' to the list: ")
languages.append('Chinese')
print(f"\t{languages}")

print("• Using the `insert(index)` method to add 'Japanese' at index '4' the list: ")
languages.insert(4, 'Japanese')
print(f"\t{languages}")

print(f"• Using the `pop()` method to remove the last item of the list which is '{languages.pop()}': \n\t{languages}")

print(f"• Using the `pop(index)` method to remove the 3rd item of the list which is '{languages.pop(2)}': \n\t{languages}")

print("• Using the `remove(value)` method to remove 'Japanese' from the list: ")
languages.remove('Japanese')
print(f"\t{languages}")

print(f"• Using the `sorted(list)` function to present the list in a sorted order but still retain the list's original order: \n\t{sorted(languages)}")

print(f"• Using the `sorted(list, reverse=bool)` function to present the list in a REVERSE sorted order but still retain the list's original order: \n\t{sorted(languages, reverse=True)}")

print(f"• Using the `reverse()` method to reverse the order of the list: ")
languages.reverse()
print(f"\t{languages}")

print(f"• Using the `reverse()` method AGAIN (after using it before) to reverse the order of the list back to its original order: ")
languages.reverse()
print(f"\t{languages}")

print(f"• Using the `sort()` method to sort the list alphabetically: ")
languages.sort()
print(f"\t{languages}")

print(f"• Using the `sort(reverse=bool)` method sort the list reverse-alphabetically: ")
languages.sort(reverse=True)
print(f"\t{languages}")

print(f"• Using the `len(list)` function to get the length of the list: \n\t{len(languages)}")
