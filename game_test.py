import unittest

from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game("Adam")

    def test_add_item(self):
        self.assertEqual(len(self.game.inventory), 0)
        self.assertEqual(self.game.add_item("teapot"), 1)
