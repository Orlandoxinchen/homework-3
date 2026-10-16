# Homework 3

**Xinchen Leng**

Part 1 is solved below. Part 2 is the simulation in [`fraud_simulation.py`](fraud_simulation.py). Both are on this page, so the answers can be read without downloading a file.

Repository: https://github.com/Orlandoxinchen/homework-3

---

## Part 1. Analytical problems

### 1. Amazon fraud detection

The system is given by

- sensitivity: $P(\text{Flagged} \mid \text{Fraud}) = 0.98$
- specificity: $P(\text{Not flagged} \mid \text{Legitimate}) = 0.95$
- base rate: $P(\text{Fraud}) = 0.001$

Specificity fixes the false-positive rate, and the complement of the base rate is the legitimate share:

$$
P(\text{Flagged} \mid \text{Legitimate}) = 1 - 0.95 = 0.05,
$$

$$
P(\text{Legitimate}) = 1 - 0.001 = 0.999.
$$

#### 1(a). Probability that a flagged transaction is actually fraud

Bayes’ theorem:

$$
P(\text{Fraud} \mid \text{Flagged})
= \frac{P(\text{Flagged} \mid \text{Fraud})\,P(\text{Fraud})}{P(\text{Flagged})}.
$$

The denominator uses the law of total probability:

$$
\begin{aligned}
P(\text{Flagged})
&= P(\text{Flagged} \mid \text{Fraud})\,P(\text{Fraud})
 + P(\text{Flagged} \mid \text{Legitimate})\,P(\text{Legitimate}) \\
&= (0.98)(0.001) + (0.05)(0.999) \\
&= 0.00098 + 0.04995 \\
&= 0.05093.
\end{aligned}
$$

The numerator is the true-detection piece, $0.00098$:

$$
P(\text{Fraud} \mid \text{Flagged})
= \frac{0.00098}{0.05093}
= \frac{98}{5093}
\approx 0.01924.
$$

**Answer.** $0.01924$, about 1.92 percent. A flag is weak evidence of fraud. Fraud is rare, and a 5 percent false-positive rate applied to the 99.9 percent of transactions that are legitimate produces almost all of the flags.

#### 1(b). Specificity raised to 0.99

Now $P(\text{Flagged} \mid \text{Legitimate}) = 0.01$. Sensitivity and the base rate are unchanged:

$$
\begin{aligned}
P(\text{Flagged})
&= (0.98)(0.001) + (0.01)(0.999) \\
&= 0.00098 + 0.00999 \\
&= 0.01097,
\end{aligned}
$$

$$
P(\text{Fraud} \mid \text{Flagged})
= \frac{0.00098}{0.01097}
= \frac{98}{1097}
\approx 0.08933.
$$

**Answer.** $0.08933$, about 8.93 percent. The posterior is about 4.6 times the answer in part (a).

The business change is in the review queue, not in the share of fraud that is caught. Sensitivity is still 0.98, so the same fraction of fraudulent transactions is flagged. The false-positive rate falls from 5 percent to 1 percent. Flags drop from about 5.09 percent of all transactions to about 1.10 percent, and a reviewed flag is much more likely to be a real case. Automatic blocking is still a poor rule: even after the change, about 91 percent of flags are legitimate. The gain is a shorter queue and fewer good customers pulled into review.

### 2. Two independent tech stocks

Returns below are decimals. Independence means $\operatorname{Cov}(X, Y) = 0$.

| Stock A return | −2% | 0% | 3% | 5% |
| --- | ---: | ---: | ---: | ---: |
| $P(X)$ | 0.1 | 0.3 | 0.4 | 0.2 |

| Stock B return | 3% | 1% | 4% |
| --- | ---: | ---: | ---: |
| $P(Y)$ | 0.2 | 0.5 | 0.3 |

#### 2(a). Expected returns

$$
\begin{aligned}
E[X]
&= (-0.02)(0.1) + (0)(0.3) + (0.03)(0.4) + (0.05)(0.2) \\
&= -0.002 + 0 + 0.012 + 0.010 \\
&= 0.020.
\end{aligned}
$$

