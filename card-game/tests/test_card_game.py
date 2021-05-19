from card_game import CardDeck

class TestCardGame:
    def test_create_deck(self):
        # given
        expected_deck_size = 52
        # when
        actual_deck = CardDeck()
        # then
        assert expected_deck_size == len(actual_deck.cards)

