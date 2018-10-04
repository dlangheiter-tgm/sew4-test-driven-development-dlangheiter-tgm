import math

class Bruch(object):

    def __init__(self, zaehler=None, nenner=None):
        """ Konstruktor

        :param zaehler: Zaehler des Bruchs
        :param nenner: Nenner des Bruchs
        :raises ZeroDivisionError: Wenn Nenner 0 ist, kann kein Bruch berechnet werden!
        """
        if isinstance(zaehler, int) and isinstance(nenner, int):
            """ Klassenaufruf: Bruch(2,4)
            """
            if nenner != 0:
                self.zaehler = zaehler
                self.nenner = nenner
            elif zaehler < 0 and nenner < 0:
                self.zaehler = abs(zaehler)
                self.nenner = abs(nenner)
            else:
                raise ZeroDivisionError("Division durch 0 nicht definiert!")

        elif isinstance(zaehler, Bruch):
            """ Klassenaufruf: self.b2 = Bruch(self.b)
                --> Zuweisen von Zaehler und Nenner aus dem Bruchobjekt
            """
            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner

        elif isinstance(zaehler, int) and not isinstance(nenner, float):
            """ Klassenaufruf: Bruch(4)
                --> ohne Nenner, daher Deklarierung von Nenner = 1
            """
            self.zaehler = zaehler
            self.nenner = 1

        else:
            raise TypeError("Zaehler und/oder Nenner nicht zulaessig!")

    def __add__(self, other):
        """ Add-Operator

        :raises TypeError: Wenn float übergeben wird
        """
        if isinstance(other, float):
            raise TypeError("Rationale Zahlen sind bei Bruchadditionen nicht erlaubt!")
        pass

    def __float__(self):
        """ Convert to float

        :return: Float number
        """
        return float(self.zaehler) / float(self.nenner)

    def __int__(self):
        """ Convert to int

        :return: Integer number
        """
        return math.floor(float(self))

    def __str__(self):
        """ Converts to string

        :return: String representation of Bruch
        """
        if self.zaehler < 0 and self.nenner < 0:
            return "(%i/%i)" % (-self.zaehler, -self.nenner)
        return "(%i/%i)" % (self.zaehler, self.nenner)
