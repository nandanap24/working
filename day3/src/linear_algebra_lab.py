import numpy as np

vector = np.array([3,4])

print("Vector : ", vector)
print("Shape : ",vector.shape)

norm = np.linalg.norm(vector)

print("Norm: ", norm)

matrix = np.array([[1,2,3],[4,5,6]])
transpose = matrix.T
print("Matrix: ",matrix)
print("Transpose: ",transpose)

A= np.array([[1,2,3]])
B= np.array([[2],[4],[6]])
matrix_multi = np.matmul(A,B)