from mtablica import MonitorowanaTablica

def quick_sort(tablica: MonitorowanaTablica):
    quick_sort_recursive(tablica, 0, len(tablica) - 1)

def podziel(tablica, poczatek, koniec):
    pivot = tablica[koniec]
    indeks = poczatek

    for pozycja in range(poczatek, koniec):
        if tablica[pozycja] <= pivot:
            tablica[indeks], tablica[pozycja] = tablica[pozycja], tablica[indeks]
            indeks += 1

    tablica[indeks], tablica[koniec] = tablica[koniec], tablica[indeks]

    return indeks

def quick_sort_recursive(tablica, poczatek, koniec):
    if poczatek < koniec:
        indeks_pivot = podziel(tablica, poczatek, koniec)
        quick_sort_recursive(tablica, poczatek, indeks_pivot - 1)
        quick_sort_recursive(tablica, indeks_pivot + 1, koniec)
