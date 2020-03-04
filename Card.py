#The module allows you to select a certain number of cards from the deck

import random

class Card():
    def get_card(self, lst, val):
        return random.sample(lst, val)
