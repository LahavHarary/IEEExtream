
"""
N Bathrooms
Two colors: Black and Pink
The *i*th bathroom needs Bi black tiles and Pi pink tiles
Moasic tiles are sold in piles of 10:
10 black tiles cost CB dollars
10 ping tiles cost CP dollars
How much money does he need in total to decorate all N bathrooms

    I am starting this question with two variables , "amountB" and "amountC"
    with a different variable named newAmountOfTiles(B and C) I am getting each one of the bathrooms
    need for tiles and adding them to "amountB" and "amountC"
    The problemn with this question is that I have to "ROUND UP" the amount of tiles needed
        so after I have the sum of tiles needed for the entire room (black / pink) I am using two seperate
        while loops that add to amountB and amountC until they can be divided nicely by ten.

    what is left to do is return the calculation (amountOfTiles for each one of the room * amount
    of money each batch of tiles cost divided by ten (the amount of tiles inside a batch)).
"""


def MosaicDecorationOne(N, CB, CP):
    AmountOfTilesNeededB = 0
    AmountOfTilesNeededC = 0

    for i in range(N):
        newAmountTilesB, newAmountTilesC = [int(n) for n in input().split()]
        AmountOfTilesNeededB += newAmountTilesB
        AmountOfTilesNeededC += newAmountTilesC

    while (AmountOfTilesNeededB % 10 != 0):
        AmountOfTilesNeededB += 1

    while (AmountOfTilesNeededC % 10 != 0):
        AmountOfTilesNeededC += 1

    return int((AmountOfTilesNeededC * CP / 10) + (AmountOfTilesNeededB * CB / 10))


N, CB, CP = [int(n) for n in input().split()]
print(MosaicDecorationOne(N, CB, CP))