import csv
report=[['subject','mark'],['maths',36],['chemistry',22]]
with open('sample.csv','w',newline='') as txt:
    string=csv.writer(txt)
    string.writerows(report)
print('written')
txt.close
        
