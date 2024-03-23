import csv
new=['physics',98]
with open('sample.csv','a',newline='') as txt:
    string=csv.writer(txt)
    string.writerow(new)
print('changed')
txt.close()
