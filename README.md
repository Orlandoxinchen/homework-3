# Homework 3 — Fraud detection simulation

Xinchen Leng

Part 2 of Homework 3. The script simulates the fraud-detection system from Part 1, Question 1.

## Run

```bash
pip install -r requirements.txt
python fraud_simulation.py
```

The seed is 42 and the sample size is 100,000 transactions, as specified in the assignment.

## What it reports

- Empirical P(Fraud | Flagged), next to the Bayes answer from Part 1
- Confusion-matrix counts: true positive, false positive, true negative, false negative
