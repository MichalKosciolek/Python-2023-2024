input_list = input('Lista: ').split()
range_list = input('Zakres: ').split()
left = int(range_list[0])
right = int(range_list[1])

if left > right:
    print('Bledny zakres')
    exit(1)

def odwracanie(L, left, right):
    Lista = L.copy()
    if left > right:
        return Lista
    Lista[left:right+1] = Lista[left:right+1][::-1]
    return Lista

def odwracanie_recursive(L, left, right):
    Lista = L.copy()
    if left > right:
        return Lista
    Lista[left], Lista[right] = Lista[right], Lista[left]
    return odwracanie_recursive(Lista, left+1, right-1)

print('Wersja iteracyjna: ', odwracanie(input_list, left, right))
print('Wersja rekurencyjna: ', odwracanie_recursive(input_list, left, right))