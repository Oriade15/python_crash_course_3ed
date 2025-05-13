import plotly.express as px

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
outcomes = []

for roll_count in range(1000):
    outcome = die_1.roll() + die_2.roll()
    outcomes.append(outcome)

# Analyze the results.
outcome_frequencies = []
maximum_outcome = die_1.num_of_sides + die_2.num_of_sides
possible_outcomes = range(2, maximum_outcome+1)
for outcome in possible_outcomes:
    outcome_frequency = outcomes.count(outcome)
    outcome_frequencies.append(outcome_frequency)

# Visualise the Outcomes.
title = "Outcomes of Rolling Two D6 1,000 Times"
labels = {'x': 'Outcome', 'y': 'Outcome Frequency'}
fig = px.bar(x=possible_outcomes, y=outcome_frequencies, title=title, 
             labels=labels)

# Further customise the chart.
fig.update_layout(xaxis_dtick=1)

fig.show()
