
"""
    BASE:
    I am taking From the bigger out of J and K 2 and from the smaller of them I take 1.
    That way each one of the girls can rap or something.
    Counter is getting bigger by one in this case.
    If k and j are equal then I divide by 3 the sum of them (which makes the process a lot faster).

    Base case was mathematically correct but the test for this question doesn't have a lot of time.
    So I usde a lot of while loops with greater number and made the same calculation.

"""

def func():
    K, J = [int(n) for n in input().split()]
    counter = 0

    while K >= 100000 and J >= 100000:
        if K > J:
            K -= 20000
            J -= 10000
            counter += 10000
        else:
            K -= 10000
            J -= 20000
            counter += 10000

    while K >= 10000 and J >= 10000:
        if K > J:
            K -= 2000
            J -= 1000
            counter += 1000
        elif K < J:
            K -= 1000
            J -= 2000
            counter += 1000
        else:
            counter += int((K+J) / 3)
            K = 0
            J = 0

    while K >= 1000 and J >= 1000:
        if K > J:
            K -= 200
            J -= 100
            counter += 100
        elif K < J:
            K -= 100
            J -= 200
            counter += 100
        else:
            counter += int((K+J) / 3)
            K = 0
            J = 0

    while K >= 100 and J >= 100:
        if K > J:
            K -= 20
            J -= 10
            counter += 10
        elif K < J:
            K -= 10
            J -= 20
            counter += 10
        else:
            counter += int((K+J) / 3)
            K = 0
            J = 0

    while K >= 1 and J >= 1:
        if K > J:
            K -= 2
            J -= 1
            counter += 1
        elif K < J:
            K -= 1
            J -= 2
            counter += 1
        else:
            counter += int((K+J) / 3)
            K = 0
            J = 0

    return counter


print(func())