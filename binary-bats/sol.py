input = list(map(int, input()))

idxs = []

for i in range(len(input)):
    if input[i] == 1 and i != 0:
        idxs.append(i)
        for j in range(i, len(input), i):
            input[j] ^= 1

print(len(idxs))
