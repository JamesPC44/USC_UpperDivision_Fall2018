import random
import time

small = 100
big = 10000
bigger = 1000000
biggest = 20000000

alphabet = 'abcdefghijklmnopqrstuvwxyz'
bigstr1 = ''
bigstr2 = ''

for a in range(8,10):
    start = time.time()
    print ("Starting")

    bigstr1 = ''
    bigstr2 = ''
    f = open("test_cases/input/input" + str(a).zfill(2) + ".txt", "a")

    for x in range(random.randint(1,big)):
        bigstr1 += random.choice(alphabet)

    for x in range(big):
        bigstr2 += random.choice(alphabet)

    f.write(bigstr1)
    f.write('\n')
    f.write(bigstr2)

    print (time.time() - start)

