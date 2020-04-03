import random

def partition(sortlist, left, right, pivotIndex):
    pivotValue = sortlist[pivotIndex]
    sortlist[pivotIndex], sortlist[right] = sortlist[right], sortlist[pivotIndex]
    storeIndex = left

    for i in range(left, right):
        if sortlist[i] < pivotValue:
            sortlist[storeIndex], sortlist[i] = sortlist[i], sortlist[storeIndex]
            storeIndex += 1
    sortlist[right], sortlist[storeIndex] = sortlist[storeIndex], sortlist[right]
    return storeIndex

def select(sortlist, k):
    left = 0
    right = len(sortlist) - 1
    
    while True:
        if left == right:
            return sortlist[left]
        pivotIndex = random.randint(left, right)
        pivotIndex = partition(sortlist, left, right, pivotIndex)

        if k == pivotIndex:
            return sortlist[k]
        elif k < pivotIndex:
            right = pivotIndex - 1
        else:
            left = pivotIndex + 1

def main():
    sortlist = [8, 9, 7, 6, 5, 4, 2, 3, 1]
    print(select(sortlist, 8))

main()
