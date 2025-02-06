print("Messages")


def show_messages(messages):
    print("\nShowing Messages ...")
    for message in messages:
        print(f"• {message}")
    

messages = [
    'Hi.',
    "What's up?",
    "How're you doing?",
    "I'm doing great. And you?",
    "Very well too."
]

show_messages(messages)
