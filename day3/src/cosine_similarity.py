import numpy as np

vector_a = np.array([1,2,3])
vector_b = np.array([4,5,6])

cosine_similarity = (np.dot(vector_a,vector_b)/(np.linalg.norm(vector_a)*np.linalg.norm(vector_b)))
print("Cosine similarity : ",cosine_similarity)