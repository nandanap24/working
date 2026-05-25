# AI-ML-LLM 60 Day Lab

A structured 60-day hands-on journey to become an AI/ML Engineer through mathematics, coding, debugging, Git workflows, and real engineering practices.

---

# Week 1 — Foundation Engine

## Day 1 — AI Engineering Environment + Python Baseline

- Python setup
- Virtual environments
- Linux shell basics
- Project structure
- JSON/text file handling

## Day 2 — Git/GitHub Workflow + Clean Python

- Git workflow
- Branching and merge conflicts
- Type hints
- Dot product and weighted sums

## Day 3 — Linear Algebra for ML

- Vectors and matrices
- Matrix multiplication
- Transpose and norms
- Cosine similarity
- Shape algebra and debugging

## Day 4 — Eigenvectors, PCA Intuition, Probability Basics

- Mean, variance, covariance
- Eigenvalues and eigenvectors
- PCA pipeline
- Covariance matrix
- Probability distributions
- Dimensionality reduction intuition

---

# Project Structure

```bash id="ewm1ax"
ai-ml-llm-60day-lab/
│
├── src/
├── notes/
├── reports/
├── tests/
├── data/
└── README.md
```

---

# Key Mathematical Concepts

## Variance

Measures how much data spreads around the mean.

## Covariance

Measures how two variables move together.

- Positive covariance → variables increase together
- Negative covariance → one increases while the other decreases

## Eigenvectors and Eigenvalues

Eigenvectors represent important stable directions in data.

Eigenvalues measure the importance of those directions.

Core equation:

```text id="r4l4lq"
Av = λv
```

---

# PCA (Principal Component Analysis)

PCA reduces dimensions while preserving maximum variance.

PCA Pipeline:

1. Center data
2. Compute covariance matrix
3. Compute eigenvectors/eigenvalues
4. Select principal components
5. Project data into lower dimensions

---

# Cosine Similarity

Measures directional similarity between vectors.

Range:

- 1 → highly similar
- 0 → unrelated
- -1 → opposite direction

Used in:

- embeddings
- semantic search
- recommendation systems
- vector databases

---

# Engineering Practices

- Shape logging for debugging
- Success and failure case testing
- Git branching workflow
- Merge conflict handling
- Experimental observations
- README documentation
- Reproducible reports

---

# Example Commands

Run Day 4 PCA experiments:

```bash id="cg1vny"
python src/day4_pca_lab.py
```

Save outputs:

```bash id="j5x9fw"
python src/day4_pca_lab.py > reports/day4_output.txt
```

---

# Current Progress

Completed:

- Day 1
- Day 2
- Day 3
- Day 4

---

# Goals

Build strong foundations in:

- AI Engineering
- Machine Learning
- Deep Learning
- LLMs
- RAG Systems
- AI Deployment
- MLOps
