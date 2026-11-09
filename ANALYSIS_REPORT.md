# Mall Customers Clustering Analysis Report

## Executive Summary
This report presents a complete unsupervised learning clustering analysis on 200 mall customers using K-Means clustering. The analysis identified **5 optimal clusters** that segment customers based on their annual income and spending behavior patterns.

---

## 1. Data Overview
- **Total Records:** 200 customers
- **Features Used:** Annual Income (k$), Spending Score (1-100)
- **Data Quality:** No missing values, 2 minor outliers detected (retained as valid customer data)
- **Period:** Complete dataset

### Dataset Statistics
| Metric | Age | Annual Income | Spending Score |
|--------|-----|---------------|----------------|
| Mean | 38.9 years | $60.6k | 50.2/100 |
| Std Dev | 14.0 | 26.3 | 25.8 |
| Min | 18 | 15 | 1 |
| Max | 70 | 137 | 99 |

---

## 2. Data Cleaning Process

### Steps Performed:
1. ✓ **Missing Value Check:** No missing values found
2. ✓ **Duplicate Records:** No duplicates detected
3. ✓ **Outlier Detection:** 2 outliers found in Annual Income using IQR method
   - Decision: Retained (represent legitimate high-income customers)
4. ✓ **Data Standardization:** Applied StandardScaler to normalize features
   - Ensures equal feature contribution in clustering

---

## 3. Optimal Cluster Determination

### Methodology:
Two complementary methods were used to determine the optimal number of clusters:

#### a) **Elbow Method**
- Plots within-cluster sum of squares (inertia) vs number of clusters
- Identifies the "elbow" point where adding more clusters provides diminishing returns
- **Result:** Elbow observed around k=5

#### b) **Silhouette Score Analysis**
- Measures how similar an object is to its own cluster vs other clusters
- Range: -1 to 1 (higher is better)
- **Result:** Peak score of 0.5547 at k=5 clusters

### Results:
```
k=2: Inertia=269.69, Silhouette Score=0.3213
k=3: Inertia=157.70, Silhouette Score=0.4666
k=4: Inertia=108.92, Silhouette Score=0.4939
k=5: Inertia=65.57,  Silhouette Score=0.5547  ← OPTIMAL
k=6: Inertia=55.06,  Silhouette Score=0.5399
k=7: Inertia=44.86,  Silhouette Score=0.5281
```

**Conclusion:** **k=5 clusters** is optimal based on both methods.

---

## 4. Cluster Segmentation & Insights

### **Cluster 0: "Average Customers"** (40.5% - 81 customers)
- **Profile:** Middle-aged, moderate income and spending
- **Avg Age:** 42.7 years
- **Avg Income:** $55.3k
- **Avg Spending Score:** 49.5/100
- **Gender:** 59% Female, 41% Male
- **Business Insight:** Stable, consistent customer base; potential for targeted marketing

### **Cluster 1: "High-Value Spenders"** (19.5% - 39 customers)
- **Profile:** Young professionals with high income AND high spending
- **Avg Age:** 32.7 years
- **Avg Income:** $86.5k
- **Avg Spending Score:** 82.1/100
- **Gender:** 54% Female, 46% Male
- **Business Insight:** Premium customers; invest in loyalty programs and premium services

### **Cluster 2: "Budget Shoppers"** (11.0% - 22 customers)
- **Profile:** Young, low income but enthusiastic shoppers
- **Avg Age:** 25.3 years
- **Avg Income:** $25.7k
- **Avg Spending Score:** 79.4/100
- **Gender:** 59% Female, 41% Male
- **Business Insight:** Price-conscious; focus on promotions and value offerings

### **Cluster 3: "Wealthy Conservative Spenders"** (17.5% - 35 customers)
- **Profile:** Affluent but cautious with spending
- **Avg Age:** 41.1 years
- **Avg Income:** $88.2k
- **Avg Spending Score:** 17.1/100
- **Gender:** 54% Male, 46% Female
- **Business Insight:** High purchasing power but selective; focus on quality and exclusivity

### **Cluster 4: "Economical Seniors"** (11.5% - 23 customers)
- **Profile:** Older, lower income, low spending
- **Avg Age:** 45.2 years
- **Avg Income:** $26.3k
- **Avg Spending Score:** 20.9/100
- **Gender:** 61% Female, 39% Male
- **Business Insight:** Budget-limited; offer essential products and senior discounts

---

