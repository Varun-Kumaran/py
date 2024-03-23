import csv
data=[['date','subject'],['1','french'],['5','english']]
with open('S1.csv', 'w')as w:
    writer=csv.writer(w)
    writer.writerows(data)
w.close
