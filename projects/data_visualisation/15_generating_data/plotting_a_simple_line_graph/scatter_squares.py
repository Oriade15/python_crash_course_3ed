import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Squares of Numbers", fontsize=28)
ax.set_xlabel("Number", fontsize=14)
ax.set_ylabel("Square of Number", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=12)

# Set the range for each axis
ax.axis([0, 1100, 0, 1_100_000])

# ax.ticklabel_format(style='plain')

plt.show()

# plt.savefig('squares_of_numbers_plot.png', bbox_inches='tight')
