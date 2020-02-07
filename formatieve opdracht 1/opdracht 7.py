from random import *

random_getal = randint(0,10)
print(random_getal)

while True:

    geraden_getal = int(input('welk getal wilt u raden: '))

    if geraden_getal == random_getal:
        print('GEFELICITEERD u heeft hetgetal geraden!!!')
        break

    else:
        print('helaas probeer het nogeens')