import csv
import math

with open("data.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    
print(data)
new_data = data[0]
print(new_data)

def mean():
    n = len(new_data)
    total = 0
    
    for i in new_data:
        total = total+int(i)
        
    mean = total/n
  
    return mean

square_list = []
for i in new_data:
    difference = int(i)-mean()
    square = difference**2
    square_list.append(square)
    
sum = 0

for i in square_list:
    sum = sum+i
    
result = sum/(len(new_data)-1)

standard_deviation = math.sqrt(result)

print(standard_deviation)
 
