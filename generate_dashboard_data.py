
import csv
import json

customers = []

# Read original customer information
with open("customers.csv", "r") as file:
    original_data = {
        int(row["CustomerID"]): row
        for row in csv.DictReader(file)
    }

# Read actual K-Means results
with open("kmeans_results.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        customer_id = int(row["CustomerID"])
        original = original_data[customer_id]
        cluster = int(row["Cluster"])

        if cluster == 0:
            segment = "Medium Income - High Spending"
        elif cluster == 1:
            segment = "High Income - Low Spending"
        else:
            segment = "Low Income - High Spending"

        customers.append({
            "CustomerID": customer_id,
            "Age": int(original["Age"]),
            "AnnualIncome": int(row["AnnualIncome"]),
            "SpendingScore": int(row["SpendingScore"]),
            "Cluster": cluster,
            "Customer_Segment": segment
        })

total = len(customers)

dashboard_data = {
    "customers": customers,
    "summary": {
        "total_customers": total,
        "average_age": round(sum(c["Age"] for c in customers) / total, 1),
        "average_income": round(sum(c["AnnualIncome"] for c in customers) / total, 2),
        "average_spending": round(sum(c["SpendingScore"] for c in customers) / total, 1)
    }
}

with open("dashboard_data.json", "w") as file:
    json.dump(dashboard_data, file, indent=4)

print("K-Means dashboard data updated successfully!")
print("Total customers:", total)
print("Average age:", dashboard_data["summary"]["average_age"])
print("Average income:", dashboard_data["summary"]["average_income"])
print("Average spending:", dashboard_data["summary"]["average_spending"])
