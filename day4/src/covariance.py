import numpy as np

x= np.array([1,2,3,4])
y= np.array([2,4,6,8])

cov_matrix = np.cov(x,y)
print(cov_matrix)


# Your Output
# [
# 1.6667 3.3333
# 3.3333 6.6667]

# Structure of Covariance Matrix

# Covariance matrix format:

# [
# Cov(x,x) Cov(y,x)
# Cov(x,y) Cov(y,y)]