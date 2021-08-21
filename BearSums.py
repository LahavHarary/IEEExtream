def func(S, E, L):

    """
    create a set of elements
    check if current is in set - if so return the min to the left side and max to right side.
    if current is not in set, add its inverse.
    if the loop has finished and nothing was inside return "!OK".

    example:
    S = 8
    L = 1 2 4 4
    {}
    _________________________________
    S - L[index] = 8-1 = 7
    7 is not in set of numbers
    7 is beeing added to set of numbers.
    {7}
    _________________________________
    S - L[index] = 8-2 = 6
    6 is not in set of numbers
    6 is beeing added to set of numbers.
    {7,6}
    _________________________________
    S - L[index] = 8-4 = 4
    4 is not in set of numbers
    4 is beeing added to set of numbers.
    {7,6,4}
    _________________________________
    S - L[index] = 8-4 = 4
    4 is in set of numbers
    L[index] = 4, S-L[index] = 4
    4 NOT < 4 (Smaller has to be on the left side , Bigger has to be on the right side)
    ELSE: return 4,4

    VAR is different from !OK so 4,4 is printed.
    """

    setOfNumbers = set()

    for index in range(len(L)):

        if (S - L[index]) in setOfNumbers:

            if L[index] < S - L[index]:
                return L[index], S - L[index]

            else:
                return S - L[index], L[index]

        setOfNumbers.add(L[index])

    return "!OK"


# Tuple isn't good for the output so I'm doing a little trick to print it

T = int(input())
for i in range(T):
    S, E = [int(n) for n in input().split()]
    L = [int(n) for n in input().split()]
    var = func(S, E, L)

    if (var != '!OK'):
        print(var[0], var[1])
    else:
        print(var)