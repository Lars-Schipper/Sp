import random


def check(secret, gok):
    print('secret = ', secret, 'gok = ', gok)

    if secret == gok:
        print('gefeliciteerd!!')
        return True

    elif secret != gok:


        return False

def input_secret():
    secret = input('voer je code in: ').split(',')

    while len(secret) != 4:
        secret = input('voer een geldige code van 4 cijfers in: ').split(',')

    return secret

def input_gok():
    gok = input('voer je gok in: ').split(',')

    while len(gok) != 4:
        gok = input('voer een geldige gok van 4 cijfers in: ').split(',')

    return gok

def gok_generator():
    gok = []
    for i in range(0, 4):
        gok.append(kleur_opties[random.randrange(0, 6)])

    return gok

def secret_generator():
    secret_g = []
    for i in range(0, 4):
        secret_g.append(kleur_opties[random.randrange(0, 6)])

    return secret_g


kleur_opties = ['1', '2', '3', '4', '5', '6']   #kleuren opties definiëren

# main_loop
while True:
    wie_raad = input('wil je dat de computer raad?(y/n/q)')

    if wie_raad == 'y': # de computer raad
        a = input_secret()
        i = 0
        while True:
            i += 1
            print(i)

            if check(a, gok_generator()) == True:
                break
    # ======================================================
    elif wie_raad == 'n': # ik raad

        secret = secret_generator()
        print(secret)
        while True:
            if check(secret, input_gok()) == True:
                break
    #========================================================
    elif wie_raad == 'q': #als q wordt ingevoerd eindigt het programma
        print('bedankt voor het spelen')
        break