name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict( list1, list2 ):
    new_dict = {}
    interimZip = zip( list1, list2 )
    new_dict = dict( interimZip )
    print new_dict
    return new_dict

make_dict( name, favorite_animal )