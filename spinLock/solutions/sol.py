x, y = map(int,input().split())
secret = input()
board = []
for i in range(y):
    board.append(input())

best = 10000000
winning_column = -1
for i in range(x):
    current = 0
    for j in range(y):
        turn_right = abs(board[j].index(secret[j]) - i)
        turn_left = x - abs(board[j].index(secret[j]) - i)
        current += min(turn_left, turn_right)
    if current < best:
        best = current
        winning_column = i

print(best, winning_column)