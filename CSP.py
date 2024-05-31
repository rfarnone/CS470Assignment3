import pandas
import csv
csvFile = pandas.read_csv('CSPData.csv')
print(csvFile)


with open('CSPData.csv', mode ='r')as file:
    csvFile2 = csv.reader(file)
    for lines in csvFile2:
        print(lines)
