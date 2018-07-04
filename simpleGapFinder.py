myList = [0, 23, 10, 2, 3, 7, 5, 12, 15, 17]
myList.sort()

for number in range(len(myList) - 1):
    if myList[number] + 1 == myList[number + 1]:
        continue
    else:
        myList[number + 1] = myList[number] + 1

print(myList)
