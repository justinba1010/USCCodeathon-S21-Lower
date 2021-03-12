#!/usr/local/bin/python3
from random import randint
case_num = int(input())
if case_num == 0:
    print(1)
    print(4, 2)
elif case_num == 1:
    print(2)
    print(5, 4)
    print(8, 10)
else:
    case_count = case_num * 10
    print(case_count)
    for i in range(case_count):
        if case_num > 30:
            n = randint((10 ** 9) - 50, 10 ** 9)
            j = randint(3, 10)
        elif case_num > 20:
            j = randint(3, (10**8))
            n = j-randint(1,10)
        else:
            n = randint(3, (10 ** 4))
            j = randint(3, (10 **4))
        print(n, j)