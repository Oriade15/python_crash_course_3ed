import plotly.express as px

from die import Die

# Create three D6 dice.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list.
outcomes = [die_1.roll() + die_2.roll() + die_3.roll() for roll_count in range(1000)]

# Analyze the results.
maximum_outcome = die_1.num_of_sides + die_2.num_of_sides + die_3.num_of_sides
possible_outcomes = range(3, maximum_outcome+1)
outcome_frequencies = [outcomes.count(outcome) for outcome in possible_outcomes]

# Visualise the Outcomes.
title = "Sums of Outcomes of Rolling Three D6 1,000 Times"
labels = {'x': 'Sum of Outcomes', 'y': 'Frequency'}
fig = px.bar(x=possible_outcomes, y=outcome_frequencies, title=title, 
             labels=labels)

# Further customise the chart.
fig.update_layout(xaxis_dtick=1)

fig.show()
