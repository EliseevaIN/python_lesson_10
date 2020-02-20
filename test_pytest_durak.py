import pytest
from durak import Durak

class TestDurak:

    def setup(self):
        self.cards_game = Durak(25)
        print("start test")

    def teardown(self):
        print("test passed")

    def test_init(self):
        assert self.cards_game.order_num == 25

    def test_all_cards(self):
        cards_game = Durak(25)
        cards_game.all_cards()
        assert len(cards_game.player_1_cards) == 6
        assert len(cards_game.player_2_cards) == 6
        assert len(cards_game.deck) == 24

    def test_bito(self):
        cards_game = Durak(25)
        cards_game.all_cards()
        cards_game.order_cards()
        assert len(cards_game.list_bito) + len(cards_game.player_1_cards) + len(cards_game.player_2_cards) == 36
        assert len(cards_game.deck) == 0

    def test_dobor(self):
        cards_game = Durak(1)
        cards_game.all_cards()
        cards_game.order_cards()
        assert len(cards_game.player_1_cards) >= 6
        assert len(cards_game.player_2_cards) >= 6