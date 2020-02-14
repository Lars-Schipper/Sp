def check(secret, gok):
    print('secret = ', secret, 'gok = ', gok)
    zwarte_pin = 0
    witte_pin = 0
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
