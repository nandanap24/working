## Cosine Similarity

Cosine similarity measures angular similarity between vectors.
It is widely used in embeddings and semantic search.
Values closer to 1 indicate strong similarity.

## Matrix Multiplication

Matrix multiplication requires matching inner dimensions.
The resulting shape uses the outer dimensions.
Shape mismatches are common ML engineering errors.

## Matrix Multiplication Experiment

Changed matrix A values from small numbers to larger numbers.

### Effect

The resulting matrix values increased significantly.

### Engineering Insight

Larger input values increase weighted sums during matrix multiplication.
This directly affects neural network activations and model outputs.

## Important Rules

- Inner dimensions must match.
- Outer dimensions determine output shape.
- Shape mismatches are common ML bugs.
- Always print tensor shapes when debugging.
