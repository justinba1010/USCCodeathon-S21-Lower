p, n = map(int, input().split())
processes = input().split()
show_explanation = False
if show_explanation:
    print("starting configuration:")
    # print(" ".join(processes))

message = ""
just_showed = False
instruct_pos = 0
while instruct_pos < n:
    command = 0
    if show_explanation and not just_showed:
        print(" ".join(processes))
    just_showed = False
    if len(processes) == 0:
        message = "ALL GONE"
        break
    if processes[0].endswith("DARK"):
        if show_explanation:
            print("Ended with 'DARK', Tom's eyes are saved!")
        break
    if processes[0].endswith("TEMP"):
        processes.pop(0)
        if show_explanation:
            print("Ended with 'TEMP', process was closed!")
        continue
    if processes[0].endswith("HUNGRY"):
        if len(processes) > 1:
            processes.pop(1)
            if show_explanation:
                print("Ended with 'HUNGRY', process to the right was closed!")
        if len(processes):
            processes.pop(0)
            if show_explanation:
                print("'HUNGRY' process closed itself!")
        continue
    command = int(input())
    instruct_pos += 1
    cur = processes.pop(command%len(processes))
    processes.insert(0, cur)
    if show_explanation:
        print("pressed tab", command, "time(s):")
        print(" ".join(processes))
        just_showed = True

if message == "":
    print(processes[0])
else:
    print(message)