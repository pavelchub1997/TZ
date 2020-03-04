import random

class Deck:
    def shuffle_card(self, lst_card):
        shuffle_lst = []
        while lst_card != []:
            ind = random.randint(0, len(lst_card)-1)
            shuffle_lst.append(lst_card[ind])
            lst_card.pop(ind)
        return shuffle_lst

    def get_card(self, N, shuffle_card):
        return [shuffle_card[ind] for ind in range(N)], shuffle_card[N:]