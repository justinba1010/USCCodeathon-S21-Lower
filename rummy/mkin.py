## Copyright 2021 William Hobbs
## Inspired by Dr. Jeremy Lewis
## Code-A-Thon Problem for 145 and 146

from random import randint, sample

def generate_string():
    test_num = int(input())
    if test_num == 0:
        num_of_cases = 3
    elif test_num == 1:
        num_of_cases = 4
    else:
        num_of_cases = test_num//5 + 4
    print(num_of_cases)
    for t in range(num_of_cases):
        if test_num == 0:
            number_of_cards = randint(10, 15)
        elif test_num == 1:
            number_of_cards = randint(16, 20)
        else:
            number_of_cards = randint(20, 52)
            # number_of_cards = 52
        output = generate_cards(number_of_cards)
        print(number_of_cards)
        print(" ".join(output))
        # number_of_cards = 52
    # output_string = str(number_of_cards)
    # while len(output) < number_of_cards:
        # output.add(generate_cards())
    # for i in range(number_of_cards):
    #     output_string = output_string + " " + generate_card()

def generate_cards(amount):
    # card_value = randint(1, 13)
    ## 1 is ace, 2-10 are their value, 11, 12, 13 are jack, queen, king, respectively
    # card_suit = randint(1, 4)
    #make a deck
    deck = []
    for value in range(1, 14):
        for suit in range(1, 5):
            deck.append(get_value(value) + get_suit(suit))
    return sample(deck, k=amount)
    # ret = get_value(card_value) + get_suit(card_suit)
    # return ret

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
