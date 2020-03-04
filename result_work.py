#In this module, all possible cards in the deck are formed and the result of the program execution

import Check, Deck, functools

def forming_list_card():
    lst_1 = ['ch', 'b', 'kr', 'p']
    lst_2 = [str(i) for i in range(2, 15)]
    return functools.reduce(lambda x1, x2: x1 + x2, [list(map(lambda num: num + letter, lst_2)) for letter in lst_1], [])

def result():
    lst_all_card = forming_list_card()
    lst_1 = Check.check_if_list_is_empty(lst_all_card, int(input('Введите количество кард в колоде: ')))
    if Check.check_get_card(lst_1) is True:
        lst = Deck.Deck()
        lst_2 = lst.shuffle_card(lst_1)
        N = int(input('Введите количество карт, которое Вы хотите выбрать из колоды: '))
        lst_3, lst_1 = lst.get_card(N, lst_2)
        print(lst_2, lst_3, lst_1)
    else: print('Карт нет. Поэтому перемешивание и выбор N карт невозможен.')
