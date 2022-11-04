file = open('data.dat', 'r') 
lines = file.readlines() 
count = 0

for line in lines: 
    c0 = 0
    c1 = 0
  
    for i in line: 
        if i == '0': 
            c0 = c0 + 1
        if i == '1':
            c1 = c1 + 1
    
    if (c0 % 3 == 0 or c1 % 2 == 0):
      count = count + 1

print(count)