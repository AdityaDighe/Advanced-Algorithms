stack = []
list = [8,6,7,5,2,6,7,1]
total = 0

for i in range(len(list)):
    if(list[i]<=len(stack)):
        for j in range(list[i]):
            stack.pop()
        stack.append(list[i])

        print(stack)
        print("Cost = ",list[i]+1)
        total+=list[i]+1

    else:
        stack.append(list[i])
        print(stack)
        print("Cost = 1")
        total+=1


print("Total Cost = ", total)
print("Ammortized Cost = ", total/len(list))
