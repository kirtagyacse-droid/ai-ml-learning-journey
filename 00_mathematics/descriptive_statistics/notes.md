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
