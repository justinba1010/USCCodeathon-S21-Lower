#!/usr/local/bin/python3
from random import randint
case_num = int(input())
if case_num == 0:
    print(4, 2)
elif case_num == 1:
    print(5, 4)
else:
    n = randint(3, 100000)
    j = randint(3, 2 ** 25)
    print(n, j)