"""
Configuration file for Mall Customers Clustering Analysis
Modify these settings to customize the analysis
"""

# ============================================
# DATA CONFIGURATION
# ============================================

# Input data file path
INPUT_FILE = 'data/Mall_Customers.csv'

# Output directory for results
OUTPUT_DIR = 'outputs/'

# ============================================
# CLUSTERING CONFIGURATION
# ============================================

# Optimal number of clusters to use
# Based on elbow method and silhouette analysis: 5 is optimal
# You can experiment with different values (2-10)
OPTIMAL_K = 5

# Random state for reproducibility
# Set to any integer for consistent results
# Use None for random results each time
RANDOM_STATE = 42

# Number of different initializations for K-Means
# Higher value = more thorough search but slower
N_INIT = 10

# Range of k values to test for optimization
# Default: 2 to 10
K_RANGE = range(2, 11)

# ============================================
# VISUALIZATION CONFIGURATION
# ============================================

# Matplotlib style
# Options: 'seaborn-v0_8-darkgrid', 'seaborn-v0_8', 'default', etc.
PLOT_STYLE = 'seaborn-v0_8-darkgrid'

# Color palette for visualizations
# Options: 'husl', 'viridis', 'plasma', 'inferno', 'coolwarm', etc.
COLOR_PALETTE = 'viridis'

# DPI for saved images (higher = better quality, larger file)
FIGURE_DPI = 300

# Figure sizes (width, height) in inches
FIGURE_SIZE_2D = (15, 12)
FIGURE_SIZE_3D = (14, 5)
FIGURE_SIZE_OPT = (14, 5)

# ============================================
# ANALYSIS CONFIGURATION
# ============================================

# Features to use for clustering
# Default: Annual Income and Spending Score
FEATURES = ['Annual Income (k$)', 'Spending Score (1-100)']

# Outlier detection method
# 'iqr' = Interquartile Range method
OUTLIER_METHOD = 'iqr'

# Outlier threshold for IQR method
# 1.5 is standard, 2.0 is conservative
IQR_MULTIPLIER = 1.5

# ============================================
# PREPROCESSING CONFIGURATION
# ============================================

# Standardization method
# 'standard' = StandardScaler (mean=0, std=1)
# 'minmax' = MinMaxScaler (0-1 range)
SCALER_TYPE = 'standard'

# Whether to keep outliers in analysis
# True = keep (more realistic), False = remove
KEEP_OUTLIERS = True

# ============================================
# OUTPUT CONFIGURATION
# ============================================

# Whether to generate PNG visualizations
GENERATE_PLOTS = True

# Whether to save clustered data to CSV
SAVE_CSV = True

# Whether to save summary to text file
SAVE_SUMMARY = True

# Whether to display plots (set False for headless/server environments)
SHOW_PLOTS = False

# Verbose output
VERBOSE = True

# ============================================
# CLUSTER NAMING
# ============================================

# Custom names for clusters (optional)
# If empty, will use default numeric names
CLUSTER_NAMES = {
    0: "Average Customers",
    1: "High-Value Spenders",
    2: "Budget Shoppers",
    3: "Wealthy Conservative",
    4: "Economical Seniors"
}

# ============================================
# ADVANCED PARAMETERS
# ============================================

# Maximum number of iterations for K-Means
MAX_ITER = 300

# Tolerance for convergence
TOLERANCE = 1e-4

# Whether to use k-means++ initialization
# True = better initial centroids, slower
# False = random initialization, faster
INIT_METHOD = 'k-means++'

# ============================================
# EXPERIMENTAL SETTINGS
# ============================================

# Whether to perform additional analyses
CALCULATE_DAVIES_BOULDIN = False
CALCULATE_CALINSKI_HARABASZ = False

# Whether to use different clustering algorithms
# Set to True to compare K-Means with others
COMPARE_ALGORITHMS = False
