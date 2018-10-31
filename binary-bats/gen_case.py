import random

exponent = int(input())

# To generate a case, we need a max interval and a number of bats
max_interval = 2**exponent
num_bats = max_interval // 2

# Every interval is unique, we store them in a set
intervals = set()

# Randomly select up to `num_bats` unique intervals
for _ in range(num_bats):
    intervals.add(random.randint(1, max_interval))

# We add 1 padding to ensure the bat with the largest interval gets two squeaks
output = [0] * (max(intervals) + 1)

output[0] = len(intervals) % 2

for interval in intervals:
    for i in range(interval, len(output), interval):
        output[i] ^= 1

output = list(map(str, output))
print("".join(output))
