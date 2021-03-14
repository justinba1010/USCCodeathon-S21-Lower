#!/usr/local/bin/python3
import random
import string
case_num = int(input())
if case_num == 0:
    p = 4
    n = 3
elif case_num == 1:
    p = 6
    n = 4
elif case_num <= 20:
    p = random.randint(3, 1000)
    n = random.randint(3, 100)
else:
    p = random.randint(case_num * 1000, case_num * 2000)
    n = random.randint(case_num*1000, case_num*2000)

print(p, n)
processes = set()
while len(processes) < p:
    cur = "".join(random.choices(string.ascii_uppercase, k=6))
    processes.add(cur)

print(" ".join(processes))

for i in range(n):
    if case_num <= 20:
        times_to_press = random.randint(1, p * 3)
    elif case_num <=30:
        times_to_press = random.randint(p//2, p)
    else:
        times_to_press = random.randint(p//2, p) * 1000

    print(times_to_press)