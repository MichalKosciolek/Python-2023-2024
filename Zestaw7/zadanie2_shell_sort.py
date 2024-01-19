from mtablica import MonitorowanaTablica

def shell_sort(tablica: MonitorowanaTablica):
    n = len(tablica)
    dist = n // 2
    while dist > 0:
        for i in range(dist, n):
            tmp = tablica[i]
            j = i
            while j >= dist and tablica[j - dist] > tmp:
                tablica[j] = tablica[j - dist]
                j -= dist
            tablica[j] = tmp
        dist //= 2