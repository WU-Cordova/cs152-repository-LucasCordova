
# I made a change

from datastructures.bag import Bag
from projects.project1.card import Card, CardSuit, CardFace


def main():
    
    card_suits = [suit.value for suit in list(CardSuit)]

    cards = []

    for suit in list(CardSuit):
        for face in list(CardFace):

            cards.append(Card(suit.value, face.value))

    print(card_suits)



if __name__ == '__main__':
    main()
