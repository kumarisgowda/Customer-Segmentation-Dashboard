
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# Step 1: Load customer dataset
data = pd.read_csv("customers.csv")

# Step 2: Select features
X = data[["AnnualIncome", "SpendingScore"]]

# Step 3: Scale the data
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Create K-Means model
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Step 5: Train the model
data["Cluster"] = kmeans.fit_predict(X_scaled)

# Step 6: Display customer clusters
print("\nCustomer Segmentation Results")
print(data[["CustomerID", "AnnualIncome",
            "SpendingScore", "Cluster"]])

# Step 7: Display cluster centers
print("\nCluster Centers:")
print(kmeans.cluster_centers_)

# Step 8: Save results
data.to_csv("kmeans_results.csv", index=False)

print("\nK-Means clustering completed!")
print("Results saved in kmeans_results.csv")
