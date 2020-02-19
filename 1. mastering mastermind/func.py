# lars schipper
import random

def check(secret, gok): #deze functie controleerd hoeveel cijfers op de juiste plek zitten en hoeveel wel in de code zitten maar niet op de juiste plek staan
    zwarte_pin = 0
    witte_pin = 0
    tijdelijk = []

    for i in range(0, len(secret)):
        tijdelijk.append(secret[i])

    for i in range(0, len(secret)):
        if secret[i] == gok[i]:
            zwarte_pin += 1
            tijdelijk.remove(gok[i])

    for i in range(0, len(secret)):
        if gok[i] in tijdelijk:
            tijdelijk.remove(gok[i])
            witte_pin += 1

    return zwarte_pin, witte_pin

def input_secret():  # deze functie vraagt om een input van de gebruiker en returt deze als secret
    secret = input('voer je code in: ').split(',')

    while len(secret) != 4:
        secret = input('voer een geldige code van 4 cijfers in: ').split(',')

    return secret

def input_gok():  #deze functie vraag om een inpupt voor de gok van de gebruiker
    gok = input('voer je gok in: ').split(',')

    while len(gok) != 4:
        gok = input('voer een geldige gok van 4 cijfers in: ').split(',')

    return gok

def gok_generator():   #deze functie genereerd een random code om als gok te gebruiken
    gok = []
    kleur_opties = ['1', '2', '3', '4', '5', '6']
    for i in range(0, 4):
        gok.append(kleur_opties[random.randrange(0, 6)])

    return gok

def secret_generator():   #deze functie genereerd een random secret voor het programma zodat de spelen kan raden
    secret_g= []
    kleur_opties = ['1', '2', '3', '4', '5', '6']
    for i in range(0, 4):
        secret_g.append(kleur_opties[random.randrange(0, 6)])

    return secret_g

def algoritme_1(secret): #deze functie is het eerste algoritme dat gebruikt kan worden om het secret van de speler te raden

    lijst = keuze_lijst()

    while len(lijst) > 1:
        i = random.randrange(0, len(lijst))
        gok = lijst[i]
        stap_1 = check(secret, gok)
        zwarte_pinnen = stap_1[0]
        witte_pinnen = stap_1[1]

        for element in lijst:
            checker = check(element, gok)
            zwarte_pinnen_gecheckt = checker[0]
            witte_pinnen_gechekt = checker[1]
            if zwarte_pinnen != zwarte_pinnen_gecheckt or witte_pinnen != witte_pinnen_gechekt:
                lijst.remove(element)


    if lijst[0] == secret:
        waarheid = 1
        return lijst, waarheid

    return False

def algoritme_2(secret):  #deze functie is het tweede algoritme dat gebruikt kan worden om het secret van de speler te raden
    print('algoritme 2')

    checker = check(secret, gok_generator())
    zwart = checker[0]
    wit = checker[1]

    print('zwart = {}, wit = {}'.format(zwart,wit))

def algoritme_3(secret):  #deze functie is het derde algoritme dat gebruikt kan worden om het secret van de speler te raden
    if secret == secret:
        return secret
    else:
        returnaa

def keuze_lijst(): #deze funtie genereerd een lijst met alle mogelijke combinaties voor de secret
    lijst = []
    kleuren = ['1','2','3','4','5','6']
    for i in kleuren:
        for j in kleuren:
            for a in kleuren:
                for b in kleuren:
                    lijst.append([i, j, a, b])

    return lijst