## 5. Visualizations Generated

### 1. **Cluster Optimization Analysis**
- Elbow Method Plot: Shows diminishing returns after k=5
- Silhouette Score Plot: Confirms k=5 as optimal with highest cohesion

### 2. **Cluster Visualizations (2D)**
- **Income vs Spending Score:** Main clustering pattern - shows clear customer segments
- **Age vs Spending Score:** Identifies age-based spending behavior
- **Age vs Income:** Reveals age-income-spending relationships
- **Cluster Distribution:** Size and population of each segment

### 3. **Advanced Visualizations**
- **3D Scatter Plot:** Multi-dimensional view of all three variables
- **Silhouette Plot:** Quality assessment of cluster membership
  - Wider sections = more consistent clusters
  - Cluster 5 shows good internal cohesion

---

## 6. Model Performance Metrics

### Silhouette Analysis:
- **Overall Silhouette Score:** 0.5547 (Good - indicates well-separated clusters)
- **Range:** 0.3 to 0.7 is typical for good clustering
- **Interpretation:** Clusters are reasonably well-defined with low overlap

### Cluster Quality:
| Cluster | Size | Quality |
|---------|------|---------|
| Cluster 0 | 81 | Good (Largest, stable) |
| Cluster 1 | 39 | Very Good (Premium segment) |
| Cluster 2 | 22 | Good (High spending energy) |
| Cluster 3 | 35 | Good (Affluent segment) |
| Cluster 4 | 23 | Good (Clear characteristics) |

---

## 7. Business Recommendations

### 1. **Cluster 1 - High-Value Spenders**
   - Strategy: VIP treatment and premium membership
   - Actions: Exclusive offers, early access to new products, dedicated customer service

### 2. **Cluster 0 - Average Customers**
   - Strategy: Retention and loyalty building
   - Actions: Regular promotions, seasonal offers, community engagement

### 3. **Cluster 2 - Budget Shoppers**
   - Strategy: Value and volume-based
   - Actions: Discounts, bulk offers, student programs, financing options

### 4. **Cluster 3 - Wealthy Conservative**
   - Strategy: Quality and exclusivity
   - Actions: Premium products, white-glove service, luxury experiences

### 5. **Cluster 4 - Economical Seniors**
   - Strategy: Affordability and accessibility
   - Actions: Senior discounts, easy shopping experience, essential products

---

## 8. Algorithm Details

### K-Means Clustering
- **Algorithm:** K-Means (Lloyd's Algorithm)
- **Distance Metric:** Euclidean Distance
- **Optimization:** 10 initializations to avoid local minima
- **Convergence:** Achieved successfully

### Preprocessing:
- **Standardization:** StandardScaler (mean=0, std=1)
- **Features:** Annual Income, Spending Score
- **Rationale:** Equal feature scaling prevents high-range features from dominating

---

## 9. Output Files Generated

1. **01_Cluster_Optimization.png**
   - Elbow Method and Silhouette Score analysis
   - Helps visualize why k=5 was chosen

2. **02_Cluster_Visualizations.png**
   - Four 2D scatter plots showing cluster patterns
   - Includes centroid markers (red X)
   - Distribution histogram

3. **03_3D_and_Silhouette.png**
   - 3D visualization of all features
   - Silhouette plot for quality assessment

4. **Clustered_Customers.csv**
   - Original data with assigned cluster labels
   - Ready for further analysis or business implementation

5. **Cluster_Summary.txt**
   - Text-based summary of all cluster statistics

---

## 10. Conclusion

The unsupervised clustering analysis successfully identified **5 distinct customer segments** based on spending behavior and income. Each cluster represents a unique market opportunity with specific characteristics:

- **40.5%** are stable, average spenders (Cluster 0)
- **19.5%** are high-value, high-income spenders (Cluster 1)
- **11%** are young budget-conscious shoppers (Cluster 2)
- **17.5%** are affluent but selective buyers (Cluster 3)
- **11.5%** are economical, lower-income customers (Cluster 4)

**Model Quality:** Good (Silhouette Score: 0.5547)

These insights enable targeted marketing strategies, personalized product recommendations, and optimized customer service approaches for maximum business impact.

---

## Technical Notes

- **Programming Language:** Python
- **Libraries:** scikit-learn, pandas, numpy, matplotlib, seaborn
- **Execution Time:** < 5 seconds
- **Reproducibility:** Random state set to 42 for consistent results
