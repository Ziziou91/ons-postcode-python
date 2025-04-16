import csv

csv_file = 'ONSPD_FEB_2024_UK_BT.csv'

pcds_values = []

with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        full_value = row['pcds']
        before_space = full_value.split(' ')[0] 

        if not pcds_values or before_space != pcds_values[-1]:
            pcds_values.append(before_space)

print(pcds_values)
