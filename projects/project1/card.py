

from dataclasses import dataclass
from enum import Enum


class CardSuit(Enum):
    HEARTS = "❤️"
    SPADE = "♠️"
    CLUBS = "♣️"
    DIAMONDS = "♦️"

class CardFace(Enum):
    ONE = "1"
    TWO = "2"
    JACK = "10"
    QUEEN = "10"
    KING = "10"
    ACE = "11"

@dataclass
class Card:
    card_face: CardFace
    card_suit: CardSuit
