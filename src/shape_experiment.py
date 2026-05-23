import numpy as np
arr = np.arange(6)
print(arr)

# reshaped
reshaped = arr.reshape(2,3)
print(reshaped)

print(reshaped.shape)

print(arr.reshape(3,2))
print(arr.reshape(4,2))