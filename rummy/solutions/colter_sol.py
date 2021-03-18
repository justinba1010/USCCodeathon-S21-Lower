from collections import Counter
cases = int(input())
for t in range(cases):
    card_count = int(input())
    cards = input().split()
    values = Counter([i[0] for i in cards])
    # print(values)
    points = 0
    for j in values:
        # print(j)
        if '1' <= j <= '9':
            if values[j] == 3:
                points += 15
            elif values[j] == 4:
                points += 20
        elif j in "KQJ0":
            if values[j] == 3:
                points += 30
            elif values[j] == 4:
                points += 40
        elif j in "A":
            if values[j] == 3:
                points += 45
            elif values[j] == 4:
                points += 60
    print(points)