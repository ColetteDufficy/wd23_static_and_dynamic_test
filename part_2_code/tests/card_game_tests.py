import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Hearts", 8)
        self.card2 = Card("Spades", 1)
        self.card3 = Card("Diamonds", 4)
        self.card_game = CardGame("Poker", [self.card1, self.card2, self.card3])

    def test_card1_has_suit(self):
        self.assertEqual("Hearts", self.card1.suit)
    
    def test_card1_has_value(self):
        self.assertEqual(4, self.card3.value)
    
    def test_check_for_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card2))

    def test_which_is_highest_card(self):
        self.assertEqual(self.card1, self.card_game.highest_card(self.card1, self.card3))

    def test_total_value_of_cards(self):
        self.assertEqual("You have a total of 13", self.card_game.cards_total(self.card_game.cards))