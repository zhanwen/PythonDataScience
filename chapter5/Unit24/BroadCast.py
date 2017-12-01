import numpy as np

# 0, 1, 2, 3
a = np.arange(4)
# 1, 2, 3, 4
b = np.arange(1, 5)
# 1, 3, 5, 7
c = a + b
# print(c)

# 0, 5, 10, 15
d = a * 5
# print(d)

noise = np.eye(4) + 0.01*np.ones((4,))

noise = np.eye(4) + 0.01*np.random.random([4, 4])
result = np.round(noise, 1)
