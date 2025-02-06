print("Seeing the World!")

places_to_visit = ['Mecca', 'Madinah', 'Gaza', 'Seoul', 'Shanghai', 'Texas', 'Jerusalem']

print(f"• My list in its original order: \n\t{places_to_visit}")
print(f"• My list in alphabetically sorted order: \n\t{sorted(places_to_visit)}")
print(f"• My list in its original order: \n\t{places_to_visit}")
print(f"• My list in reverse alphabetically sorted order: \n\t{sorted(places_to_visit, reverse=True)}")
print(f"• My list in its original order: \n\t{places_to_visit}")

places_to_visit.reverse()
print(f"• My list changed to reverse order: \n\t{places_to_visit}")

places_to_visit.reverse()
print(f"• My list changed to its original order: \n\t{places_to_visit}")

places_to_visit.sort()
print(f"• My list changed to alphabetically sorted order: \n\t{places_to_visit}")

places_to_visit.sort(reverse=True)
print(f"• My list changed to reverse alphabetically sorted order: \n\t{places_to_visit}")

