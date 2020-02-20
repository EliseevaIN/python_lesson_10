import unittest
from durak import Durak


class TestDurak_unittest(unittest.TestCase):

    def setUp(self):
        self.cards_game = Durak(25)
        print('start test')

    def tearDown(self):
        print('test passed')

    def test_all_cards(self):
        cards_game = Durak(25)
        cards_game.all_cards()
        self.assertEqual(len(cards_game.player_1_cards), 6)
        self.assertEqual(len(cards_game.player_2_cards), 6)
        self.assertEqual(len(cards_game.deck), 24)

    def test_bito(self):
        cards_game = Durak(25)
        cards_game.all_cards()
        cards_game.order_cards()
        check_list = cards_game.list_bito + cards_game.player_1_cards + cards_game.player_2_cards
        un = set(check_list)
        self.assertEqual((len(cards_game.list_bito) + len(cards_game.player_1_cards) + len(cards_game.player_2_cards)), 36)
        self.assertEqual(len(cards_game.deck), 0)
        self.assertEqual(len(un), 36)

    def test_dobor(self):
        cards_game = Durak(1)
        cards_game.all_cards()
        cards_game.order_cards()
        self.assertEqual(len(cards_game.player_1_cards), 6)
        self.assertEqual(len(cards_game.player_2_cards), 6)