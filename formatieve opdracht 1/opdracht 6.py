def gemiddelde_lijst(list):
    totaal_aantal_punten = 0

    for i in list:
        totaal_aantal_punten += i

    gemiddelde = totaal_aantal_punten / len(list)
    return gemiddelde

def gemiddelde_lijst_in_lijst(list_2):
    for i in list_2:
        gemiddelde = 0

        for j in i:
            gemiddelde += j

        print('gemiddelde van lijst', i, 'is:',gemiddelde/ len(i))
    return


list = [6, 7, 8, 4, 6, 7]
list_2 = [[6,7,8,4],[9,2,3,4],[6,6,5,4]]
print(gemiddelde_lijst(list))
gemiddelde_lijst_in_lijst(list_2)