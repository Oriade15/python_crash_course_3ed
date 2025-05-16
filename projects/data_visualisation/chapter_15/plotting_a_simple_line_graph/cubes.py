import matplotlib.pyplot as plt 

# numbers = range(1, 6) # first five numbers
numbers = range(1, 5001) 
cubes = [number**3 for number in numbers]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

ax.scatter(numbers, cubes, s=10)

# Set chart title and label axes.
ax.set_title("Cubes of Numbers", fontsize=28)
ax.set_xlabel("Number", fontsize=14)
ax.set_ylabel("Cube", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=12)

# Set the range for each axis
ax.axis([0, 5500, 0, 130_000_000_000]) # for 5,000 points

plt.show()
