def schuifer(ch, n):

    if n < 0:
        lines = ch
        for i in range(n, 0):
            lines = lines[-1:]+ lines[:-1]
        return lines

    elif n > 0:
        lines = ch
        for i in range(0, n+1):
            lines = lines[-1:]+ lines[:-1]
        return lines
    elif n == 0:
        return 'er word vandaag niet geschoven want n = 0'

ch = '1011000'
n = int(input('met welke factor wilt u verschuiven?: '))
print('begin waarde ch =', ch)
print(schuifer(ch, n))
