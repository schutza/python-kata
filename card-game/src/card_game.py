from dataclasses import dataclass, field
from typing import List




SUITS = ['HEART', 'SPADE', 'DIAMOND', 'CLUB']
VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

@dataclass
class Card:
    value: int
    suit: str


def create_deck():
    cards = [Card(value, suit) for value in VALUES for suit in SUITS]
    return cards


@dataclass
class CardDeck:
    cards: List[Card] = field(default_factory=create_deck)

