data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
    x = []
    with open(data1) as data:
        for line in data:
            x = line.split()
    return x

x = readData(data1)
txt = []
for i in x:
    if (i == 'and') or (i == "I") or (i == "The") or (i == "you"):
        txt.append("*"*len(i))
    else:
        txt.append(i)

txt = ' '.join(txt);
print txt
