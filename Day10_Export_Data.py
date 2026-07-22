import pandas as pd

df = pd.DataFrame({
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Karan', 'Pooja'],
    'Age': [22, 25, 28, 24, 30, 27],
    'Salary': [30000, 45000, 50000, 35000, 60000, 48000]
})

# Clean the data - remove duplicates, sort
cleaned_df = df.sort_values(by='Salary', ascending=False)

# Export to CSV
cleaned_df.to_csv('cleaned_dataset.csv', index=False)
print("Cleaned dataset exported successfully!")
print(cleaned_df)