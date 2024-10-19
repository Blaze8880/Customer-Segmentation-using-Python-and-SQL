from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Select features for clustering
X = df[['total_purchases', 'total_spent']]

# Apply KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Plot the customer segments
plt.scatter(df['total_purchases'], df['total_spent'], c=df['Cluster'], cmap='viridis')
plt.title('Customer Segmentation based on Purchases')
plt.xlabel('Total Purchases')
plt.ylabel('Total Spent')
plt.show()
