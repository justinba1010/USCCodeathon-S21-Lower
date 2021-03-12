#this is the naive solution
case_count = int(input())
for t in range(case_count):
    n, j =list(map(int,input().split()))
    # n, j = [20, 4]
    j %= n
    pos = 0
    hitCount = n -1
    while pos < n:
        pos += j
        pos = pos % n
        if pos == 0:
            break
        hitCount -= 1
    print(hitCount)