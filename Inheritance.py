class animals:
    def __init__(organism, legs, feathers, milk):

        organism.nolegs = legs
        organism.feathers = feathers
        organism.milks = milk

    def __init__(living, legs, feathers, milk):
        living.nolegs = legs
        living.feathers = feathers
        living.milks = milk

    def printme(organism):
        print("organism has", organism.nolegs, " legs have feathers", organism.feathers, "is milk giving",organism.milks)

    def printme(living):

        print("living has", living.nolegs, " legs have feathers", living.feathers, "is milk giving", living.milks)
class birds(animals):
    pass

class memmal(animals):
    pass
x= birds(2,True,False)
x.printme()
y= memmal(4,False,True)
y.printme()