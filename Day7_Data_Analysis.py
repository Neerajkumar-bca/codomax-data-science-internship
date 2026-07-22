import pandas as pd

df = pd.DataFrame({
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Karan', 'Pooja'],
    'Age': [22, 25, 28, 24, 30, 27],
    'Salary': [30000, 45000, 50000, 35000, 60000, 48000],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'IT', 'HR']
})

# Task: Calculate metrics
print("Total Salary:", df['Salary'].sum())
print("Average Salary:", df['Salary'].mean())
print("Minimum Salary:", df['Salary'].min())
print("Maximum Salary:", df['Salary'].max())
print("Total Employees:", df['Name'].count())

# Business Insight
print("\nAverage Salary by Department:")
print(df.groupby('Department')['Salary'].mean())

print("\nEmployee Count by Department:")
print(df['Department'].value_counts())