import string
import random
case_num = int(input())
if case_num == 0:
    print("Enjoy the Codeathon")
elif case_num == 1:
    print("Sample cases do NOT give any points and watch out for   extra      spaces")
else:
    #intentional space at beginning
    letters = '               abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sentence = "".join([random.choice(letters) for i in range(case_num*10)])
    print(sentence)