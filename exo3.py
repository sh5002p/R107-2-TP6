def ajouter_elt(lst=[0,1,2], elt=3):
    print({id(lst)})
    print(lst)
    lst.append(elt)
    print({id(lst)})
    return lst
def ajouter_carac(ch="abc", elt="d"):
    print({id(ch)})
    ch += elt
    print({id(ch)})x
    return ch

print(ajouter_elt())
print(ajouter_carac())