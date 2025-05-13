import matplotlib.pyplot as plt

from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list.
outcomes = []

for roll_count in range(1000):
    outcome = die.roll()
    outcomes.append(outcome)

# Analyze the results.
outcome_frequencies = []
possible_outcomes = range(1, die.num_of_sides+1)
for outcome in possible_outcomes:
    outcome_frequency = outcomes.count(outcome)
    outcome_frequencies.append(outcome_frequency)

# Visualise the Outcomes.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(x=possible_outcomes, height=outcome_frequencies)

title = "Outcomes of Rolling One D6 1,000 Times"
labels = {'x': 'Outcome', 'y': 'Frequency'}
ax.set_title(title, fontsize=28)
ax.set_xlabel(labels['x'], fontsize=14)
ax.set_ylabel(labels['y'], fontsize=14)
ax.tick_params(labelsize=12)

plt.show()
