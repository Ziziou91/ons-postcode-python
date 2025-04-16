import csv

# Replace with your actual file path
csv_file = 'ONSPD_FEB_2024_UK_BT.csv'

# Create a list to store the values from the 'pcds' column
pcds_values = []

with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Access the value under the 'pcds' column
        pcds_values.append(row['pcds'])

# Print all values
print(pcds_values)
