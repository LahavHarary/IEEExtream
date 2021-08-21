from math import ceil


"""
W = Width of bathroom wall
H = Height of bathroom wall
A = width of mosaic tile
B = height of mosaic tile
M = pile of 10 mosaic tiles cost
C = pay for the worker per inch of the work (Cutting).

    At first, I'm declaring two variables that are the "REAL" amount of tiles that needed (for width and height).
    Later on, I'm creating two variables that store the rounded amount (Ceiling). 
    Another variable named amount of tiles bought is added, I calculate him with with roundedHeight * roundedWidth.
    
    I need to round amount of tiles bought so I'm running on a while loop until it can be divided nicely by ten.
    
    I am calculating the amount of dollars spend on tiles (taking the amount of tiles divided them by 10 and 
    then multiply them by M (the cost per batch of tiles).
    
    Now in order to return the correct amount of money I have too check if the worker needed to cut my tiles.
    In order to do so I am checking if the rounded is equal to the real if so, then no cutting was needed
    but if they aren't equal it means that some cutting was needed.
        Cutting calculations are:
        Width of bathroom wall * pay for the worker per inch of the work (Cutting)
        And / Or: 
        Height of bathroom wall * pay for the worker per inch of the work (Cutting).
    
    last, I return the total amount (work cost and tiles cost).
    


"""

def MoasicDecorationTwo(W, H, A, B, M, C):
    amount_tiles_to_buy_for_width_real_size = W / A
    amount_tiles_to_buy_for_height_real_size = H / B

    amount_tiles_to_buy_for_width_rounded = ceil(amount_tiles_to_buy_for_width_real_size)
    amount_tiles_to_buy_for_height_rounded = ceil(amount_tiles_to_buy_for_height_real_size)

    amount_of_tiles_bought = (amount_tiles_to_buy_for_width_rounded * amount_tiles_to_buy_for_height_rounded)
    while (amount_of_tiles_bought % 10 != 0):
        amount_of_tiles_bought += 1

    amount_of_dollars_spend_on_tiles = (amount_of_tiles_bought / 10) * M

    work_price = 0
    if (amount_tiles_to_buy_for_width_real_size != amount_tiles_to_buy_for_width_rounded):
        work_price += H * C
    if (amount_tiles_to_buy_for_height_real_size != amount_tiles_to_buy_for_height_rounded):
        work_price += W * C

    return work_price + amount_of_dollars_spend_on_tiles


W, H, A, B, M, C = [int(n) for n in input().split()]
print(int(MoasicDecorationTwo(W, H, A, B, M, C)))