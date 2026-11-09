"""
Mall Customers Clustering Analysis
Unsupervised Learning Project using K-Means Clustering

Author: [Your Name]
Date: 2024
Description: This script performs comprehensive clustering analysis on mall customer data
using K-Means algorithm. It includes data cleaning, optimal cluster determination,
visualization, and detailed cluster profiling.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples
from mpl_toolkits.mplot3d import Axes3D
import warnings
warnings.filterwarnings('ignore')

# ============================================
# Configuration
# ============================================
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
RANDOM_STATE = 42
OPTIMAL_K = 5
INPUT_FILE = 'data/Mall_Customers.csv'
OUTPUT_DIR = 'outputs/'

# ============================================
# 1. LOAD AND EXPLORE THE DATA
# ============================================
def load_and_explore_data(filepath):
    """Load dataset and display basic information"""
    print("="*60)
    print("MALL CUSTOMERS CLUSTERING ANALYSIS")
    print("="*60)
    
    df = pd.read_csv(filepath)
    
    print("\n1. DATASET OVERVIEW")
    print("-" * 60)
    print(f"Dataset shape: {df.shape}")
    print(f"\nFirst few rows:")
    print(df.head())
    print(f"\nData types:\n{df.dtypes}")
    print(f"\nBasic statistics:\n{df.describe()}")
    
    return df


# ============================================
# 2. DATA CLEANING
# ============================================
def clean_data(df):
    """Perform data cleaning operations"""
    print("\n2. DATA CLEANING")
    print("-" * 60)
    
    # Check for missing values
    print(f"Missing values:\n{df.isnull().sum()}")
    
    # Check for duplicates
    duplicates = df.duplicated().sum()
    print(f"Duplicate rows: {duplicates}")
    
    # Check for outliers using IQR method
    print(f"\nChecking for outliers...")
    
    def detect_outliers(data):
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        outliers = ((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).sum()
        return outliers
    
    numeric_cols = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
    for col in numeric_cols:
        outlier_count = detect_outliers(df[col])
        print(f"  {col}: {outlier_count} outliers detected")
    
    print("\n✓ Data cleaned successfully!")
    print(f"Final dataset shape: {df.shape}")
    
    return df


# ============================================
# 3. FEATURE SELECTION AND STANDARDIZATION
# ============================================
def prepare_features(df):
    """Select and standardize features for clustering"""
    print("\n3. FEATURE SELECTION FOR CLUSTERING")
    print("-" * 60)
    
    # Select features
    features = ['Annual Income (k$)', 'Spending Score (1-100)']
    X = df[features].copy()
    
    print(f"Features for clustering: {features}")
    print(f"\nFeature statistics:\n{X.describe()}")
    
    # Standardize features
    print("\n4. DATA STANDARDIZATION")
    print("-" * 60)
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("✓ Features standardized using StandardScaler")
    
    return X, X_scaled, scaler, features


# ============================================
# 5. FIND OPTIMAL NUMBER OF CLUSTERS
# ============================================
def find_optimal_clusters(X_scaled, k_range=range(2, 11)):
    """Determine optimal number of clusters using Elbow and Silhouette methods"""
    print("\n5. FINDING OPTIMAL NUMBER OF CLUSTERS")
    print("-" * 60)
    
    inertias = []
    silhouette_scores = []
    
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=10)
        kmeans.fit(X_scaled)
        inertias.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))
    
    print(f"\nElbow Method Results:")
    for k, inertia, sil_score in zip(k_range, inertias, silhouette_scores):
        print(f"  k={k}: Inertia={inertia:.2f}, Silhouette Score={sil_score:.4f}")
    
    return inertias, silhouette_scores, list(k_range)


# ============================================
# 6. VISUALIZE CLUSTER OPTIMIZATION
# ============================================
def plot_optimization(k_range, inertias, silhouette_scores):
    """Create visualization for cluster optimization analysis"""
    print("\n6. CREATING OPTIMIZATION VISUALIZATIONS")
    print("-" * 60)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Elbow Method Plot
    axes[0].plot(k_range, inertias, 'bo-', linewidth=2, markersize=8)
    axes[0].set_xlabel('Number of Clusters (k)', fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Inertia (Within-cluster Sum of Squares)', fontsize=12, fontweight='bold')
    axes[0].set_title('Elbow Method For Optimal k', fontsize=13, fontweight='bold')
    axes[0].grid(True, alpha=0.3)
    axes[0].set_xticks(k_range)
    
    # Silhouette Score Plot
    axes[1].plot(k_range, silhouette_scores, 'go-', linewidth=2, markersize=8)
    axes[1].set_xlabel('Number of Clusters (k)', fontsize=12, fontweight='bold')
    axes[1].set_ylabel('Silhouette Score', fontsize=12, fontweight='bold')
    axes[1].set_title('Silhouette Score For Different k', fontsize=13, fontweight='bold')
    axes[1].grid(True, alpha=0.3)
    axes[1].set_xticks(k_range)
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}01_Cluster_Optimization.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: 01_Cluster_Optimization.png")
    plt.close()


# ============================================
# 7. PERFORM CLUSTERING
# ============================================
def perform_clustering(X_scaled, k=OPTIMAL_K):
    """Perform K-Means clustering with optimal k"""
    print("\n7. PERFORMING CLUSTERING")
    print("-" * 60)
    print(f"Optimal number of clusters selected: {k}")
    
    kmeans = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=10)
    cluster_labels = kmeans.fit_predict(X_scaled)
    
    print(f"✓ K-Means clustering completed")
    
    return kmeans, cluster_labels


# ============================================
# 8. CLUSTER VISUALIZATION
# ============================================
def plot_clusters_2d(df, scaler, kmeans, optimal_k):
    """Create 2D cluster visualizations"""
    print("\n8. CREATING CLUSTER VISUALIZATIONS")
    print("-" * 60)
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # Plot 1: Clusters by Annual Income vs Spending Score
    ax1 = axes[0, 0]
    scatter = ax1.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], 
                          c=df['Cluster'], cmap='viridis', s=100, alpha=0.6, 
                          edgecolors='black', linewidth=0.5)
    ax1.scatter(scaler.inverse_transform(kmeans.cluster_centers_)[:, 0],
               scaler.inverse_transform(kmeans.cluster_centers_)[:, 1],
               c='red', marker='X', s=300, edgecolors='black', linewidth=2, label='Centroids')
    ax1.set_xlabel('Annual Income (k$)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Spending Score (1-100)', fontsize=11, fontweight='bold')
    ax1.set_title(f'Clusters: Annual Income vs Spending Score (k={optimal_k})', 
                  fontsize=12, fontweight='bold')
    ax1.legend()
    plt.colorbar(scatter, ax=ax1, label='Cluster')
    
    # Plot 2: Clusters by Age vs Spending Score
    ax2 = axes[0, 1]
    scatter2 = ax2.scatter(df['Age'], df['Spending Score (1-100)'], 
                           c=df['Cluster'], cmap='viridis', s=100, alpha=0.6, 
                           edgecolors='black', linewidth=0.5)
    ax2.set_xlabel('Age', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Spending Score (1-100)', fontsize=11, fontweight='bold')
    ax2.set_title(f'Clusters: Age vs Spending Score (k={optimal_k})', 
                  fontsize=12, fontweight='bold')
    plt.colorbar(scatter2, ax=ax2, label='Cluster')
    
    # Plot 3: Clusters by Age vs Annual Income
    ax3 = axes[1, 0]
    scatter3 = ax3.scatter(df['Age'], df['Annual Income (k$)'], 
                           c=df['Cluster'], cmap='viridis', s=100, alpha=0.6, 
                           edgecolors='black', linewidth=0.5)
    ax3.set_xlabel('Age', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Annual Income (k$)', fontsize=11, fontweight='bold')
    ax3.set_title(f'Clusters: Age vs Annual Income (k={optimal_k})', 
                  fontsize=12, fontweight='bold')
    plt.colorbar(scatter3, ax=ax3, label='Cluster')
    
    # Plot 4: Cluster size distribution
    ax4 = axes[1, 1]
    cluster_counts = df['Cluster'].value_counts().sort_index()
    colors = plt.cm.viridis(np.linspace(0, 1, optimal_k))
    bars = ax4.bar(cluster_counts.index, cluster_counts.values, color=colors, 
                   edgecolor='black', linewidth=1.5)
    ax4.set_xlabel('Cluster', fontsize=11, fontweight='bold')
    ax4.set_ylabel('Number of Customers', fontsize=11, fontweight='bold')
    ax4.set_title('Customer Distribution Across Clusters', fontsize=12, fontweight='bold')
    ax4.set_xticks(range(optimal_k))
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}02_Cluster_Visualizations.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: 02_Cluster_Visualizations.png")
    plt.close()




# ============================================
# 9. CLUSTER ANALYSIS AND INSIGHTS
# ============================================
def analyze_clusters(df, optimal_k):
    """Print detailed cluster analysis"""
    print("\n9. CLUSTER ANALYSIS & INSIGHTS")
    print("-" * 60)
    
    cluster_profiles = {}
    
    for cluster in range(optimal_k):
        cluster_data = df[df['Cluster'] == cluster]
        
        profile = {
            'size': len(cluster_data),
            'percentage': (len(cluster_data)/len(df))*100,
            'avg_age': cluster_data['Age'].mean(),
            'avg_income': cluster_data['Annual Income (k$)'].mean(),
            'avg_spending': cluster_data['Spending Score (1-100)'].mean(),
            'gender_dist': cluster_data['Gender'].value_counts().to_dict()
        }
        
        cluster_profiles[cluster] = profile
        
        print(f"\nCluster {cluster}:")
        print(f"  Size: {profile['size']} customers ({profile['percentage']:.1f}%)")
        print(f"  Avg Age: {profile['avg_age']:.1f} years")
        print(f"  Avg Income: ${profile['avg_income']:.1f}k")
        print(f"  Avg Spending Score: {profile['avg_spending']:.1f}/100")
        print(f"  Gender: {profile['gender_dist']}")
    
    return cluster_profiles


# ============================================
# 10. SAVE RESULTS
# ============================================
def save_results(df, cluster_profiles, optimal_k):
    """Save clustered data and summary report"""
    print("\n10. SAVING RESULTS")
    print("-" * 60)
    
    # Save clustered data
    df.to_csv(f'{OUTPUT_DIR}Clustered_Customers.csv', index=False)
    print("✓ Saved: Clustered_Customers.csv")
    
    # Save summary to text file
    with open(f'{OUTPUT_DIR}Cluster_Summary.txt', 'w') as f:
        f.write("="*60 + "\n")
        f.write("MALL CUSTOMERS CLUSTERING ANALYSIS - SUMMARY\n")
        f.write("="*60 + "\n\n")
        
        f.write(f"Optimal Number of Clusters: {optimal_k}\n")
        f.write(f"Total Customers: {len(df)}\n\n")
        
        f.write("CLUSTER PROFILES:\n")
        f.write("-"*60 + "\n")
        
        for cluster, profile in cluster_profiles.items():
            f.write(f"\nCluster {cluster}:\n")
            f.write(f"  Size: {profile['size']} customers ({profile['percentage']:.1f}%)\n")
            f.write(f"  Average Age: {profile['avg_age']:.1f} years\n")
            f.write(f"  Average Annual Income: ${profile['avg_income']:.1f}k\n")
            f.write(f"  Average Spending Score: {profile['avg_spending']:.1f}/100\n")
            f.write(f"  Gender Distribution: {profile['gender_dist']}\n")
    
    print("✓ Saved: Cluster_Summary.txt")


# ============================================
# 11. MAIN EXECUTION
# ============================================
def main():
    """Main execution function"""
    
    # Load and explore data
    df = load_and_explore_data(INPUT_FILE)
    
    # Clean data
    df = clean_data(df)
    
    # Prepare features
    X, X_scaled, scaler, features = prepare_features(df)
    
    # Find optimal clusters
    inertias, silhouette_scores, k_range = find_optimal_clusters(X_scaled)
    
    # Plot optimization
    plot_optimization(k_range, inertias, silhouette_scores)
    
    # Perform clustering
    kmeans, cluster_labels = perform_clustering(X_scaled, OPTIMAL_K)
    df['Cluster'] = cluster_labels
    
    print(f"\nCluster distribution:")
    print(df['Cluster'].value_counts().sort_index())
    
    # Create visualizations
    plot_clusters_2d(df, scaler, kmeans, OPTIMAL_K)
    
    # Analyze clusters
    cluster_profiles = analyze_clusters(df, OPTIMAL_K)
    
    # Save results
    save_results(df, cluster_profiles, OPTIMAL_K)
    
    # Final message
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE!")
    print("="*60)
    print("\nGenerated files:")
    print("  1. 01_Cluster_Optimization.png - Elbow & Silhouette Analysis")
    print("  2. 02_Cluster_Visualizations.png - 2D Cluster Plots")
    print("  3. Clustered_Customers.csv - Data with Cluster Labels")
    print("  4. Cluster_Summary.txt - Detailed Summary Report")


if __name__ == "__main__":
    main()
