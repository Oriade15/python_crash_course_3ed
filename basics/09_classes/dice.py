from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        print(" • Rolling Die ...")
        print(f"\tValue: {randint(1, self.sides)}\n")


print("Dice\n")

times_to_roll_die = 10

six_sided_die = Die()

print(f"Rolling {six_sided_die.sides}-sided Die {times_to_roll_die} times\n")
for value in range(0, times_to_roll_die):
    six_sided_die.roll()
    
ten_sided_die = Die(10)

print(f"Rolling {ten_sided_die.sides}-sided Die {times_to_roll_die} times\n")
for value in range(0, times_to_roll_die):
    ten_sided_die.roll()

twenty_sided_die = Die(20)

print(f"Rolling {twenty_sided_die.sides}-sided Die {times_to_roll_die} times\n")
for value in range(0, times_to_roll_die):
    twenty_sided_die.roll()