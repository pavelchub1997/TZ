import random

class Card():
    def get_card(self, lst, val):
        return random.sample(lst, val)