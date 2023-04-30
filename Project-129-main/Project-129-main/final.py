import csv
import pandas as pd

file1 = 'data1_sorted.csv'
file2 = 'data2.csv'

dataset1 = []
dataset2 = []
with open("C:\Users\DELL\Documents\Project-129-main\Project-129-main\data1_sorted.csv",'r') as f:
    csv_reader =csv.reader(f)
    for i in csv_reader:
        dataset1.append(i)     
with open("C:\Users\DELL\Documents\Project-129-main\Project-129-main\data2.csv",'r') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        dataset2.append(i)
headers1 = dataset1[0]
headers2 = dataset2[0]
starsdataset1 = dataset1[1:]
starsdataset2 = dataset2[1:]
h = headers1+headers2
starsd =[]
for i in starsdataset1:
    starsd.append(i)
for j in starsdataset2:
    starsd.append(j)
with open("total_stars.csv",'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(starsd) 
df = pd.read_csv('total_stars.csv')