
"""
# Credit for yuval meir for teaching me The theoretically optimal page replacement algorithm in Os


#   2
#   5
#   7   7   2   11  7
#   10
#   9   1   7   6   9   9   8   7   6   7

#   1   1   2   2   1
#   7   7   2   11  7
#   2   7   7   7   11

#   0   1   2   3   4
#   1   1   2   2   1
#   7   7   2   11  7
#   2   7   7   7   11

This algorithm consists of the theoretically optimal page replacement algorithm

    I am looking at the array and determine how many switches would be minimal.


"""


def function(c):

    firstIndex = 0
    secondIndex = 1
    startLoopIndex = 1
    while c[firstIndex] == c[secondIndex]:
        secondIndex += 1
        startLoopIndex += 1

    if(len(c) == 1):
        return 1
    elif(len(c) == 2):
        if(c[0] == c[1]):
            return 1
        return 0

    stepCounter = 2


    for i in range(startLoopIndex+1,len(c)):
        j = i
        while(j < len(c) and c[j] != c[firstIndex] and c[j] != c[secondIndex]):
            j += 1

        if(j < len(c)):
            if(c[j] == c[firstIndex]):
                if (c[i] != c[firstIndex]):
                    secondIndex = i
                    stepCounter += 1
            elif(c[j] == c[secondIndex]):
                if (c[i] != c[secondIndex]):
                    firstIndex = i
                    stepCounter += 1
        else:
            secondIndex = i
            stepCounter += 1


    return stepCounter

t = int(input())
for i in range(t):
    N = int(input())
    c = [int(n) for n in input().split()]
    print(function(c))