listA = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
listB = [1, 2, 3, 5, -10, 4]
listC = [3, 5, -7, 8, 1, -9, 4]
listD = [7, 9, 12, -33, -4, 5, 6]
listE = [4, 5, 8, 9, 10, 11, -40, 55]

def maxSequence(aList):
    aListLength = len(aList)
    subSequenceSum = 0

    subSequence = max((aList[i:j] for i in range(aListLength + 1) for j in range(i, aListLength + 1)), key = sum)

    for k in range(len(subSequence)):
        subSequenceSum += subSequence[k]


    return str(subSequenceSum) +": "+"["+", ".join(str(item) for item in subSequence)+"]"

print(maxSequence(listA))
print(maxSequence(listB))
print(maxSequence(listC))
print(maxSequence(listD))
print(maxSequence(listE))
