def merge_sort(unsorted_list):

    if len(unsorted_list) == 1:
        return unsorted_list
    elif len(unsorted_list) == 2:
        if unsorted_list[0] > unsorted_list[1]:
            unsorted_list[0], unsorted_list[1] = unsorted_list[1], unsorted_list[0]
        return unsorted_list
    else:

        if len(unsorted_list) %2 != 0:
            unsorted_list_left_side = unsorted_list[0:len(unsorted_list)/2 + 1]
            unsorted_list_right_side = unsorted_list[(len(unsorted_list) - len(unsorted_list_left_side) + 1):len(unsorted_list)]
        else:
            unsorted_list_left_side = unsorted_list[0:len(unsorted_list)/2]
            unsorted_list_right_side = unsorted_list[(len(unsorted_list) - len(unsorted_list_left_side)):len(unsorted_list)]

        sorted_sublist_left_side = merge_sort(unsorted_list_left_side)
        sorted_sublist_right_side = merge_sort(unsorted_list_right_side)

        sorted_list = len(sorted_sublist_left_side + sorted_sublist_right_side) * [0]

        left_list_counter = 0
        right_list_counter = 0
        for i in range(len(sorted_list)):

            if left_list_counter < len(sorted_sublist_left_side) and right_list_counter < len(sorted_sublist_right_side):
                if sorted_sublist_left_side[left_list_counter] > sorted_sublist_right_side[right_list_counter]:
                    sorted_list[i] = sorted_sublist_right_side[right_list_counter]
                    right_list_counter += 1
                else:
                    sorted_list[i] = sorted_sublist_left_side[left_list_counter]
                    left_list_counter += 1
            else:
                if left_list_counter >= len(sorted_sublist_left_side):
                    sorted_list[i] = sorted_sublist_right_side[right_list_counter]
                    right_list_counter += 1
                else:
                    sorted_list[i] = sorted_sublist_left_side[left_list_counter]
                    left_list_counter += 1
        return sorted_list

def main():
    unsorted_list = [8, 6, 7, 5, 3, 0, 9, 2, 4, 1]
    print 'Unsorted list', unsorted_list
    print 'Sorted list', merge_sort(unsorted_list)

main()
def merge_sort(unsorted_list):

    if len(unsorted_list) == 1:
        return unsorted_list
    elif len(unsorted_list) == 2:
        if unsorted_list[0] > unsorted_list[1]:
            unsorted_list[0], unsorted_list[1] = unsorted_list[1], unsorted_list[0]
        return unsorted_list
    else:

        if len(unsorted_list) %2 != 0:
            unsorted_list_left_side = unsorted_list[0:len(unsorted_list)//2 + 1]
            unsorted_list_right_side = unsorted_list[(len(unsorted_list) - len(unsorted_list_left_side) + 1):len(unsorted_list)]
        else:
            unsorted_list_left_side = unsorted_list[0:len(unsorted_list)//2]
            unsorted_list_right_side = unsorted_list[(len(unsorted_list) - len(unsorted_list_left_side)):len(unsorted_list)]

        sorted_sublist_left_side = merge_sort(unsorted_list_left_side)
        sorted_sublist_right_side = merge_sort(unsorted_list_right_side)

        sorted_list = len(sorted_sublist_left_side + sorted_sublist_right_side) * [0]

        left_list_counter = 0
        right_list_counter = 0
        for i in range(len(sorted_list)):

            if left_list_counter < len(sorted_sublist_left_side) and right_list_counter < len(sorted_sublist_right_side):
                if sorted_sublist_left_side[left_list_counter] > sorted_sublist_right_side[right_list_counter]:
                    sorted_list[i] = sorted_sublist_right_side[right_list_counter]
                    right_list_counter += 1
                else:
                    sorted_list[i] = sorted_sublist_left_side[left_list_counter]
                    left_list_counter += 1
            else:
                if left_list_counter >= len(sorted_sublist_left_side):
                    sorted_list[i] = sorted_sublist_right_side[right_list_counter]
                    right_list_counter += 1
                else:
                    sorted_list[i] = sorted_sublist_left_side[left_list_counter]
                    left_list_counter += 1
        return sorted_list

def main():
    unsorted_list = [8, 6, 7, 5, 3, 0, 9, 2, 4, 1]
    print('Unsorted list', unsorted_list)
    print('Sorted list', merge_sort(unsorted_list))

main()
