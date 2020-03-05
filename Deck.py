#The module allows you to mix cards and select N cards

import random
import result_work


class Deck:
    def shuffle_card(self, lst_card):
        shuffle_lst = []
        while len(lst_card) != len(shuffle_lst):
            ind = random.randint(0, len(lst_card)-1)
            shuffle_lst.append(lst_card[ind])
        return shuffle_lst

    def get_card(self, value_n, shuffle_card):
        return [shuffle_card[ind] for ind in range(value_n)], shuffle_card[value_n:]

    def get_cards_from_template(self, template, list_cards):
        return result_work.pattern_search(template, list_cards)
