shoppingList = ['apples', 'bananas', 'tofu', 'cake']
emptyList = []
pets = ['cat', 'bat', 'dog']


def commaCode(list):
    for i in list[:-1]:
        print(i + str(','), end= ' ')
        if i == list[-2]:
            print(str('and ') + list[-1])
            

commaCode(pets)
