import numpy as np

x= np.array([[1,2],[2,4],[3,6],[4,8]])
print("Shape of X: ",x.shape)

mean = np.mean(x, axis=0)
x_centered = x- mean
print("X_centered : ", x_centered)
print("Centered_shape : ",x_centered)

cov_matrix = np.cov(x_centered.T)
print("Cov_matrix : ",cov_matrix)
print("Covariance_shape : ",cov_matrix.shape)

eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
print("Eigenvalues :",eigenvalues)
print("Eigenvalues shape : ",eigenvalues.shape)

print("Eigenvectors : ",eigenvectors)
print("Eigenvectors shape : ",eigenvectors.shape)

principal_component = eigenvectors[:,0]
print("Principal component : ",principal_component)
print("Principal component shape : ",principal_component.shape)

projected_data = np.dot(x_centered,principal_component)
print("Projected_data : ",projected_data)
print("Projected shape : ",projected_data.shape)