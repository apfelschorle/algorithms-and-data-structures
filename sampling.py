import random

def sampling(original_list, sampling_num):
    sampling_list = []
    for i in range(sampling_num):
        sampling_list.append(original_list[i])

    for j in range(sampling_num, len(original_list)):
        index = int(j * random.random())

        if index < sampling_num:
            sampling_list[index] = original_list[j]
    return sampling_list       

def main():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(original_list)
    print(sampling(original_list, 4))

main()
