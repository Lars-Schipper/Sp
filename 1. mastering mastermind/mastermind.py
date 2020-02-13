import random


def check(secret, gok):
    print('secret = ', secret, 'gok = ', gok)
    return




kleur_opties = ['1', '2', '3', '4', '5', '6']

while True:
    wie_raad = input('wil je dat de computer raad(y/n/q): ')

    if wie_raad == 'y': # de computer raad
        secret = input('voer je code in: ').split(',')

        gok = []

        for i in range(0, 4):
            gok.append(kleur_opties[random.randrange(0,6)])

        check(secret, gok)

    elif wie_raad == 'n': # ik raad
        print('ik raad')

    elif wie_raad == 'q':
        print('bedankt voor het spelen')
        break