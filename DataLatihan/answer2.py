data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
    x = []
    with open(data1) as data:
        for line in data:
            x = line.split()
    return x

x = readData(data1)
z = readData(data2)
txt = []
if len(x) > len(z):
    for item in x:
        j = z.count(item)
        if j > 0:
            txt.append(item)
else:
    for item in z:
        j = x.count(item)
        if j > 0:
            txt.append(item);
txt = set(txt)
print txt
            #set()
