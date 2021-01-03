from math import pi

import numpy as np


# Calculation of where the vehicle will be after 0.2 seconds.
def after_time(matrix: np.ndarray):
    print(matrix)
    # TODO


if __name__ == '__main__':
    # Set the initial values, units are [m][m][][rad/sec]
    vector = [[3], [5], [0.7 * pi], [0.2]]

    after_time(np.array(vector))
