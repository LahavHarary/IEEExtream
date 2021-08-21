

"""
t = no of times for the problem
n = 1<=n<=22000

#                   __  (5)
#               __      (4)
#           __          (3)
#       __              (2)
#    __                 (1)
#

#   1,2,3,4,5
#   1,2,4,5
#   1,2,3,5
#   1,3,4,5
#   1,3,5
#   2,3,4,5
#   2,4,5
#   2,3,5


    a few examples are written up there.

    At first, I've created a list with the vlaues of 1 and 2
        I am checking if the amount of steps is 1 or 2
        1 means that he can jump 1 only
        2 means that he can skip the first step only so my options are either jump to 1
        then 2 or jump to 2 directly (2 options).

    I am using a for loop from 2 to n,
    In the loop I am taking whatever was before (-1 and -2) and adding it to the new amount of stairs.

    for example n = 3
    I am starting at two, which means that the boy can jump to the first and then the second step
        or the second step directly -> [1,2, ?]
        ? = is equal to everything he could've done before [1,2, *3* ]
        because he has three options:
        1. jump 1->2->3
        2. jump 1->3
        3. jump 2->3

    this sequence is true for every n.

    at the end I am returning the maximum amount of things that he can do so I need to return the
    last spot inside my array.

"""




def fun(n):
    listOfStuff = [1, 2]
    if n == 1:
        return listOfStuff[0]
    elif n == 2:
        return listOfStuff[1]
    else:
        for i in range(2, n):
            listOfStuff.append(listOfStuff[i - 2] + listOfStuff[i - 1])

    return listOfStuff[i]


t = int(input())

for i in range(t):
    n = int(input())
    print(fun(n))



