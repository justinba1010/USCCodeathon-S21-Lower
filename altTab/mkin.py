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
elif case_num == 2:
    p = 10
    n = 7
elif case_num <= 20:
    p = random.randint(case_num * 3, 1000)
    n = random.randint(case_num, 100)
else:
    p = random.randint(case_num * 1000, case_num * 2000)
    n = random.randint(case_num*1000, case_num*2000)

def make_process_name():
    return "".join(random.choices(string.ascii_uppercase, k=random.randint(4, 8)))

print(p, n)
processes = set()

harder_cutoff = 20
while len(processes) < p:
    cur = make_process_name()
    chance = random.randint(1, 20)
    if case_num >= harder_cutoff and len(processes) == p - 10:
        break
    

    if chance == 1 and case_num > 10:
        cur += "DARK"
    elif 2 <= chance <= 4:
        cur += "TEMP"
    elif 5 <= chance <= 7 and len(processes) > p // 3:
        cur += "HUNGRY"
    processes.add(cur)

processes = list(processes)
if 40 > case_num >= harder_cutoff:
    while len(processes) < p:
        processes.insert(0, "DARKHUNGRY" + make_process_name() + "TEMP")
elif case_num >= 40:
    while len(processes) < p:
        processes.insert(0, make_process_name() + "HUNGRY")
print(" ".join(processes))

for i in range(n):
    if case_num <= 20:
        times_to_press = random.randint(1, p * 3)
    elif case_num <=30:
        times_to_press = random.randint(max(1, p//2), p)
    else:
        times_to_press = random.randint(1, p)

    print(times_to_press)