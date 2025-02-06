print("Archived Messages")


def show_messages(messages):
    print("\nShowing Messages ...")
    for message in messages:
        print(f"• {message}")


def send_messages(messages, sent_messages):
    print("\nSending Messages ...")
    while messages:
        message_to_send = messages.pop()
        print(f"• Sending '{message_to_send}' ....")
        sent_messages.append(message_to_send)


messages = [
    'Hi.',
    "What's up?",
    "How're you doing?",
    "I'm doing great. And you?",
    "Very well too."
]

sent_messages = []

show_messages(messages)

send_messages(messages[:], sent_messages)

print("\nCheking to see if messages are still retained.")

print("\nOriginal messages")
show_messages(messages)

print("\nSent messages")
show_messages(sent_messages)
