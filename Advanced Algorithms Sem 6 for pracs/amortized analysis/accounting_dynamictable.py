list = [8,6,7,5,2,6,7,1,2,3,2,2,2,2,2,2,2,2,2,2]
table = []
maxlen = 0
c = 3
bank = 0
cost = 0


table.append(list[0])
maxlen = 1
cost = 1
bank += c - cost
print("Table size: ",maxlen ," Actual Cost: ",cost," Bank: ", bank)
for i in range(1,len(list)):
    if(maxlen>len(table)):
        cost = 1
        bank += c - cost
        table.append(list[i])

    else:
        maxlen = maxlen*2
        cost = len(table)+1
        bank += c - cost
        table.append(list[i])

    print("Table size: ",maxlen ," Actual Cost: ",cost," Bank: ", bank)
