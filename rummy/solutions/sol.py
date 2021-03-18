## Copyright 2021 William Hobbs

def main():
    card_count = int(input())
    the_input = input()
    ## print(the_input)
    cards = the_input.split(" ")
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    value_of_hand = 0
    for i in range(len(cards)):
        numerical_value = cards[i][0]
        ## print(numerical_value)
        if numerical_value == "A":
            number_value = 1
        elif numerical_value == "K":
            number_value = 13
        elif numerical_value == "Q":
            number_value = 12
        elif numerical_value == "J":
            number_value = 11
        elif numerical_value == "0":
            number_value = 10
        else:
            number_value = int(numerical_value)
        count[number_value-1] += 1
        ## print(number_value)
    
    for i in range(len(count)): ## should be less than 13 iterations
        if count[i] == 3:
            if i == 0:
                value_of_hand += 45
            if i >=1 and i <= 8:
                value_of_hand += 15
            if i >= 9 and i <= 12:
                value_of_hand += 30
        if count[i] == 4:
            if i == 0:
                value_of_hand += 60
            if i >=1 and i <= 8:
                value_of_hand += 20
            if i >= 9 and i <= 12:
                value_of_hand += 40
    print(value_of_hand)


case_count = int(input())
for t in range(case_count):
    main()
