import csv

dataset_1 = []
dataset_2 = []

# dataset_1 = final.csv
with open("final.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_1.append(row)

# dataset_2 = archive_dataset_sorted1.csv
with open("archive_dataset_sorted1.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_2.append(row)

# splitting both datasets
headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]
headers_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

# merging the headers
headers = headers_1 + headers_2

# merging the data rows
planet_data = []
for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index] + planet_data_2[index])

with open("merged_dataset.csv", "w", newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)