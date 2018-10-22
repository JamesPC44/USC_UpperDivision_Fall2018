import random
import time

small = 100
big = 10000
bigger = 1000000
biggest = 25000000

alphabet = 'abcdefghijklmnopqrstuvwxyz'
bigstr1 = ''
bigstr2 = ''

for a in range(17,20):
    start = time.time()
    print ("Starting")

    bigstr1 = ''
    bigstr2 = ''
    f = open("inputs/input" + str(a).zfill(2) + ".txt", "a")

    for x in range(biggest):
        bigstr1 += random.choice(alphabet)

    for x in range(biggest):
        bigstr2 += random.choice(alphabet)

    f.write(bigstr1)
    f.write('\n')
    f.write(bigstr2)

    print (time.time() - start)

