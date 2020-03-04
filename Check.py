#The module allows you to check for empty list

import Card

def check_if_list_is_empty(list_all_card, val):
    if val == 0: return []
    else:
        object_card = Card.Card()
        return object_card.get_card(list_all_card, val)

def check_get_card(lst):
    if lst == []: return False
    else: return True
