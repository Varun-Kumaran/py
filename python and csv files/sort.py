import csv,operator
with open('sample.csv','r') as txt:
    string=csv.reader(txt)
    next(string)
    sortedreport=sorted(string,key=operator.itemgetter(0))
print(sortedreport)
