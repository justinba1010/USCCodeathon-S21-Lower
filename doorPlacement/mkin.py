import random
case_num = int(input())
x = random.randint(4, 99)
y = random.randint(4, 99)
if case_num == 0:
    x = 5
    y = 8
elif case_num == 1:
    x = 6
    y = 10

board = [list("."*x) for i in range(y)]
furniture_count = random.randint(3, max(3, x*y//3))
for i in range(furniture_count):
    pos_x = random.randint(1, x-2)
    pos_y = random.randint(1, y-2)
    board[pos_y][pos_x] = "F"

board[0] = list("W"*x)
board[-1] = list("W"*x)
for i in range(y):
    board[i][0] = "W"
    board[-i-1][-1] = "W"

print(x)
print(y)
for line in board:
    print("".join(line))