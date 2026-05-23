import numpy as np

a= np.array([1,2,3])
b= np.array([4,5,6]) # b= np.array([10,10,10])

result= np.dot(a,b)

print("Vector a :",a)
print("Shape a :", a.shape)

print("Vector b :",b)
print("Shape b :", b.shape)

print("Dotproduct of a&b :", result)

### Engineering Insight
# Larger weights increase contribution of features in weighted sums.
# This is foundational to neural network computations.