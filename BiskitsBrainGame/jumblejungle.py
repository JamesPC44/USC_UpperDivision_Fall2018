import time

start = time.time()

str1 = input()
str2 = input()

# Map for each letter of the alphabet for each string
dic1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
        'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 
        't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

dic2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
        'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 
        't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

stack1 = []
stack2 = []

for x in str1:
    dic1[x] = dic1[x] + 1

for x in str2:
    dic2[x] = dic2[x] + 1

print ("dic 1")
print (dic2)
print ("dic 2")
print (dic1)
# At this point each string is in its own dictionary
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

print ("stack1")
print (stack1)
print ("stack2")
print (stack2)

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


print (time.time() - start)