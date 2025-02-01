print("Polling")

poll_candidates = [
    'Bolu',
    'Timileyin',
    'Oriade',
    'Adedeji',
    'Dare',
    'Tolu',
    'Tola'
]

favorite_language_poll = {
    'Oriade': 'C#',
    'Bolu': 'JavaScript',
    'Adedeji': 'Python',
    'Tolu': 'Python',
    'Tola': 'Rust'
}

print("\nChecking Poll .....")

for candidate in poll_candidates:
    if candidate in favorite_language_poll.keys():
        print(f"• Thank you {candidate} for participating in the poll.")
    else:
        print(f"• Hello {candidate}, we are inviting you to participate in our poll.")
