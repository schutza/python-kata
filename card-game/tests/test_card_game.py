from card_game import CardDeck, Player, CardGame

class TestCardGame:
    def test_create_deck(self):
        # given
        expected_deck_size = 52
        # when
        actual_deck = CardDeck()
        # then
        assert expected_deck_size == len(actual_deck.cards)

    def test_deal(self):
        # given
        players = [Player(str(i)) for i in range(0, 3)]
        game = CardGame(players)
        # when
        game.deal()
        # then
        assert players[0].hand_size() == players[1].hand_size() == players[2].hand_size()
