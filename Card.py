#The module allows you to select a certain number of cards from the deck

import random


class Card:
    def get_card(self, list_of_selected_card, val):
        return random.sample(list_of_selected_card, val)
