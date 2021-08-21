def Fibonacci(t):

    """
    Notes for exam: I've read about the fibo pattern in: https://www.jain108.com/fibonacci-60-code/
    So the credit goes there.

    I have tried to calculate this fibo sequence with recursion, it didin't work well (Slow).
    I have tried to use dynamic programming principles and it was too slow also.

    After I almost gave up  I've read online that a sequence of numbers in the regular fibo series is
    repeating itself.
    I've decided to use that info to make an array of 60 numbers and try it out here.
    I have calculated manually every number in our fibo series and then In the running process

    In order to get the correct answer I am getting a number from our user, I need to match that number
        inside my arr (because it starts from 0) so I take the number and subtract 1 from it.
        that allows me to get the position inside my arr.
        I am using modulo 60 and calling Fibonacci function.
    """


    fib_series = [1, 2, 3, 5, 8, 3, 1, 4, 5, 9,
                  4, 3, 7, 0, 7, 7, 4, 1, 5, 6,
                  1, 7, 8, 5, 3, 8, 1, 9, 0, 9,
                  9, 8, 7, 5, 2, 7, 9, 6, 5, 1,
                  6, 7, 3, 0, 3, 3, 6, 9, 5, 4,
                  9, 3, 2, 5, 7, 2, 9, 1, 0, 1]

    return fib_series[t]


amount_of_test_cases = int(input())

for i in range(amount_of_test_cases):
    gen = int(input()) - 1
    print((Fibonacci(gen % 60)))
