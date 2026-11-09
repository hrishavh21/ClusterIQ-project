# Mall Customers Clustering Analysis

A comprehensive unsupervised learning project using K-Means clustering to segment mall customers based on their spending behavior and annual income. This project demonstrates data cleaning, optimal cluster determination, visualization, and business insights generation.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)
- [Cluster Profiles](#cluster-profiles)
- [Visualizations](#visualizations)
- [Technical Details](#technical-details)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Project Overview

This project performs **unsupervised learning** using **K-Means clustering** to identify distinct customer segments in a mall. The analysis includes:

- ✅ Data cleaning and preprocessing
- ✅ Optimal cluster determination (Elbow Method & Silhouette Score)
- ✅ 2D and 3D cluster visualizations
- ✅ Detailed cluster profiling and business insights
- ✅ Statistical analysis of customer segments

**Optimal Result:** 5 distinct customer clusters identified with high quality (Silhouette Score: 0.5547)

---

## ✨ Features

- **Comprehensive Data Cleaning**
  - Missing value detection
  - Duplicate removal
  - Outlier identification (IQR method)

- **Multiple Cluster Optimization Methods**
  - Elbow Method (Inertia analysis)
  - Silhouette Score analysis
  - Visual comparison of both methods

- **Advanced Visualizations**
  - 2D scatter plots (Income vs Spending, Age vs Spending, etc.)
  - 3D cluster visualization
  - Silhouette plots for quality assessment
  - Cluster distribution histogram

- **Detailed Analysis**
  - Cluster profiling (size, demographics, spending patterns)
  - Gender distribution per cluster
  - Age and income analysis
  - Business recommendations

---

## 📊 Dataset

**Source:** Mall Customer Segmentation Data

**File:** `data/Mall_Customers.csv`

**Attributes:**
| Column | Description | Data Type |
|--------|-------------|-----------|
| CustomerID | Unique customer identifier | Integer |
| Gender | Male or Female | Categorical |
| Age | Customer age in years | Integer |
| Annual Income (k$) | Annual income in thousands | Integer |
| Spending Score (1-100) | Shop spending score assigned | Integer |

**Statistics:**
- Total Records: 200 customers
- Age Range: 18-70 years
- Income Range: $15k-$137k
- Spending Score Range: 1-100

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/mall-customers-clustering.git
cd mall-customers-clustering
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Prepare Data
Ensure your dataset is placed in the `data/` directory:
```
your-project/
├── data/
│   └── Mall_Customers.csv
├── outputs/
├── main.py
└── requirements.txt
```

---

## 💻 Usage

### Run the Complete Analysis
```bash
python main.py
```

### Expected Output
The script will generate:

1. **Console Output:**
   - Dataset overview and statistics
   - Data cleaning report
   - Cluster optimization analysis
   - Detailed cluster profiles

2. **Generated Files in `outputs/` folder:**
   - `01_Cluster_Optimization.png` - Elbow method and silhouette analysis
   - `02_Cluster_Visualizations.png` - 2D scatter plots
   - `03_3D_and_Silhouette.png` - 3D visualization and silhouette plot
   - `Clustered_Customers.csv` - Original data with cluster assignments
   - `Cluster_Summary.txt` - Text report of cluster statistics

### Customization

You can modify the following parameters in `main.py`:

```python
# Configuration (lines 17-21)
RANDOM_STATE = 42           # For reproducibility
OPTIMAL_K = 5               # Number of clusters (change if needed)
INPUT_FILE = 'data/Mall_Customers.csv'
OUTPUT_DIR = 'outputs/'
```

---

## 📁 Project Structure

```
mall-customers-clustering/
│
├── data/
│   └── Mall_Customers.csv          # Input dataset
│
├── outputs/                        # Generated results (created after running)
│   ├── 01_Cluster_Optimization.png
│   ├── 02_Cluster_Visualizations.png
│   ├── 03_3D_and_Silhouette.png
│   ├── Clustered_Customers.csv
│   └── Cluster_Summary.txt
│
├── main.py                         # Main analysis script
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
└── LICENSE                         # License file
```

---

## 📈 Results

### Optimal Cluster Analysis

| K Value | Inertia | Silhouette Score | Observation |
|---------|---------|------------------|-------------|
| 2 | 269.69 | 0.3213 | Poor separation |
| 3 | 157.70 | 0.4666 | Moderate |
| 4 | 108.92 | 0.4939 | Good |
| **5** | **65.57** | **0.5547** | **Optimal** ✓ |
| 6 | 55.06 | 0.5399 | Diminishing returns |
| 7 | 44.86 | 0.5281 | Diminishing returns |

**Conclusion:** k=5 provides the best balance between model complexity and cluster quality.

---

## 👥 Cluster Profiles

### Cluster 0: "Average Customers" (40.5% of customers)
- **Size:** 81 customers
- **Avg Age:** 42.7 years
- **Avg Income:** $55.3k
- **Avg Spending Score:** 49.5/100
- **Profile:** Middle-aged, moderate income and spending habits
- **Business Strategy:** Retention and loyalty programs

### Cluster 1: "High-Value Spenders" (19.5% of customers)
- **Size:** 39 customers
- **Avg Age:** 32.7 years
- **Avg Income:** $86.5k
- **Avg Spending Score:** 82.1/100
- **Profile:** Young professionals with high income and enthusiasm
- **Business Strategy:** Premium membership and exclusive offers

### Cluster 2: "Budget Shoppers" (11.0% of customers)
- **Size:** 22 customers
- **Avg Age:** 25.3 years
- **Avg Income:** $25.7k
- **Avg Spending Score:** 79.4/100
- **Profile:** Young, price-conscious but enthusiastic
- **Business Strategy:** Discounts and value promotions

### Cluster 3: "Wealthy Conservative Spenders" (17.5% of customers)
- **Size:** 35 customers
- **Avg Age:** 41.1 years
- **Avg Income:** $88.2k
- **Avg Spending Score:** 17.1/100
- **Profile:** Affluent but selective buyers
- **Business Strategy:** Premium quality and exclusivity focus

### Cluster 4: "Economical Seniors" (11.5% of customers)
- **Size:** 23 customers
- **Avg Age:** 45.2 years
- **Avg Income:** $26.3k
- **Avg Spending Score:** 20.9/100
- **Profile:** Lower income, budget-limited
- **Business Strategy:** Essential products and senior discounts

---

## 📊 Visualizations

### 1. Cluster Optimization Plots
- **Elbow Method:** Shows diminishing returns after k=5
- **Silhouette Score:** Peaks at k=5 (0.5547)

### 2. 2D Cluster Scatter Plots
- **Income vs Spending Score:** Primary segmentation pattern
- **Age vs Spending Score:** Age-based spending behavior
- **Age vs Income:** Age-income relationships
- **Cluster Distribution:** Size of each segment

### 3. 3D Visualization
- Multi-dimensional view of Age, Income, and Spending Score
- Color-coded by cluster membership

### 4. Silhouette Plot
- Quality assessment of cluster membership
- Measures how well-separated clusters are
- Wider sections indicate consistent clusters

---

## 🔧 Technical Details

### Algorithm: K-Means Clustering
- **Distance Metric:** Euclidean Distance
- **Initialization:** k-means++ (10 different initializations)
- **Optimization:** Lloyd's Algorithm
- **Convergence:** Achieved with inertia minimization

### Preprocessing
- **Standardization:** StandardScaler (zero mean, unit variance)
- **Rationale:** Prevents high-range features from dominating
- **Features Used:** Annual Income, Spending Score

### Evaluation Metrics
- **Silhouette Score:** 0.5547 (Good - indicates well-separated clusters)
- **Inertia:** 65.57 (Within-cluster sum of squares)
- **Davies-Bouldin Index:** Useful for cluster separation

### Libraries Used
- **pandas:** Data manipulation and analysis
- **numpy:** Numerical computing
- **scikit-learn:** Machine learning algorithms
- **matplotlib:** Data visualization
- **seaborn:** Statistical visualization

---

## 📝 How to Interpret Results

### Elbow Method
- Look for the "elbow" point where inertia levels off
- Adding clusters beyond this point provides little improvement
- In this case: clear elbow at k=5

### Silhouette Score
- Range: -1 to 1
- Higher values indicate better-defined clusters
- 0.5547 indicates good cluster quality
- Negative values suggest wrong cluster assignment

### Cluster Profiling
- Use cluster statistics to understand customer characteristics
- Identify patterns in age, income, and spending
- Develop targeted business strategies per segment

---

## 🚀 Future Enhancements

- [ ] Implement hierarchical clustering for comparison
- [ ] Add DBSCAN clustering algorithm
- [ ] Include customer demographics in analysis
- [ ] Create interactive dashboard with Plotly/Dash
- [ ] Add time-series analysis for seasonal patterns
- [ ] Implement automated cluster naming
- [ ] Add predictive models for new customer assignment
- [ ] Integration with business intelligence tools

---

## 📚 Learning Resources

- [K-Means Clustering - scikit-learn Documentation](https://scikit-learn.org/stable/modules/clustering.html#k-means)
- [Silhouette Score Explanation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html)
- [Unsupervised Learning Guide](https://en.wikipedia.org/wiki/Unsupervised_learning)

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Created as an unsupervised learning project for customer segmentation analysis.

---

## 📧 Contact & Support

- Issues: [GitHub Issues](https://github.com/yourusername/mall-customers-clustering/issues)
- Email: your.email@example.com

---

## 🎓 Academic Reference

This project demonstrates key concepts in:
- **Unsupervised Learning:** K-Means clustering algorithm
- **Data Preprocessing:** Standardization and outlier detection
- **Model Evaluation:** Silhouette analysis and elbow method
- **Data Visualization:** 2D/3D plotting and statistical graphics
- **Business Analytics:** Customer segmentation and profiling

---

**⭐ If you found this project helpful, please give it a star!**

Last Updated: October 2024