$$
\begin{aligned}
E[Y]
&= (0.03)(0.2) + (0.01)(0.5) + (0.04)(0.3) \\
&= 0.006 + 0.005 + 0.012 \\
&= 0.023.
\end{aligned}
$$

**Answer.** $E[X] = 0.020$ (2.00 percent). $E[Y] = 0.023$ (2.30 percent).

#### 2(b). Variances, shortcut formula

$$
\operatorname{Var}(X) = E[X^2] - (E[X])^2.
$$

$$
\begin{aligned}
E[X^2]
&= (-0.02)^2(0.1) + (0.03)^2(0.4) + (0.05)^2(0.2) \\
&= (0.0004)(0.1) + (0.0009)(0.4) + (0.0025)(0.2) \\
&= 0.00004 + 0.00036 + 0.00050 \\
&= 0.00090.
\end{aligned}
$$

$$
\operatorname{Var}(X) = 0.00090 - (0.020)^2 = 0.00090 - 0.00040 = 0.00050.
$$

$$
\begin{aligned}
E[Y^2]
&= (0.03)^2(0.2) + (0.01)^2(0.5) + (0.04)^2(0.3) \\
&= (0.0009)(0.2) + (0.0001)(0.5) + (0.0016)(0.3) \\
&= 0.00018 + 0.00005 + 0.00048 \\
&= 0.00071.
\end{aligned}
$$

$$
\operatorname{Var}(Y) = 0.00071 - (0.023)^2 = 0.00071 - 0.000529 = 0.000181.
$$

**Answer.** $\operatorname{Var}(X) = 0.00050$. $\operatorname{Var}(Y) = 0.000181$.

#### 2(c). Portfolio $R = 0.6X + 0.4Y$

Linearity of expectation does not need independence. Independence is used for the variance, where the covariance term drops out.

$$
E[R] = 0.6\,E[X] + 0.4\,E[Y] = 0.6(0.020) + 0.4(0.023) = 0.012 + 0.0092 = 0.0212.
$$

$$
\begin{aligned}
\operatorname{Var}(R)
&= (0.6)^2 \operatorname{Var}(X) + (0.4)^2 \operatorname{Var}(Y) \\
&= (0.36)(0.00050) + (0.16)(0.000181) \\
&= 0.000180 + 0.00002896 \\
&= 0.00020896.
\end{aligned}
$$

**Answer.** $E[R] = 0.0212$ (2.12 percent). $\operatorname{Var}(R) = 0.00020896$.

### 3. Server response time

$$
f(x) =
\begin{cases}
\dfrac{3}{8}x^2, & 0 \le x \le 2, \\
0, & \text{otherwise.}
\end{cases}
$$

#### 3(a). Valid PDF

On $[0, 2]$, $x^2 \ge 0$ and $3/8 > 0$, so $f(x) \ge 0$. Outside that interval the density is zero, which is also nonnegative.

$$
\int_0^2 \frac{3}{8}x^2 \, dx
= \frac{3}{8}\cdot\frac{x^3}{3}\Big|_0^2
= \frac{1}{8}x^3\Big|_0^2
= \frac{1}{8}(8) - 0
= 1.
$$

**Answer.** The function is nonnegative and integrates to 1, so it is a valid PDF.

#### 3(b). CDF on $[0, 2]$

$$
F(x) = P(X \le x) = \int_0^x \frac{3}{8}t^2 \, dt = \frac{1}{8}t^3\Big|_0^x = \frac{x^3}{8}, \qquad 0 \le x \le 2.
$$

**Answer.** $F(x) = x^3/8$ for $0 \le x \le 2$.

#### 3(c). Three probabilities

$$
P(X \le 1) = F(1) = \frac{1^3}{8} = \frac{1}{8} = 0.125.
$$

$$
\begin{aligned}
P(0.5 \le X \le 1.5)
&= F(1.5) - F(0.5) \\
&= \frac{(1.5)^3}{8} - \frac{(0.5)^3}{8} \\
&= \frac{3.375}{8} - \frac{0.125}{8} \\
&= 0.40625.
\end{aligned}
$$

