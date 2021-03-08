import string
import random

case_num = int(input())
# print("case_num", case_num)
# case_num = 4
all_letters = (string.ascii_uppercase)
# print(all_letters)
if case_num == 0:
    letters_per_dial = 4
    y = 3
elif case_num == 1:
    letters_per_dial = 6
    y = 4
else:
    letters_per_dial = case_num + 2
    if case_num <= 10:
        y = case_num * 2
    else:
        y = (case_num+10) ** 2

letters_per_dial = min(letters_per_dial, 26)

# secret = random.sample(all_letters, letters_per_dial)
secret = []
words = []
print(letters_per_dial, y)
for i in range(y):
    cur = random.sample(all_letters, letters_per_dial)
    words.append(cur)
    secret.append(random.choice(cur))
print("".join(secret))
for i in range(y):
    print("".join(words[i]))

