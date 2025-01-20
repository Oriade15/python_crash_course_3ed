print("\nDinner Guests")

guests = ['Mummy', 'Daddy', 'Aisha', 'Toyyibah', 'Khalid']

print(f"\nI am inviting {len(guests)} guests to my dinner.")

print("\nInvitations")
print(f"• Hello {guests[0]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")
print(f"• Hello {guests[1]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")
print(f"• Hello {guests[2]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")
print(f"• Hello {guests[3]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")
print(f"• Hello {guests[4]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")

print(f"\nOh! It seems like {guests[3]} won't be able to make it to dinner.")
print("Seems like we would need to invite someone else.")

guests[3] = 'GrandMa'

print(f"\nHere are the new invitations (for {len(guests)} guests).")

print("\nNew Invitations")
print(f"• Hello {guests[0]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")
print(f"• Hello {guests[1]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")
print(f"• Hello {guests[2]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")
print(f"• Hello {guests[3]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")
print(f"• Hello {guests[4]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")

print("\nGuess what! I just got a bigger table.")
print("And I sure everyone knows what this means.")
print("It means I would be inviting more people to my dinner")

guests.insert(0, 'GrandPa') # Insert at begining 
guests.insert(3, 'Big Daddy') # Insert at middle
guests.append('Big Mummy') # Append 

print(f"\nHere are the new invitations (for {len(guests)} guests).")

print("\nNew Invitations")
print(f"• Hello {guests[0]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")
print(f"• Hello {guests[1]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")
print(f"• Hello {guests[2]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")
print(f"• Hello {guests[3]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")
print(f"• Hello {guests[4]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")
print(f"• Hello {guests[5]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")
print(f"• Hello {guests[6]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")
print(f"• Hello {guests[7]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")

print("\nAhhh! Omoo, I get bad news  oo.")
print("The table wey i talk say I dey expect no fit arrive on time for the dinner.")
print("Soo, na only two (2) people i fit invite liek this.")
print("Make una no fear. Insha Allah, I go invite everybody another time")

print("\nApology Messages")

removed_guest = guests.pop(0) # Removed GrandPa (from the beginning)
print(f"• Dear {removed_guest}, I'm sorry I can't invite you to dinner. Maybe some other time insha Allah.")
removed_guest = guests.pop() # Removed Big Mummy (from the end)
print(f"• Dear {removed_guest}, I'm sorry I can't invite you to dinner. Maybe some other time insha Allah.")
removed_guest = guests.pop() # Removed Khalid (from the end)
print(f"• Dear {removed_guest}, I'm sorry I can't invite you to dinner. Maybe some other time insha Allah.")
removed_guest = guests.pop() # Removed GrandMa (from the end)
print(f"• Dear {removed_guest}, I'm sorry I can't invite you to dinner. Maybe some other time insha Allah.")
removed_guest = guests.pop() # Removed Aisha (from the end)
print(f"• Dear {removed_guest}, I'm sorry I can't invite you to dinner. Maybe some other time insha Allah.")
removed_guest = guests.pop() # Removed Big Daddy (from the end)
print(f"• Dear {removed_guest}, I'm sorry I can't invite you to dinner. Maybe some other time insha Allah.")


print(f"\nHere are the invitations for the remaining {len(guests)} invitees.")

print("\nRemaining Invitations")
print(f"• Hello {guests[0]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")
print(f"• Hello {guests[1]}, I am inviting you for dinner at my place tomorrow evening at 7.00 pm.")

del guests[1] # Remove Daddy
del guests[0] # Remove Mummy

print("\nOh Oh! It seems like I've deleted my list.")
print("Let me check to confirm.")

print(f"Guest list: {guests}")
print(f"\nI am now inviting {len(guests)} guests to my place for dinner.")
