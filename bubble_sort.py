def bubble_sort(provided_list):
    list_length = len(provided_list)

    while list_length != 0:
        for i in range(len(provided_list) - 1):
            if provided_list[i] > provided_list[i + 1]:

                provided_list[i], provided_list[i + 1] = provided_list[i + 1], provided_list[i]
                print provided_list

        list_length = list_length - 1

def main():
    provided_list = [4, 6, 7, 1, 5, 3, 0, 2]
    print 'Sorting step by step:'
    bubble_sort(provided_list)

main()
