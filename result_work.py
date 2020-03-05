#In this module, all possible cards in the deck are formed and the result of the program execution

import Deck
import functools


def forming_list_card():
    lst_1, lst_2, lst_3 = [' черви', ' бубен', ' треф', ' пик'], [str(i) for i in range(2, 11)], ['Валет', 'Дама',
                                                                                                  'Король', 'Туз']
    for i in range(len(lst_3)):
        lst_2.append(lst_3[i])
    return functools.reduce(lambda x1, x2: x1 + x2, [list(map(lambda num: num + letter, lst_2)) for letter in lst_1],
                            [])


def forming_list_with_cards_by_template_part_1(value_second_part_template, list_with_card, symbol, length):
    res_lst, buff_lst = [], []
    for ind, value in enumerate(list_with_card):
        if value.endswith(value_second_part_template) is True:
            buff_lst.append(value)
    for value in buff_lst:
        if symbol == '%' and (len(value.split(' ')[0]) == length or len(buff_lst) == length):
            res_lst.append(value)
        elif symbol == '*':
            res_lst.append(value)
    return res_lst


def forming_list_with_cards_by_template_part_2(value_first_part_template, list_with_card):
    res_lst = []
    for ind, value in enumerate(list_with_card):
        if value.startswith(value_first_part_template) is True:
            res_lst.append(value)
    return res_lst


def forming_list_with_cards_by_template_part_3(value_first_part_template, value_second_part_template, list_with_card):
    res_lst, buff_lst = [], []
    for ind, value in enumerate(list_with_card):
        if value.startswith(value_first_part_template) is True:
            buff_lst.append(value)
    for value in buff_lst:
        if value.endswith(value_second_part_template) is True:
            res_lst.append(value)
    return res_lst


def forming_get_cards(template, list_with_card, symbol, length):
    str_2 = template.split(symbol)
    if str_2[0] == '':
        list_get_card = forming_list_with_cards_by_template_part_1(str_2[1], list_with_card, symbol, length)
    elif str_2[1] == '':
        list_get_card = forming_list_with_cards_by_template_part_2(str_2[0], list_with_card)
    else:
        list_get_card = forming_list_with_cards_by_template_part_3(str_2[0], str_2[1], list_with_card)
    return list_get_card


def del_get_card(list_get_card, list_with_card):
    for value in list_get_card:
        for ind, val in enumerate(list_with_card):
            if value == val:
                list_with_card.pop(ind)
                break
    return list_with_card


def forming_get_card(template, list_with_card):
    for ind, value in enumerate(list_with_card):
        if template in value:
            return list_with_card.pop(ind)


def pattern_search(template, list_with_card):
    if template.find('*') != -1:
        list_get_card = forming_get_cards(template, list_with_card, '*', length=0)
    elif template.find('%') != -1:
        list_get_card = forming_get_cards(template, list_with_card, '%', length=1)
    else:
        list_get_card = forming_get_card(template, list_with_card)
    return list_get_card


def menu(list_of_selected_card, class_obj_deck):
    while True:
        print('\n1)Getting a deck of cards by the value of N;\n'
              '2)Getting a deck of cards by the value of template;\n'
              '0)Program shutdown.')
        key = int(input('Input value key: '))
        if key == 1:
            list_of_selected_cards_by_value, list_of_selected_card = \
                class_obj_deck.get_card(int(input('\nEnter the number of cards you want to choose from the deck: ')),
                                        list_of_selected_card)
            print('Remaining deck of cards: ', list_of_selected_card)
            print('Drawn cards from the deck: ', list_of_selected_cards_by_value)
        elif key == 2:
            template = input('Enter a template value: ')
            list_of_selected_cards_by_value = class_obj_deck.get_cards_from_template(template, list_of_selected_card)
            list_of_selected_card = del_get_card(list_of_selected_cards_by_value, list_of_selected_card)
            print('Remaining deck of cards: ', list_of_selected_card)
            print('Drawn cards from the deck: ', list_of_selected_cards_by_value)
        elif key == 0:
            break


def result():
    lst_all_card = forming_list_card()
    class_obj_deck = Deck.Deck()
    list_shuffle_cards = class_obj_deck.shuffle_card(lst_all_card)
    menu(list_shuffle_cards, class_obj_deck)
