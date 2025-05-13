import plotly.express as px

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
title = "Outcomes of Rolling One D6 1,000 Times"
labels = {'x': 'Outcome', 'y': 'Outcome Frequency'}
fig = px.bar(x=possible_outcomes, y=outcome_frequencies, title=title, 
             labels=labels)
fig.show()
