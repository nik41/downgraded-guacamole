list = [4,2,3,6,5,7,4,3,1,1]

def maxDistance(list, num):
    sortedList = sorted(list)
    listLength = len(sortedList)
    sum = 0
    maxDis = 0

    for i in reversed(range(listLength)):
        sum+=sortedList[i]
        if sum > maxDis and sum<= num:
            maxDis = sum
    return maxDis

print(maxDistance(list,30))
print(maxDistance(list,4))
print(maxDistance(list,34))
print(maxDistance(list,17))