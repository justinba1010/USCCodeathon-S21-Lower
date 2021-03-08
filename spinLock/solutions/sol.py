x, y = map(int,input().split())
secret = input()
board = []
for i in range(y):
    board.append(input())

best = 10000000
winning_column = -1
help_text = False
if help_text:
    print("secret word", secret)
    for i in board:
        print("".join(i))
for i in range(x):
    current = 0
    if help_text:
        print("column:", i)
    for j in range(y):
        turn_right = abs(board[j].index(secret[j]) - i)
        turn_left = x - abs(board[j].index(secret[j]) - i)
        min_turns = min(turn_left, turn_right)
        current += min_turns
        # print("min turns on dial", j, "was", min_turns)
    if help_text: 
        print("total turns was", current)
        print()
    if current < best:
        best = current
        winning_column = i

print(winning_column, best)