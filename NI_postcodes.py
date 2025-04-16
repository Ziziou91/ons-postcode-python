import csv

input_file = 'ONSPD_FEB_2024_UK_BT.csv'
output_file = 'unique_ni_codes.csv'


pcds_values = []

with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
     open(output_file, mode='w', newline='', encoding='utf-8') as outfile:   
     
    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)

    writer.writerow(['outward_code'])

    prev_value = None


    for row in reader:
        full_value = row['pcds']
        before_space = full_value.split(' ')[0] 

        if before_space != prev_value:
            writer.writerow([before_space])
            prev_value = before_space

