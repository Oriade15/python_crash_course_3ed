print("Dream Vacation")

poll_responses = []
is_polling_active = True
poll_prompt = "\nIf you could visit one place in the world, where would you go?\n\tAnswer (to exit, enter 'x'): "

print("\nDream Vacation Poll ")
while is_polling_active:
    poll_response = input(poll_prompt)
    if poll_response == 'x':
        is_polling_active = False
    else:
        poll_responses.append(poll_response)
        print("Thank you for participating in our poll." + 
            " Your Response has been saved.")

print("\nReviewing poll responses ...")
if len(poll_responses) != 0:
    print("\nPoll Results")
    for response in poll_responses:
        print(f"• {response}")
else:
    print("\nOops! Seems like no one participated in our poll.")

