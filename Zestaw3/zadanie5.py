class Bug:

    """
    Klasa Bug przechowuje iformacje i liczniku i id owada
    """

    licznik = 0

    def __init__(self):

        """Zwieksza licznik o 1 i przypisuje id owada"""

        Bug.licznik += 1
        self.id = Bug.licznik

    def __del__(self):

        """Zmniejsza licznik o 1 i wyswietla informacje o usuwanym owadzie"""

        print('Koniec', self)
        Bug.licznik -= 1

    def __str__(self):

        """Wyswietla informacje o owadzie"""

        return f'Licznik: {self.licznik}, Id: {self.id}'

bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])