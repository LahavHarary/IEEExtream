"""
QUEUE
#FIFO:
Cycle           0   1   2   3   4   5
Page Requested  -   0   1   2   3   4
OS Page 0       -   0   0   0   0   4*
OS Page 1       -   -   1   1   1   1
OS Page 2       -   -   -   2   2   2
OS Page 3       -   -   -   -   3   3

LIST
#LRU:
Cycle           0   1   2   3   4   5
Page Requested  -   0   1   2   3   4
OS Page 0       -   0   0   0   0   4*
OS Page 1       -   -   1   1   1   1
OS Page 2       -   -   -   2   2   2
OS Page 3       -   -   -   -   3   3

FIFO = 1
LRU = 1
No improvment
____________________________________________

#FIFO
Cycle      0   1   2   3   4   5   6   7
New Data   -   0   1   0   2   0   8   0
OS Page 0  -   0   0   0   2*  2   8*  8
OS Page 1  -   -   1   1   1   0*  0   0

#LRU
Cycle      0   1   2   3   4   5   6   7
New Data   -   0   1   0   2   0   8   0
OS Page 0  -   0   0   0   0   0   0   0
OS Page 1  -   -   1   1   2*  2   8*  2

FIFO = 3
LRU = 2


p = number of pages in os
s = page size
n = number of memory accesses by the app

    I am creating two variables named swQ and swL
    Two lists qFifo and listLru
    I run with a for loop and each iteration a flag for Q and flag for L is created.
    I am getting a number from the user and divide it by s (size of the pages, the division is taking the
        floor of the number).

    * I am running on the another for loop for the queue.
    if the Q[k] is equal to the number divided by s then flagQ is set to 1

    *  I am running on the another for loop for the list.
    if the L[k] is equal to the number divided by s then flagL is set to 1
    in addition to that, I remove that number and add it right back at the beggining of the loop

    later on:

    * If flagQ is 1 it means that nothing new needs to be added to the Q.
        if flag Q is 0 it means that nothing inside of the Q was equal to the number and the number
        needs to be added to the queue.
        I can't just add the number to the queue because I have memory issue in this question.
        I am checking if there is room inside the Q, if there isn't then I need to pop the last used
        and add one to the counter of switches. (NOTE: Popping is for 0)
        After that, Number will be added to Q.

    * If flagL is 1 it means that nothing new needs to be added to the Q. (I had already
        taken cared of it).

        if flagL is 0 it means that nothing inside of the Q was equal to the number and the number
        needs to be added to the List.
        I can't just add the number to the List because I have memory issue in this question.
        I am checking if there is room inside the L, if there isn't then I need to pop the last used
        and add one to the counter of switches. (NOTE: Popping is for P-1)
        After that, Number will be added to List.


        Lastly: I need to check whether moving to LRU was worth is so I am comparing between the counters
"""


def MemoryManagementFunction(p, s, n):
    switchesQueue = 0  # FIFO
    switchesList = 0  # LRU

    queueFifo = []  # FIFO
    listLru = []  # LRU

    for i in range(n):
        flagQ = 0
        flagL = 0
        number_from_user = int(input())
        number_from_user = int(number_from_user // s)

        for k in range(len(queueFifo)):
            if queueFifo[k] == number_from_user:
                flagQ = 1;
                break

        for k in range(len(listLru)):
            if listLru[k] == number_from_user:
                listLru.remove(listLru[k])
                listLru.insert(0, number_from_user)
                flagL = 1
                break

        if flagQ == 0:
            if (len(queueFifo) == p):
                queueFifo.pop(0)
                switchesQueue += 1
            queueFifo.append(number_from_user)

        if flagL == 0:
            if (len(listLru) == p):
                listLru.pop(p-1)
                switchesList += 1
            listLru.insert(0, number_from_user)

    if (switchesList < switchesQueue):
        print("yes", switchesQueue, switchesList)
    else:
        print("no ", switchesQueue, switchesList)


test_cases = int(input())
for i in range(test_cases):
    p, s, n = [int(n) for n in input().split()]
    MemoryManagementFunction(p,s,n)