import random

def deck_shuffling(shuffle):
    for i in range(1, len(shuffle)):
        shuffling = int(random.random() * i)
        temporary_shuffle = shuffle[i]
        shuffle[i] = shuffle[shuffling]
        shuffle[shuffling] = temporary_shuffle
    return shuffle

def main():
    card_deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print deck_shuffling(card_deck)
    
main()
