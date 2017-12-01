import numpy as np

"""
 If true (default), then the object is copied.  Otherwise, a copy will
            only be made if __array__ returns a copy, if obj is a nested sequence,
            or if a copy is needed to satisfy any of the other requirements
            (`dtype`, `order`, etc.).
"""
numbers = np.array(range(1, 11), copy=True)
# print(numbers)

ones = np.ones([2, 4], dtype=np.float64)
# print(ones)

zeros = np.zeros([2, 4], dtype=np.float64)
# print(zeros)

empty = np.empty([2, 4], dtype=np.float64)
# print(empty)

# shape
ones.shape

# type
zeros.dtype

# ndim
numbers.ndim

eye = np.eye(3, k=1)
# print(eye)

np_numbers = np.arange(2, 5, 0.25)

# copy array
np_numbers_copy = np_numbers.copy()

#
np_numbers = np_numbers.astype(np.int)