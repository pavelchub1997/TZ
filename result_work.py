#In this module, all possible cards in the deck are formed and the result of the program execution

import Check
import Deck
import functools
import sys


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
        if value.endwith(value_second_part_template) is True:
            buff_lst.append(value)
            list_with_card.pop(ind)
    for value in buff_lst:
        if symbol == '%' and len(value.split(' ')) == length:
            res_lst.append(value)
        else:
            res_lst.append(value)
    return res_lst, list_with_card


def forming_list_with_cards_by_template_part_2(value_first_part_template, list_with_card):
    res_lst = []
    for ind, value in enumerate(list_with_card):
        if value.startwith(value_first_part_template) is True:
            res_lst.append(value)
            list_with_card.pop(ind)
    return res_lst, list_with_card


def forming_list_with_cards_by_template_part_3(value_first_part_template, value_second_part_template, list_with_card):
    res_lst, buff_lst = [], []
    for ind, value in enumerate(list_with_card):
        if value.startswith(value_first_part_template) is True:
            buff_lst.append(value)
            list_with_card.pop(ind)
    for value in buff_lst:
        if value.endswith(value_second_part_template) is True:
            res_lst.append(value)
    return res_lst, list_with_card


def forming_get_cards(template, list_with_card, symbol, length):
    str_2 = template.split(symbol)
    if str_2[0] == '':
        list_get_card, list_with_card = forming_list_with_cards_by_template_part_1(str_2[1], list_with_card, symbol,
                                                                                   length)
    elif str_2[1] == '':
        list_get_card, list_with_card = forming_list_with_cards_by_template_part_2(str_2[0], list_with_card)
    else:
        list_get_card, list_with_card = forming_list_with_cards_by_template_part_3(str_2[0], str_2[1], list_with_card)
    return list_get_card, list_with_card


def forming_get_card(template, list_with_card):
    for ind, value in enumerate(list_with_card):
        if template in value:
            return [template], list_with_card.pop(ind)


def pattern_search(template, list_with_card):
    if template.find('*') != 1:
        list_get_card, list_with_card = forming_get_cards(template, list_with_card, '*', length=0)
    elif template.find('%') != 1:
        list_get_card, list_with_card = forming_get_cards(template, list_with_card, '%', length=1)
    else:
        list_get_card, list_with_card = forming_get_card(template, list_with_card)
    return list_get_card, list_with_card


def menu(list_of_selected_card, class_obj_deck):
    key = int(input('Input value key: '))
    while key != 0:
        print('\n1)Getting a deck of cards by the value of N;\n'
              '2)Getting a deck of cards by the value of template\n'
              '0)Program shutdown.')
        if key == 1:
            list_of_selected_cards_by_value, list_of_selected_card = \
                class_obj_deck.get_card(int(input('Enter the number of cards you want to choose from the deck: ')),
                                        list_of_selected_card)
            print(list_of_selected_card, list_of_selected_cards_by_value)
        elif key == 2:
            template = input('Enter a template value: ')
            list_of_selected_cards_by_value, list_of_selected_card = \
                class_obj_deck.get_cards_from_template(template, list_of_selected_card)
            print(list_of_selected_card, list_of_selected_cards_by_value)
        elif key == 0:
            sys.exit()


def result():
    lst_all_card = forming_list_card()
    lst_of_selected_card = Check.check_if_list_is_empty(lst_all_card, int(input('Введите количество кард в колоде: ')))
    if Check.check_get_card(lst_of_selected_card) is True:
        class_obj_deck = Deck.Deck()
        list_shuffle_cards = class_obj_deck.shuffle_card(lst_of_selected_card)
        menu(list_shuffle_cards, class_obj_deck)
    else:
        print('There are no cards. Therefore, mixing and selection of N cards is not possible.')
        sys.exit()
