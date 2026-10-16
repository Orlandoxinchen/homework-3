"""Homework 3, Part 2.

Simulate the fraud-detection system from Part 1, Question 1.
Seed 42 and 100,000 transactions, as specified in the assignment.
"""

import numpy as np
import pandas as pd

# Step 1: Set random seed for reproducibility
np.random.seed(42)

# Step 2: Create 100,000 transactions
n_transactions = 100000

# Step 3: Determine which transactions are fraudulent (0.1% rate)
is_fraud = np.random.rand(n_transactions) < 0.001

# Step 4: Apply fraud detection system
# Fraudulent transactions: 98% chance of being flagged.
# Legitimate transactions: 5% chance of being flagged (false positive).
flagged = np.zeros(n_transactions, dtype=bool)
n_fraud = int(is_fraud.sum())
n_legit = n_transactions - n_fraud
flagged[is_fraud] = np.random.rand(n_fraud) < 0.98
flagged[~is_fraud] = np.random.rand(n_legit) < 0.05

# Step 5: Calculate empirical probability
# P(Fraud | Flagged) = (flagged AND fraud) / (total flagged)
fraud_and_flagged = int(np.sum(is_fraud & flagged))
total_flagged = int(np.sum(flagged))
empirical_prob = fraud_and_flagged / total_flagged

print(f"Empirical P(Fraud | Flagged) = {empirical_prob:.4f}")
print("Theoretical P(Fraud | Flagged) = 0.0192")

# Step 6: Confusion matrix (counts)
true_positive = int(np.sum(is_fraud & flagged))
false_positive = int(np.sum(~is_fraud & flagged))
true_negative = int(np.sum(~is_fraud & ~flagged))
false_negative = int(np.sum(is_fraud & ~flagged))

confusion = pd.DataFrame(
    {
        "Not flagged": [true_negative, false_negative],
        "Flagged": [false_positive, true_positive],
    },
    index=["Not fraud", "Fraud"],
)

print()
print(f"Transactions: {n_transactions:,}")
print(f"Fraudulent:   {n_fraud:,}")
print(f"Flagged:      {total_flagged:,}")
print(f"Fraud and flagged: {fraud_and_flagged:,}")
print()
print("Confusion matrix")
print(confusion.to_string())
print()
print(f"True positive:  {true_positive:,}")
print(f"False positive: {false_positive:,}")
print(f"True negative:  {true_negative:,}")
print(f"False negative: {false_negative:,}")
