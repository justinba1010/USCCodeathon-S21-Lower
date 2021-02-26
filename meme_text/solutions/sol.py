sentence = list(input().lower())
pos = 0
should_be_cap = False
while pos < len(sentence):
    if should_be_cap:
        sentence[pos] = sentence[pos].upper()
    if sentence[pos] != " ":
        should_be_cap = not should_be_cap
    pos += 1
print("".join(sentence))