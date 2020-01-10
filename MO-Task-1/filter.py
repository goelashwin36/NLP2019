# The corpus created had a bunch of english words. Those were remove using this python script.
import csv

newFile = open('Hindi.csv', mode='w')

fileWriter = csv.writer(newFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

with open('TempCorpus.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        try:
            if(not(97<=ord(row[0][0])<97+26)):
                fileWriter.writerow([row[0], row[1]])
        except(IndexError):
            pass
print("Done")
