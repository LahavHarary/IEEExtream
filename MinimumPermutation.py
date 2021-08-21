
"""
    A = array
    S = set
    N = Size of array
    M = Size of set

    creating a list made with S and sorting it.
    For loop in order to insert the smallest in the set into the list in order


"""


def function(A, S):
    l = list(S)
    l.sort()

    j = 0  # ArrayIndex
    i = 0  # newSetIndex
    while i in range(len(l)) and j < len(A):
        if (l[i] < A[j]):
            A.insert(j, l[0])
            l.pop(i)
        j += 1

    A.extend(l)

    for i in range(len(A)):
        print(A[i], end=" ")


N, M = [int(n) for n in input().split()]
A = [int(n) for n in input().split()]
S = [int(n) for n in input().split()]

function(A, S)
