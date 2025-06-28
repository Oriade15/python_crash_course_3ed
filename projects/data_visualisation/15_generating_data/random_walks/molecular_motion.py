import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep simulating new paths, as long as the program is active.

while True:
    # Simulate a random path

    path = RandomWalk()
    path.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=96)
    point_numbers =  range(path.points_count)
    ax.plot(path.x_values, path.y_values, linewidth=2)
    ax.set_aspect('equal')

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=200)
    ax.scatter(path.x_values[-1], path.y_values[-1], c='red', 
               edgecolors='none', s=200)
    
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input("Simulate another path? (y/n): ")
    if keep_running == 'n':
        break
