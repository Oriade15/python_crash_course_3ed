from random import choice

class RandomWalk:
    """ A class to generate random walks. """

    def __init__(self, points_count=5000):
        """ Initialize attributes of a walk. """
        self.points_count = points_count

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ Calculate  all points in the walk. """
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.points_count:

            # Decide which direction to go, and how far to go.
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)           
            self.y_values.append(y)

    def get_step(self):
        """ Determine the direction & distance for each step. """
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance


class ModifiedRandomWalk:
    """ A class to generate random walks (in a more linear fashion). """

    def __init__(self, points_count=5000):
        """ Initialize attributes of a walk. """
        self.points_count = points_count

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ Calculate  all points in the walk. """
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.points_count:

            # Go in the positive direction, and decide how far to go.
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)           
            self.y_values.append(y)

    def get_step(self):
        """ Go in the positive direction, 
        and determine the distance for each step. """
        direction = choice([1])
        distance =  choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        return direction * distance
