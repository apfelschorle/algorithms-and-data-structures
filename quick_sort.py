def quick_sort(unsorted_list):

    if len(unsorted_list) <= 1:
        return unsorted_list

    pivot_index = 0

    compare_index = len(unsorted_list) - 1
    while pivot_index != compare_index:

        if unsorted_list[compare_index] < unsorted_list[pivot_index]:
            unsorted_list[compare_index], unsorted_list[pivot_index + 1] = unsorted_list[pivot_index + 1], unsorted_list[compare_index]
            unsorted_list[pivot_index], unsorted_list[pivot_index + 1] = unsorted_list[pivot_index + 1], unsorted_list[pivot_index]
            pivot_index += 1
        else:
            compare_index -= 1

    sub_left_list = unsorted_list[0:pivot_index]
    sub_right_list = unsorted_list[pivot_index + 1:len(unsorted_list)]
    
    sorted_sub_left_list = quick_sort(sub_left_list)
    sorted_sub_right_list = quick_sort(sub_right_list)

    sorted_list = sorted_sub_left_list + [unsorted_list[pivot_index]] + sorted_sub_right_list
    return sorted_list

def main():
    unsorted_list = [8, 6, 7, 5, 3, 0, 9, 4, 1, 2]
    print(quick_sort(unsorted_list))

main()
