import pandas as pd

data = pd.read_csv("the_data_scientist.csv")
jumlah = 0
for j in data:
    for i in data[j]:
        jumlah += i
    print(chr(int(jumlah//255)),end="")
    jumlah = 0