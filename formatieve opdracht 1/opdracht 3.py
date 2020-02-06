def count(str, getal):
    counter = 0
    for i in str:
        if i == getal:
            counter += 1
    return counter


def verschil_in_lijst(lst):
    diff = 0
    for i in lst:
        if abs(lst[lst.index(i)] - lst[lst.index(i)+ 1]) > diff:
            diff = abs(lst[lst.index(i)] - lst[lst.index(i)+ 1])
    return diff

def lijst_check(lst):
    aantal_nullen = count(lst, 0)
    aantal_eenen  = count(lst, 1)

    if aantal_eenen > aantal_nullen and aantal_nullen <= 12:
        return True
    else:
        return False


# str = input('voer een string van nummers in: ')
# getal = input('welk getal wil je de frequentie van weten?: ')
# lst = [0, 4, 6, 8, 10, 0]
lst2 = [1,0,0,1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1]
# print(count(str, getal))
# print(verschil_in_lijst(lst))
if lijst_check(lst2) == True