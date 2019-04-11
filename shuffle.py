import random

def num_shuffling(shuffle):
    for index in range(1, len(shuffle)):
        shuffling = int(random.random() * index)
        temporary_shuffle = shuffle[index]
        shuffle[index] = shuffle[shuffling]
        shuffle[shuffling] = temporary_shuffle
    return shuffle

def main():
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(num_shuffling(num_list))
    
main()
