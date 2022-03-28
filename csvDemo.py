import csv

with open('utilities/car-sales-extended-missing-data.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    # print(csvReader)
    # print(list(csvReader))

    Brand = []
    color = []
    for row in csvReader:
        Brand.append(row[0])
        color.append(row[1])
print(Brand)
print(color)

Index = Brand.index('BMW')
color_status = color[Index]
print(" color i s " + color_status)

with open('utilities/car-sales-extended-missing-data.csv', 'a') as wFile:
    write = csv.writer(wFile)
    write.writerow(['Bentley', 'Beige'])
