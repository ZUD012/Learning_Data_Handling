import csv

# Understanding Manipulation of data -->

with open ("D:\ALL data\heart.csv" , "r") as file :
    reading  = csv.reader(file)
    header = next(reading)
    for row in reading :
        print(row) 


print()
print()

# Understanding Manipulation of data >-< 02 -->

with open ("D:\ALL data\heart.csv" , "r") as f :
    read = csv.DictReader(f)
    header  = next
    print("AGE" , "   CHOLESTROL")
    print()
    for rows in read :
        if int(rows["Age"])>50:
            print(rows["Age"],"  :  ",rows["Cholesterol"])
        
