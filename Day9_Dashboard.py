import pandas as pd
import matplotlib.pyplot as plt

print("=== MINI DASHBOARD ===")
df = pd.read_csv('data.csv') # ya upar wala data use karo

# Section 1: Data Overview
print("\n1. Dataset Info:")
print(df.head())

# Section 2: Key Metrics
print("\n2. Key Metrics:")
print("Total Employees:", df['Name'].count())
print("Average Salary:", df['Salary'].mean())

# Section 3: Charts
plt.subplot(1,2,1)
df['Department'].value_counts().plot(kind='bar', color='orange')
plt.title("Employees by Department")

plt.subplot(1,2,2)
plt.pie(df['Department'].value_counts(), labels=df['Department'].value_counts().index, autopct='%1.1f%%')
plt.title("Department %")
plt.show()

print("\nDashboard Completed!")