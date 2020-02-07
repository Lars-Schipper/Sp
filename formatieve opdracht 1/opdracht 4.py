# in samen werking met gerrit van de Bunt

def palidroom_check_zonder_library(woord):
    if str(woord) == str(woord)[::-1]:
        return True
    else:
        return False

def palidroom_check_met_library(woord):
    revlist = list(reversed(woord))
    revstr = str()

    for i in revlist:
        revstr += i
    if revstr == woord:
        return True
    else:
        return False



woord = input('welk woord wil je checken of het een palidroom is?: ')
print('==== zonder library ====')
if palidroom_check_zonder_library(woord) == True:
    print('het woord', woord, 'is een palidroom')
else:
    print('het woord', woord, 'is geen palidroom')

print('==== met library ====')
if palidroom_check_met_library(woord) == True:
    print('het woord', woord, 'is een palidroom')
else:
    print('het woord', woord, 'is geen palidroom')