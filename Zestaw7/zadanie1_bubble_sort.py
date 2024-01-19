from mtablica import MonitorowanaTablica

def bubble_sort(tablica: MonitorowanaTablica):
    for i in range(len(tablica)):
        for j in range(len(tablica)-i-1):
            if tablica[j] > tablica[j+1]:
                tablica[j], tablica[j+1] = tablica[j+1], tablica[j]
