# randomizing algorithm

# this one is good

import math

minnum = int(input('Enter your min value > '))
maxnum = int(input('Enter your max value > '))
numtoadd = 22
numsum = minnum
numstring = ''

numlist = []

i = minnum

while i <= maxnum:
    numlist.append(i)
    i += 1

while i <= maxnum:
    numstring = numstring + ' '+ str(i)
    i += 1

numstring2 = numstring

numscalled = ' '

def randomize_list(numlist):
    global i, numtoadd, numsinlist, numscalled

    randomnum = ' '

    counter = 0

    if i >= numsinlist:
        while i >= numsinlist:
            i = i-(maxnum-minnum)

    if numtoadd >= numsinlist:
        numtoadd = numtoadd - numsinlist

    randomnum = numlist[i]

    i += numtoadd

    numtoadd += 1

    counter += 1

    return randomnum

    

i = 0

randomlist = []

numtoadd = 22

numsinlist = 0
while True:
    try:
        blank = numlist[numsinlist]

    except:
        break

    numsinlist += 1

j = 0

numscalled = ' '

while j <= maxnum-minnum:
    
    randomlist.append(randomize_list(numlist))

    j += 1

numtoadd = 33

numsinlist = 0
while True:
    try:
        blank = randomlist[numsinlist]

    except:
        break

    numsinlist += 1

j = 0

numscalled = ' '

i = 0

randomrandomlist = []

while j <= maxnum-minnum:

    randomrandomlist.append(randomize_list(randomlist))
    j += 1

numtoadd = 44

numscalled = ' '

numsinlist = 0
while True:
    try:
        blank = randomrandomlist[numsinlist]

    except:
        break

    numsinlist += 1

while True:
    input(randomize_list(randomrandomlist))
    j += 1