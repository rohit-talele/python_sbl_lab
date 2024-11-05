import pandas as pd

# Simple Data Series
data_series = input("Enter a list of values for the Data Series (comma separated): ").split(',')
data_series = [int(item.strip()) for item in data_series]  # Convert input to integers
series = pd.Series(data_series)

print("\nData Series:")
print(series)

# Simple DataFrame
rows = int(input("\nEnter number of rows for the DataFrame: "))
columns = int(input("Enter number of columns for the DataFrame: "))

data_frame = []
for i in range(rows):
    row = []
    for j in range(columns):
        value = input(f"Enter value for row {i+1}, column {j+1}: ")
        row.append(value)
    data_frame.append(row)

df = pd.DataFrame(data_frame)
print("\nDataFrame:")
print(df)
