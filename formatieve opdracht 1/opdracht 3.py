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

print('====opdracht A====')
str = input('voer een string van nummers in: ')
getal = input('welk getal wil je de frequentie van weten?: ')
print(count(str, getal))

print('====opdracht B====')
lst = [0, 4, 6, 8, 10, 0]
print('het grootste verschil in de lijs:', lst, 'is:', verschil_in_lijst(lst))

print('====opdracht C====')
lst2 = [1,0,0,1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1,1]
if lijst_check(lst2) == True:
    print('de lijst:', lst2, 'voldoet wel aan de voorwaarden')
elif lijst_check(lst2) == False:
    print('de lijst:', lst2, 'voldoet niet aan de voorwaarde')