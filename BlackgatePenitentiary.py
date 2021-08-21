import operator


"""
    NO CREDIT

    n = number of people
    s = name (String) , h = height (int)
    
    In this question I am creating a class Person which contains name and height for every object.
    In for loop I am creating a list which contains all the villains.
    later on I am creating a new list which has sorted villains.
    in a second for loop i am checking if the current person is equal to the last person, if so
        I add their name to a string in which I'm creating.
        If not, I will print what was in the string beforehand and I will create a "new" string for 
        the next batch of people with the same height.
    at the end, whats left to do is print my string with start and end index (for the tallest person).

"""

class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height


def func(n):

    personUnsorted = []
    personSorted = []

    for i in range(n):
        s, h = input().split()
        personUnsorted.append(Person(s, int(h)))

    personSorted = sorted(personUnsorted,key=operator.attrgetter('height','name'))

    # 1,2                   2,4                 5
    # beno1 170 beno2 170 lahav1 180 lahav2 180 bar 203

    startIndex = 1
    endIndex = 1
    namesForPrint = personSorted[0].name
    for i in range(1,n):
        if(personSorted[i-1].height == personSorted[i].height):
            endIndex += 1
            namesForPrint = namesForPrint +" " +personSorted[i].name
        else:
            print(namesForPrint,startIndex,endIndex)
            startIndex = i+1
            endIndex = i+1
            namesForPrint = personSorted[i].name

    print(namesForPrint, startIndex, endIndex)


numOfPeople = int(input())
func(numOfPeople)