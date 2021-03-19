from collections import deque
p, n = map(int, input().split())
processes = (input().split())

for i in range(n):
    command = int(input())
    cur = processes.pop(command%p)
    processes.insert(0, cur)
print(" ".join(processes))