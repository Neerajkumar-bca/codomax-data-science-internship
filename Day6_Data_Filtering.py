import pandas as pd

# Sample Dataset
data = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Karan', 'Pooja'],
    'Age': [22, 25, 28, 24, 30, 27],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Pune', 'Mumbai', 'Delhi'],
    'Salary': [30000, 45000, 50000, 35000, 60000, 48000]
}
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Task 1: Filter rows - Age > 25
filtered_df = df[df['Age'] > 25]
print("\nFiltered Data - Age > 25:")
print(filtered_df)

# Task 2: Select columns
selected_cols = df[['Name', 'Salary', 'City']]
print("\nSelected Columns:")
print(selected_cols)

# Task 3: Sort dataset by Salary
sorted_df = df.sort_values(by='Salary', ascending=False)
print("\nSorted by Salary:")
print(sorted_df)