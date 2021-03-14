p, n = map(int, input().split())
processes = (input().split())
show_explanation = False
if show_explanation:
    print("starting configuration")
    print(" ".join(processes))

for i in range(n):
    command = int(input())
    cur = processes.pop(command%p)
    processes.insert(0, cur)
    if show_explanation:
        print("pressed tab", command, "time(s):")
        print(" ".join(processes))

print(" ".join(processes))


# p, n = map(int, input().split())
# processes = input().split()
# last_used = []
# for i in range(p):
#     last_used.append(p-i)
# print(last_used)
# # last_used = dict()
# # for i, ele in enumerate(reversed(processes)):
# #     last_used[processes[i]] = len(processes) - i
# # print(last_used)
# used_num = len(processes) + 1
# for i in range(n):
#     cur = int(input())
#     last_used[cur%p] = used_num
#     used_num += 1

# together = list(zip(last_used, processes))
# together.sort(reverse=True)
# print(together)
# print(" ".join([i[1] for i in together]))