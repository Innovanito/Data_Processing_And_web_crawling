import numpy as np

# 1
array1 = np.arange(12).reshape(4, 3)
arr2 = array1 * 10
arr3 = arr2 + 10
# print(arr3)

# 2
# print(arr3[[0, 1], [1, 2]])

# 3
print(arr3[2:4, 1:3])
# print(arr3[[0, 1], [0, 2]])
