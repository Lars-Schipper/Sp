def forpyramide(n):
    print('===met for loop===')

    # mylist = []
    for i in range(n+1):
        print(i*'*')
    for j in reversed((range(n))):
        print(j*'*')

def whilepyramide(n):
    print('===met while loop===')
    counter = 0
    while counter in range(n):
        counter += 1
        print(counter*'*')

    counter2 = n
    while counter2 in (range(n+1)):
        counter2 -= 1
        print(counter2*'*')

def omgekeerdepyramide(n):
    print('===omgekeerd===')

    for i in range(n + 1):
        print((n - i)* ' '+ i * '*')
    for i in reversed(range(n)):
        print((n-i) * ' '+ i * '*')

n = int(input('hoe groot wil je de pyramide?: '))
forpyramide(n)
whilepyramide(n)
omgekeerdepyramide(n)
