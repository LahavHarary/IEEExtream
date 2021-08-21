
"""
# 2
# 4 2
# 3
# 5
# 1
# 1
# 5 4
# 30
# 40
# 20
# 41
# 50

#  2
# [1,1,3,5]
# [0,2,2]

# K=3, N=6
# [5,5,5,7,7,8]
# [0,0,2,0,1]
#
#

    At first I'm creating two lists, dogsSize and dogsHefrsh they are both empty at the beginning.
    sum equals 0.

    I am running on a for loop and each time I get a number from the user.
    The number is being added to dogsSizes

    dogSizes list is being sorted.

    I am running on a second loop this time some is the difference between two dogs in the list.
    some is being entered to dogsHefresh list.
    because dogSizes was sorted I know that each one of the elemnets in dogsHefresh is the smallest

    I am sorting dogHefresh list as well
    Creating another loop, this one will run until N-K (which means the amount of dogs - the amount of
        dog walkers).
    I know that dogsHefresh has the smallest elements and that its sorted so I only need to calculate sum.

    sum is being returned



"""


def func(N,K):

    dogsSizes = []
    dogsHefresh = []
    sum = 0

    for i in range(N):
        some = int(input())
        dogsSizes.append(some)

    dogsSizes.sort()
    
    for i in range(N-1):
        some = dogsSizes[i+1] - dogsSizes[i]
        dogsHefresh.append(some)

    dogsHefresh.sort()
    for i in range(N-K):
        sum += dogsHefresh[i]

    return sum

t = int(input())
for i in range(t):
    N,K  = [int(n) for n in input().split()]
    print(func(N,K))