import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Karan', 'Pooja'],
    'Age': [22, 25, 28, 24, 30, 27],
    'Salary': [30000, 45000, 50000, 35000, 60000, 48000],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'IT', 'HR']
})

# 1. Bar Chart
plt.figure(figsize=(8,5))
plt.bar(df['Name'], df['Salary'], color='skyblue')
plt.title("Salary by Employee")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.xticks(rotation=45)
plt.show()

# 2. Line Chart
plt.figure(figsize=(8,5))
plt.plot(df['Age'], df['Salary'], marker='o', color='green')
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

# 3. Pie Chart
dept_count = df['Department'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(dept_count, labels=dept_count.index, autopct='%1.1f%%')
plt.title("Department Distribution")
plt.show()