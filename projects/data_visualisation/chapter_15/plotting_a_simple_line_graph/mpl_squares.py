import matplotlib.pyplot as plt

values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(values, squares, linewidth=2)

# Set chart title and label axes.
ax.set_title("Squares Numbers", fontsize=28)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=12)

plt.show()