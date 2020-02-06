def vergelijker(string1, string2):
    if string1 == string2:
        print('er is geen verschil tussen de strings')
        return

    if string1 != string2:
        if len(string1) > len(string2):
            for x in range(0, len(string1)+ 1):
                if string1[x] != string2[x]:
                    print('de strings verschillen vanaf index:', x)
                    break

        if len(string1) < len(string2):
            for x in range(0, len(string2)+ 1):
                if string1[x] != string2[x]:
                    print('de strings verschillen vanaf index:', x)
                    break
        return

string1 = input('geef een string: ')
string2 = input('geef een string: ')
vergelijker(string1,string2)
