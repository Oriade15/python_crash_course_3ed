print("Stage of life")

person_age = 19
print(f"When a person's age is {person_age}, ")

if person_age < 2:
    print("\tthen the Person is a baby.")
elif person_age >= 2 and person_age < 4:
    print("\tthen the person is a toddler.")
elif person_age >= 4 and person_age < 13:
    print("\tthen the person is a kid.")
elif person_age >= 13 and person_age < 20:
    print("\tthen the person is a teenager.")
elif person_age >= 20 and person_age < 65:
    print("\tthen the person is an adult.")
elif person_age > 65:
    print("\tthen the person is an elder.")