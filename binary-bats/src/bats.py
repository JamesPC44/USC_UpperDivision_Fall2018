#!/usr/bin/python3

def main():
    bits = list(map(int, input()))

    bats = 0
    for num in range(1,len(bits)):
        if bits[num] == 1:
            bats += 1
            for j in range(num+num, len(bits), num):
                bits[j] ^= 1

    print(bats)

if __name__ == "__main__":
    main()
