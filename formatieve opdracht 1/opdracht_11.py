# met behulp van https://gist.github.com/jameslyons/8701593



def caesar_cijfers(tekst, key):
    L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
    I2L = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    cijfertext = ""
    for c in tekst.upper():
        if c.isalpha():
            cijfertext += I2L[(L2I[c] + key) % 26]
        else:
            cijfertext += c
    return cijfertext

tekst = input('geef een tekst: ')
key = int(input('geef een rotatie: '))

print(caesar_cijfers(tekst, key))


