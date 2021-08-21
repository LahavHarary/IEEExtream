
"""
In this question I'm looking for the "Minimum walking distance" between leaves inside my tree

q = amount of test cases

a,b = Two numbers that for them I have to find the min distance.

    At first, I determine which one out of a and b is the max and the min.
    I'm creating a steps variable and I am running with a while loop (as long as min is defferent then max).
        The Condition for the while loop helps me with the case that a is equal to b at the beggining.
        inside the loop if max is greater then min I will devide (integer devision) max by 2 and steps will grow
        by 1.
        if min is greater then max then I will do the same

        the logic behind that is like looking at the tree and going backwards step by step with the greater
        out of the two leaves until they are the same.

    after the while loop we have our answer and we can return it.


"""


def function():
    a,b = [int(n) for n in input().split()]

    max = a
    min = b
    if(a < b):
        max = b
        min = a

    steps = 0
    while min != max:
        if max > min:
            max = max // 2
            steps += 1
        if min > max:
            min = min // 2
            steps += 1


    print(steps)



q = int(input())
for i in range(q):
    function()