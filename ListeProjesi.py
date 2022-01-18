# PROJE: 1. 
""" https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists 
linkinde verilen örneklerden yararlanılmıştır.
"""
def listeDuzlestir(liste):
    su_tip_veri_haric = str, bytes
    for i in liste:
        try:
            if isinstance(i, su_tip_veri_haric):
                raise TypeError
            iter(i)
        except TypeError:
            yield i
        else:
            yield from listeDuzlestir(i)

    
dizi = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
sonuc = list(listeDuzlestir(dizi))
print(sonuc)


# PROJE: 2.
def ilk(li):
    li.sort(reverse=True)
    return li[0]

def listeyiSırala(liste):
    liste.sort(key=ilk, reverse=True)
    return liste

dizi2 = [[1, 2], [3, 4], [5, 6, 7]]
print(listeyiSırala(dizi2))