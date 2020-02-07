# met behulp van https://stackoverflow.com/questions/11964450/python-order-a-list-of-numbers-without-built-in-sort-min-max-function

def list_sort(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):

            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]

    return list

list = [0,3,4,1,2,6,7,3,8,10,0]
print('ongesorteerde lijst: ', list)
print('gesorteerde lijst:   ', list_sort(list))
