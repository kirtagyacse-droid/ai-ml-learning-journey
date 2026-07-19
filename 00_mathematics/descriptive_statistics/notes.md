# Mathematics for Machine Learning - CampusX
- **Source:** Video 2 & 3 of CampusX's 23-video Mathematics for ML playlist.
## Topic: Descriptive Statistics
### 1. Measures of Central Tendency
- **Mean:** The arithmetic average of the data distribution, highly sensitive to outliers.
- **Median:** The middle value of a sorted dataset; acts as a robust metric against extreme skewness.
- **Mode:** The most frequently occurring element in the dataset; useful for categorical data features.
### 2. Measures of Dispersion
- **Variance & Standard Deviation:** Quantifies the spread or volatility of data points relative to the mean.

## Topic: Percentiles, Quartiles & Box Plots
- **Source:** Video 4 of CampusX's Mathematics for ML playlist.
### 1. Percentiles
- **Definition:** A metric indicating the value below which a given percentage of observations falls (e.g., the 80th percentile).
### 2. Quartiles & IQR
- **Quartiles (Q1, Q2, Q3):** Splits data distributions into quarters. Q1 is the 25th percentile, Q2 is the median (50th), and Q3 is the 75th percentile.
- **Interquartile Range (IQR):** Calculated as $IQR = Q3 - Q1$. Measures the statistical dispersion of the middle 50% of the dataset.
### 3. Outlier Detection via Five-Number Summary
- **Box Plot Criteria:** Outliers are mathematically flagged if data points lie outside the fences: $[Q1 - 1.5 \times IQR, Q3 + 1.5 \times IQR]$.

## Topic: Covariance, Correlation & Feature Relationships
- **Source:** Video 5 of CampusX's Mathematics for ML playlist.
### 1. Covariance
- **Definition:** Measures the directional relationship between two random variables.
- **Limitation:** Only tells the direction (positive/negative), not the magnitude or strength, because it is scale-dependent.
### 2. Pearson Correlation Coefficient
- **Definition:** Scales covariance to a range between -1 and +1 by dividing it by the product of the standard deviations.
- **Application:** Used during feature selection to drops collinear variables that introduce multi-collinearity errors into models.
### 3. Correlation vs Causation
- **Key Rule:** High mathematical correlation between features does not imply that one variable causes the change in the other.

## Topic: Random Variables & Probability Distributions
- **Source:** Video 6 of CampusX's Mathematics for ML playlist.
### 1. Random Variables
- **Definition:** A variable whose values are numerical outcomes of a random phenomenon.
### 2. Types of Distributions
- **Discrete Random Variable:** Has countable outcomes. Mapped using a Probability Mass Function (PMF).
- **Continuous Random Variable:** Has infinite outcomes. Mapped using a Probability Density Function (PDF).
### 3. Cumulative Distribution Function (CDF)
- **CDF:** Measures the probability that a random variable X takes a value less than or equal to x. Expressed as $F(x) = P(X \le x)$.

## Topic: Probability Distributions & The Normal Distribution
- **Source:** Video 7 of CampusX's Mathematics for ML playlist.
### 1. The Gaussian (Normal) Distribution
- **Bell Curve:** Characterized by its symmetrical shape where the mean, median, and mode are all equal.
- **Empirical Rule (68-95-99.7):** Specifies the percentage of data falling within 1, 2, and 3 standard deviations from the mean.
### 2. Standard Normal Distribution & Z-Scores
- **Z-Score Normalization:** Transforms a normal distribution to have a mean of 0 and a standard deviation of 1 using the formula: Z = (x - mean) / std.
- **Application:** Critical for feature scaling pipelines before feeding data into distance-based algorithms like KNN or K-Means.

## Topic: Skewness, Kurtosis & Data Transformations
- **Source:** Video 8 of CampusX's Mathematics for ML playlist.
### 1. Skewness
- **Asymmetry Metrics:** Measures the lack of symmetry in a distribution. Positive skew indicates a long tail to the right; negative skew indicates a long tail to the left.
### 2. Kurtosis
- **Tail Heaviness:** Quantifies the combined weight of a distribution's tails relative to the center (Mesokurtic, Leptokurtic, and Platykurtic).
### 3. Power Transformations
- **Normalizing Data:** Using mathematical functions like Log Transform and Box-Cox to stabilize variance and transform skewed data into a normal distribution.

## Topic: Comprehensive Review - Core Descriptive Statistics (Videos 2-8)
- **Review Range:** Intensive review of Videos 2 through 8 of CampusX's Mathematics for ML playlist.
### Phase 1: Central Tendency & Dispersion Re-evaluation
- Verified Mean equations under heavy outlier skew conditions.
