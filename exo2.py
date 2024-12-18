def ajouter_elt(lst1):
    lst2 = lst1[::]
    lst2.append(len(lst1))
    print(lst1)
    print(type(lst1))
    print({id(lst1)})
    print(lst2)
    print(type(lst2))
    print({id(lst2)})
    return lst2

ajouter_elt([1,  2, 3])