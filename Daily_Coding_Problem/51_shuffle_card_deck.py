# Given a function that generates perfectly random numbers between 1 and k (inclusive), 
# where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

# It should run in O(N) time.

import random

def generateRandom(k):
    return random.randint(0, k)


def shuffleDeck(deck):
    for i in range(51, 0, -1):
        rand = generateRandom(i)
        deck[i], deck[rand] = deck[rand], deck[i]


def printDeck():
    print(*deck)


deck = [i for i in range(1, 53)]
shuffleDeck(deck)
printDeck()