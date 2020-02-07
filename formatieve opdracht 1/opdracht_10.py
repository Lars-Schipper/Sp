# met behulp van https://www.programiz.com/python-programming/examples/fibonacci-recursion

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n - 1)+ fibonacci(n - 2))

n = int(input('van welke factor wilt u de fibonacci waarde: '))
print('de term op plek,', n, 'heeft de waarde:',fibonacci(n), 'in de fibanacci reeks')