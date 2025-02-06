""" A buffet-style restaurant offers only five basic foods. Think of five 
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the 
change.
• The restaurant changes its menu, replacing two of the items with different 
foods. Add a line that rewrites the tuple, and then use a for loop to print 
each of the items on the revised menu """

print("Buffet")

foods_offered = ('Semo', 'Amala', 'Rice', 'Eba', 'Pounded Yam')

print("\nThe foods offered in this restaurant are: ")
for food in foods_offered:
    print(f"• {food}")

# Trying to alter a value in the tuple but python won't allow
# foods_offered[3] = 'Fufu'

print("\nChanging Menu ......")

foods_offered = ('Beans', 'Amala', 'Rice', 'Fufu', 'Pounded Yam')

print("\nThe foods offered in this restaurant are: ")
for food in foods_offered:
    print(f"• {food}")