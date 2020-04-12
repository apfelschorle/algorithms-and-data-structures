def countingSort(array):
    count = [0]*(len(array)+1)
    for x in array:
        count[x] += 1

    total = 0
    for i, j in enumerate(count):
        count[i], total = total, j + total

    output = [0]*len(array)
    for x in array:
        output[count[x]] = x
        count[x] += 1

    return output

def main():
    array = [9, 1, 2, 8, 3, 7, 5, 4, 6, 1, 2, 3, 5]
    print(array)
    print(countingSort(array))

main()
