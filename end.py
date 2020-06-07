cnt = int(input())
dop = []
for i in range(cnt):
    dop.append(input())
    dop[i] = dop[i][9:]
    dop[i] = dop[i].replace(',', '')
    dop[i] = dop[i].replace('\'', '')
    dop[i] = dop[i].replace(')', '')
    dop[i] = dop[i].replace('(', '')
    dop[i] = dop[i].replace('[', '')
    dop[i] = dop[i].replace(']', '')
print("\n".join(dop))