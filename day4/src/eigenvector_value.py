import numpy as np
matrix = np.array([[2,0],[0,3]])

eigenvalues,eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues : ",eigenvalues)
print("Eigenvectors : ",eigenvectors)
