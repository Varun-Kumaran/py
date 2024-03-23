import csv
m1=['maths',97]
m2=['chemistry',96]
with open('sample.csv','r') as read:
    sample=csv.reader(read)
    data=list(sample)
    data[1]=m1
    data[2]=m2
with open('sample.csv','w',newline='') as write:
    change=csv.writer(write)
    change.writerows(data)
print('modified')
