
"""
# T = amount of test cases
# M,N,K

# M = Number of floors in the hotel
# N = Number of rooms per floor
# K = exact number of master switches that will be turned off

    at first, I am getting M numbers from my user I'm adding them to a list.
    I am sorting my list
    I'm running with for loop on the exact number of master switches that will be turned off (K)
        during the run, I am taking everything inside my array and subtract N out of it (number of floors)
        if arr[i] is negative I'm making it positive with the same value
    I am running on an additional loop and adding everything to sum

    Sum is now the max amount of hotel rooms I can have in my hotel.
    that happends Because I have sorted my array and therefore I am treating it like
        I would treat a circle (Smallest numbers -N has the greatest value inside my array)

"""




def func(M,N,K):

    arr = []

    for i in range(M):
        inp = int(input())
        arr.append(inp)

    arr.sort()

    for i in range(K):
        arr[i] -= N;

        if(arr[i] < 0):
            arr[i] *= -1

    sum = 0
    for i in arr:
        sum += i

    return sum


T = int(input())

for i in range(T):
    M, N, K = [int(n) for n in input().split()]
    print(func(M,N,K))
