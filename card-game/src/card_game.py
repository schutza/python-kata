from dataclasses import dataclass, field
from typing import List
import random


@dataclass
class Card:
    value: int
    suit: str


def create_deck():
    suits = ['HEART', 'SPADE', 'DIAMOND', 'CLUB']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    cards = [Card(value, suit) for value in values for suit in suits]
    return cards


@dataclass
class CardDeck:
    cards: List[Card] = field(default_factory=create_deck)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand: List[Card] = []

    def init_hand(self, cards: List[Card]):
        self.hand = cards

    def hand_size(self) -> int:
        return len(self.hand)


class CardGame:
    def __init__(self, players: List[Player], rules = None):
        self.card_deck = CardDeck()
        self.players = players
        self.rules = rules

    def deal(self):
        # this is rule-specific, for now assume everyone gets same amount of cards
        # will have to delegate to Rules
        [
            player.init_hand(self._cards_for_player())
            for player in self.players
        ]

    def _cards_for_player(self):
        num_players = len(self.players)
        total_cards = len(self.card_deck.cards)
        num_cards_for_player = int(total_cards / num_players)
        return random.choices(self.card_deck.cards, k=num_cards_for_player)


class Rules:
    pass


if __name__ == '__main__':
    players = [Player(str(i)) for i in range(0,3)]
    game = CardGame(players)

    game.deal()
    print('AFTER DEALING')
    for player in players:
        print(f'Player {player.name} Hand size: {player.hand_size()}')
        print(f'{player.hand}')
