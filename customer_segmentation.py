import csv

customers = []

with open("customers.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        customer = {
            "CustomerID": int(row["CustomerID"]),
            "Age": int(row["Age"]),
            "AnnualIncome": int(row["AnnualIncome"]),
            "SpendingScore": int(row["SpendingScore"])
        }

        customers.append(customer)

print("CUSTOMER DATA")
print("-" * 50)

for customer in customers:
    print(customer)

print("\nDATA TYPE CHECK")
print(type(customers[0]["AnnualIncome"]))
# Customer Data Analysis

total_customers = len(customers)

total_age = sum(c["Age"] for c in customers)
total_income = sum(c["AnnualIncome"] for c in customers)
total_score = sum(c["SpendingScore"] for c in customers)

average_age = total_age / total_customers
average_income = total_income / total_customers
average_score = total_score / total_customers

print("\nCUSTOMER DATA ANALYSIS")
print("------------------------------")

print("Total Customers:", total_customers)
print("Average Age:", average_age)
print("Average Annual Income:", average_income)
print("Average Spending Score:", average_score)
# Find highest and lowest spending customers

highest = max(customers, key=lambda c: c["SpendingScore"])
lowest = min(customers, key=lambda c: c["SpendingScore"])

print("\nCUSTOMER SPENDING INSIGHTS")
print("------------------------------")

print("Highest Spending Customer:")
print(highest)

print("\nLowest Spending Customer:")
print(lowest)# Find highest and lowest income customers

highest_income = max(customers, key=lambda c: c["AnnualIncome"])
lowest_income = min(customers, key=lambda c: c["AnnualIncome"])

print("\nCUSTOMER INCOME INSIGHTS")
print("------------------------------")

print("Highest Income Customer:", highest_income)
print("Lowest Income Customer:", lowest_income)# Create customer spending chart using HTML

html = """
<html>
<head>
<title>Customer Spending Analysis</title>
<style>
body { font-family: Arial; padding: 20px; }
.bar { background: steelblue; color: white; padding: 8px;
       margin: 10px; }
</style>
</head>
<body>
<h2>Customer Spending Analysis</h2>
"""

for customer in customers:
    score = customer["SpendingScore"]
    html += f"""
    <p>Customer {customer['CustomerID']} - {score}</p>
    <div class="bar" style="width:{score}%">{score}</div>
    """

html += "</body></html>"

with open("customer_chart.html", "w") as file:
    file.write(html)

print("\nCustomer chart created successfully!")# Prepare customer information for segmentation

print("\nCUSTOMER SEGMENTATION DATA")
print("--------------------------------")

for customer in customers:
    print(
        "Customer:", customer["CustomerID"],
        "| Income:", customer["AnnualIncome"],
        "| Spending:", customer["SpendingScore"]
    )# Prepare data for K-Means clustering

X = []

for customer in customers:
    X.append([
        customer["AnnualIncome"],
        customer["SpendingScore"]
    ])

print("\nDATA PREPARED FOR K-MEANS")
print(X)
# K-Means configuration

number_of_clusters = 3

print("\nK-MEANS CONFIGURATION")
print("Number of clusters:", number_of_clusters)
print("Input features: Annual Income and Spending Score")# Feature Scaling using Min-Max Scaling

incomes = [c["AnnualIncome"] for c in customers]
scores = [c["SpendingScore"] for c in customers]

min_income = min(incomes)
max_income = max(incomes)

min_score = min(scores)
max_score = max(scores)

scaled_data = []

for customer in customers:
    scaled_income = (
        (customer["AnnualIncome"] - min_income) /
        (max_income - min_income)
    )

    scaled_score = (
        (customer["SpendingScore"] - min_score) /
        (max_score - min_score)
    )

    scaled_data.append([scaled_income, scaled_score])

print("\nSCALED CUSTOMER DATA")
print(scaled_data)# Display customer groups using simple business rules

print("\nCUSTOMER GROUP ANALYSIS")
print("------------------------------")

for customer in customers:

    income = customer["AnnualIncome"]
    spending = customer["SpendingScore"]

    if income >= 50000 and spending >= 60:
        group = "High Income - High Spending"

    elif income >= 50000 and spending < 60:
        group = "High Income - Low Spending"

    else:
        group = "Low Income - High Spending"

    print("Customer:", customer["CustomerID"], "| Group:", group)# Count customers in each group

group_count = {}

for customer in customers:

    income = customer["AnnualIncome"]
    spending = customer["SpendingScore"]

    if income >= 50000 and spending >= 60:
        group = "High Income - High Spending"

    elif income >= 50000 and spending < 60:
        group = "High Income - Low Spending"

    else:
        group = "Low Income - High Spending"

    group_count[group] = group_count.get(group, 0) + 1

print("\nCUSTOMER GROUP SUMMARY")
print("------------------------------")

for group, count in group_count.items():
    print(group, ":", count, "customers")# Create customer group chart using HTML

html = """
<html>
<head>
<title>Customer Segmentation Chart</title>
<style>
body {
    font-family: Arial;
    padding: 20px;
}
.bar {
    background: steelblue;
    color: white;
    padding: 12px;
    margin: 15px 0;
}
</style>
</head>
<body>

<h2>Customer Segmentation Analysis</h2>
"""

for group, count in group_count.items():
    width = count * 100

    html += f"""
    <p>{group}: {count} customers</p>
    <div class="bar" style="width:{width}px">
        {count} customers
    </div>
    """

html += """
</body>
</html>
"""

with open("customer_group_chart.html", "w") as file:
    file.write(html)

print("\nCustomer group chart created successfully!")# Generate Customer Segmentation Report

report = """
CUSTOMER SEGMENTATION PROJECT
================================

PROJECT SUMMARY

Total Customers: 5
Average Age: 30.6
Average Annual Income: 45000
Average Spending Score: 65

CUSTOMER GROUPS

Low Income - High Spending: 3 customers

High Income - Low Spending: 2 customers

KEY INSIGHTS

1. Most customers belong to the Low Income - High Spending group.
2. Two customers have high income and low spending.
3. Customer 3 has the highest spending score.
4. Customer 4 has the highest annual income.

CONCLUSION

Customer segmentation helps businesses understand
customer behavior and plan targeted marketing strategies.
"""

with open("customer_segmentation_report.txt", "w") as file:
    file.write(report)

print("\nCustomer segmentation report created successfully!")