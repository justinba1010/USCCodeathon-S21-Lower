x = int(input())
y = int(input())
board = []
for i in range(y):
    board.append(input())

door_count = 0
#do not check top left or bottom left (both are corners)
for i in range(1, y-1):
    #check left side
    if board[i][1] != "F":
        door_count += 1
    #check right side
    if board[i][x-2] != "F":
        door_count += 1
#do not check top right or bottom right (both are corners)
for i in range(1, x-1):
    #check top side
    if board[1][i] != "F":
        door_count += 1
    #check bottom side
    if board[-2][i] != "F":
        door_count += 1

print(door_count)