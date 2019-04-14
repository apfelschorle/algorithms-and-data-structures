def partition(unsorted_list, left, right):
    pivot = unsorted_list[left]
    leftMark = left + 1
    rightMark = right

    while True:
        while leftMark < right and unsorted_list[leftMark] < pivot:
            leftMark += 1
        while rightMark > left and unsorted_list[rightMark] > pivot:
            rightMark -= 1

        if leftMark >= rightMark:
            break

        else:
            unsorted_list[leftMark], unsorted_list[rightMark] = unsorted_list[rightMark], unsorted_list[leftMark]

    unsorted_list[left], unsorted_list[rightMark] = unsorted_list[rightMark], unsorted_list[left]
    return rightMark

def quickselect(unsorted_list, left, right, k):
    if left == right:
        return unsorted_list[left]

    split = partition(unsorted_list, left, right)
    length = split - left + 1
    if length == k:
        return unsorted_list[split]
    elif k < length:
        return quickselect(unsorted_list, left, split - 1, k)
    else:
        return quickselect(unsorted_list, split + 1, right, k - length)

def main():
    unsorted_list = [8, 9, 7, 6, 5, 4, 2, 3, 1]
    print(quickselect(unsorted_list, 0, len(unsorted_list)-1, 3))

main()
