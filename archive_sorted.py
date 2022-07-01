import csv

data = []

with open("archive_dataset.csv", "r") as f:
    csvreader = csv.reader(f) # this variable contains all the data from the csv file
    for row in csvreader:
        data.append(row) # each row is a different element in the data array

headers = data[0] # the top row in the data array has the headers
planet_data = data[1:] # the data excluding the headers

# converting all planet names (pl_name) to lowercase
for data_point in planet_data:
    data_point[2] = data_point[2].lower()

# sorting planet names into alphabetical order
planet_data.sort(key=lambda planet_data:planet_data[2])

# creating a new sorted csv file
with open("archive_dataset_sorted.csv", "w") as f: # opening in write mode
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

# removing the blank lines in the sorted csv
# opening the sorted csv in read mode and creating a dulicate version called archive_dataset_sorted1.csv
with open("archive_dataset_sorted.csv", "r") as input, open('archive_dataset_sorted1.csv', "w", newline='') as output: # newline
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row): # if there is a blank row, strip the blank parts
            writer.writerow(row)