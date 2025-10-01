import csv

rows = [
    ["Name", "Age", "City"],  # header
    ["Parth", 18, "Mumbai"],
    ["Zudo", 20, "Delhi"],
    ["Alex", 22, "Bangalore"]
]

with open("D:\ALL data\self.csv" , "w" , newline="") as file :
    write  = csv.writer(file)
    write.writerows(rows)

with open("D:\ALL data\self.csv" , "r") as file :
    read  = csv.reader(file)
    header = next(read)
    print(header)
    for i in read :
        print(i)


