import numpy as np

# # Some synthetic data for testing
array = np.random.binomial(5, 0.5, size=100)
print(array[1:])
print(array[:-1])

# The partial differences: slicing & broadcasting!
diff = array[1:] - array[:-1]

print(diff)