In fractions, $(1.5)^3 = 27/8$ and $(0.5)^3 = 1/8$, so

$$
F(1.5) - F(0.5) = \frac{27}{64} - \frac{1}{64} = \frac{26}{64} = \frac{13}{32}.
$$

$$
P(X > 1.5) = 1 - F(1.5) = 1 - \frac{27}{64} = \frac{37}{64} = 0.578125.
$$

**Answer.** $P(X \le 1) = 1/8 = 0.125$. $P(0.5 \le X \le 1.5) = 13/32 = 0.40625$. $P(X > 1.5) = 37/64 = 0.578125$.

### 4. Binomial and hypergeometric

#### 4(a). Binomial

Each of 10 users clicks with probability 0.20, independently, so $X \sim \text{Binomial}(n = 10,\ p = 0.20)$.

$$
P(X = 3) = \binom{10}{3}(0.20)^3(0.80)^7.
$$

$$
\binom{10}{3} = 120, \qquad (0.20)^3 = 0.008, \qquad (0.80)^7 = 0.2097152.
$$

$$
P(X = 3) = 120 \times 0.008 \times 0.2097152 = 0.201326592.
$$

The same value as a reduced fraction, from $\binom{10}{3}(1/5)^3(4/5)^7$, is $393216/1953125$.

**Answer.** $P(X = 3) = 0.201326592$.

#### 4(b). Hypergeometric

The batch has $N = 20$ products, of which $K = 4$ are defective. The inspector draws $n = 5$ without replacement, so $Y \sim \text{Hypergeometric}(N = 20,\ K = 4,\ n = 5)$. Exactly one defective means 1 chosen from the 4 defectives and 4 chosen from the 16 good products:

$$
P(Y = 1) = \frac{\binom{4}{1}\binom{16}{4}}{\binom{20}{5}}.
$$

$$
\binom{4}{1} = 4,
$$

$$
\binom{16}{4} = \frac{16 \times 15 \times 14 \times 13}{4 \times 3 \times 2 \times 1} = 1820,
$$

$$
\binom{20}{5} = \frac{20 \times 19 \times 18 \times 17 \times 16}{120} = 15504.
$$

$$
P(Y = 1) = \frac{4 \times 1820}{15504} = \frac{7280}{15504} = \frac{455}{969} \approx 0.46956.
$$

**Answer.** $P(Y = 1) = 455/969 \approx 0.46956$.

---

## Part 2. Coding problem

The script [`fraud_simulation.py`](fraud_simulation.py) follows the assignment: seed 42, 100,000 transactions, fraud drawn at rate 0.001, fraudulent transactions flagged with probability 0.98, and legitimate transactions flagged with probability 0.05.

```bash
pip install -r requirements.txt
python fraud_simulation.py
```

With this seed the draw contains 102 fraudulent transactions, not the expected 100. Of those 102, 98 are flagged. Legitimate transactions contribute 4,894 flags.

$$
\widehat{P}(\text{Fraud} \mid \text{Flagged}) = \frac{98}{4992} = 0.0196,
$$

printed to four decimals, against the Part 1(a) value 0.0192. The two agree to three decimals. The gap is ordinary binomial noise in a rare-event sample.

|  | Not flagged | Flagged |
| --- | ---: | ---: |
| Not fraud | 95,004 | 4,894 |
| Fraud | 4 | 98 |

- True positive = 98 (fraud and flagged)
- False positive = 4,894 (not fraud and flagged)
- True negative = 95,004 (not fraud and not flagged)
- False negative = 4 (fraud and not flagged)

The false positives dominate the flagged column, which is the same fact Part 1(a) produced from Bayes’ theorem.

Program output:

```text
Empirical P(Fraud | Flagged) = 0.0196
Theoretical P(Fraud | Flagged) = 0.0192

Transactions: 100,000
Fraudulent:   102
Flagged:      4,992
Fraud and flagged: 98

Confusion matrix
           Not flagged  Flagged
Not fraud        95004     4894
Fraud                4       98

True positive:  98
False positive: 4,894
True negative:  95,004
False negative: 4
```
