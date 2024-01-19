from mtablica import MonitorowanaTablica

def merge(tablica, poczatek, koniec):
    if poczatek < koniec:
        srodek = (poczatek + koniec) // 2
        merge(tablica, poczatek, srodek)
        merge(tablica, srodek + 1, koniec)

        tmp = [None] * (koniec - poczatek + 1)
        lewy = poczatek
        prawy = srodek + 1
        indeks = 0

        while lewy <= srodek and prawy <= koniec:
            if tablica[lewy] <= tablica[prawy]:
                tmp[indeks] = tablica[lewy]
                lewy += 1
            else:
                tmp[indeks] = tablica[prawy]
                prawy += 1
            indeks += 1

        while lewy <= srodek:
            tmp[indeks] = tablica[lewy]
            lewy += 1
            indeks += 1
        while prawy <= koniec:
            tmp[indeks] = tablica[prawy]
            prawy += 1
            indeks += 1

        for indeks in range(koniec - poczatek + 1):
            tablica[poczatek + indeks] = tmp[indeks]

def merge_sort(tablica: MonitorowanaTablica):
    merge(tablica, 0, len(tablica) - 1)
