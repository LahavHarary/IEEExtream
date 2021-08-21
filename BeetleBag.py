import operator


"""
#credit: geeks for geeks, https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
    
    Class something is a class that has two attributes: weight and power.
    
    Inside my function I am getting the weight that the bag can hold and the amount of Items that I have to chose
    from.
    I am running with for loop and creating item variables (which contains the weight and fighting power) and adding
    them to a list.
    
    list is being sorted and a function named knapSack is being called.
    
     knapSack is then creating a two dim array and adds value to it in a way that the current block in which
     we are looking at is the best according to the step.
     
     at the end, knapSack return the last block (which has to be the best according to logic).

      

"""



class something:
    def __init__(self, weight, power):
        self.weight = weight
        self.power = power


def knapSack(weightOfBag, amountOfItems,items):
    K = [[0 for x in range(weightOfBag + 1)] for x in range(amountOfItems + 1)]

    # Build table K[][] in bottom up manner
    for i in range(amountOfItems + 1):
        for w in range(weightOfBag + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif items[i - 1].weight <= w:
                K[i][w] = max(items[i - 1].power+ K[i - 1][w - items[i - 1].weight],K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[amountOfItems][weightOfBag]

def func():
    weightOfBag, amountOfItems = [int(n) for n in input().split()]

    items = []

    for i in range(amountOfItems):
        weightOfItem,fightingPowerOfItem = [int(n) for n in input().split()]
        item = something(weightOfItem,fightingPowerOfItem)
        items.append(item)

    items = sorted(items, key=operator.attrgetter('weight', 'power'))

    return knapSack(weightOfBag,amountOfItems,items)

t = int(input())
for i in range(t):
    print(func())