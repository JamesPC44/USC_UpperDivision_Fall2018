import time
import collections

str1 = input()
str2 = input()
dic1 = collections.Ordereddic()
dic2 = collections.Ordereddic()
 
dic1['a'] = 0
dic1['b'] = 0
dic1['c'] = 0
dic1['d'] = 0
dic1['e'] = 0
dic1['f'] = 0
dic1['g'] = 0
dic1['h'] = 0
dic1['i'] = 0
dic1['j'] = 0
dic1['k'] = 0
dic1['l'] = 0
dic1['m'] = 0
dic1['n'] = 0
dic1['o'] = 0
dic1['p'] = 0
dic1['q'] = 0
dic1['r'] = 0
dic1['s'] = 0
dic1['t'] = 0
dic1['u'] = 0
dic1['v'] = 0
dic1['w'] = 0
dic1['x'] = 0
dic1['y'] = 0
dic1['z'] = 0

dic2['a'] = 0
dic2['b'] = 0
dic2['c'] = 0
dic2['d'] = 0
dic2['e'] = 0
dic2['f'] = 0
dic2['g'] = 0
dic2['h'] = 0
dic2['i'] = 0
dic2['j'] = 0
dic2['k'] = 0
dic2['l'] = 0
dic2['m'] = 0
dic2['n'] = 0
dic2['o'] = 0
dic2['p'] = 0
dic2['q'] = 0
dic2['r'] = 0
dic2['s'] = 0
dic2['t'] = 0
dic2['u'] = 0
dic2['v'] = 0
dic2['w'] = 0
dic2['x'] = 0
dic2['y'] = 0
dic2['z'] = 0

stack1 = []
stack2 = []

for x in str1:
    dic1[x] = dic1[x] + 1

for x in str2:
    dic2[x] = dic2[x] + 1

# At this point each string is in its own dicionary
for key, value in dic1.items():
    if dic1[key] >= dic2[key]:
        dic1[key] = dic1[key] - dic2[key]
        dic2[key] = 0
    else:
        dic2[key] = dic2[key] - dic1[key]
        dic1[key] = 0
    
    # In java this is equivalent to Collections.nCopies(number, element)
    stack1 = stack1 + ([key] * dic1[key])
    stack2 = stack2 + ([key] * dic2[key])

if len(stack1) == 0 and len(stack2) == 0:
    print('AC JUMBLE')

else:
    retval = 0
    while len(stack1) != 0 and len(stack2) != 0:
        v1 = ord(stack1.pop())
        v2 = ord(stack2.pop())
        retval += abs(v1 - v2)
    
    if len(stack1) != 0:
        while len(stack1) != 0:
            retval += ord(stack1.pop()) - 96
        print(retval)
    elif len(stack2) != 0:
        while len(stack2) != 0:
            retval += ord(stack2.pop()) - 96
        print(retval)
    else:
        print(retval)