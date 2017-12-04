import numpy as np

#
array = np.random.binomial(5, 0.5, size=100)
print(array[1:])
print(array[:-1])
diff = array[1:] - array[:-1]

print(diff)