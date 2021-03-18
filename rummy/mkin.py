## Copyright 2021 William Hobbs
## Inspired by Dr. Jeremy Lewis
## Code-A-Thon Problem for 145 and 146

from random import randint

def generate_string():
    number_of_cards = randint(1, 52)
    output_string = str(number_of_cards)
    for i in range(number_of_cards):
        output_string = output_string + " " + generate_card()
    print(output_string)

def generate_card():
    card_value = randint(1, 13)
    ## 1 is ace, 2-10 are their value, 11, 12, 13 are jack, queen, king, respectively
    card_suit = randint(1, 4)
    ret = get_value(card_value) + get_suit(card_suit)
    return ret

def get_value(argument):
    switcher = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "0",
        11: "J",
        12: "Q",
        13: "K"
    }
    return switcher.get(argument)

def get_suit(argument):
    switcher = {
        1: "C",
        2: "D",
        3: "S", 
        4: "H"
    }
    return switcher.get(argument)

generate_string()
