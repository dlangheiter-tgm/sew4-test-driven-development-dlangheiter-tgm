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

        :raises TypeError: When it is not an Integer or Bruch
        """
        if isinstance(other, int):
            return Bruch(other * self.nenner + self.zaehler, self.nenner)
        if isinstance(other, Bruch):
            return Bruch(self.zaehler * other.nenner + other.zaehler * self.nenner , other.nenner * self.nenner)
        raise TypeError("Addition only permitet with integers and Bruch")

    def __radd__(self, other):
        """ Radd-Operator

        :raises TypeError: When it is not an Integer or Bruch
        :param other: The object to add to
        :return: The added Bruch
        """
        return self + other

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
        if self.nenner == 1:
            return "(%i)" % self.zaehler

        if self.zaehler < 0 and self.nenner < 0:
            return "(%i/%i)" % (-self.zaehler, -self.nenner)
        return "(%i/%i)" % (self.zaehler, self.nenner)

    def __eq__(self, other):
        """ Equal method

        :param other: Param to check if equal
        :return: return if they are equal
        """
        if isinstance(other, Bruch):
            return self.nenner == other.nenner and self.zaehler == other.zaehler
        return False

    def __ge__(self, other):
        """ Greater or equals

        :param other: variable to compare to
        :return: If it is greater or equals
        """
        return float(self) >= float(other)

    def __gt__(self, other):
        """ Greater than

        :param other: variable to compare to
        :return: If it is greater than
        """
        return float(self) > float(other)

    def __le__(self, other):
        """ Less or equals

        :param other: variable to compare to
        :return: If it is less or equals
        """
        return float(self) <= float(other)

    def __lt__(self, other):
        """ Less than

        :param other: variable to compare to
        :return: If it is less than
        """
        return float(self) < float(other)

    def __ne__(self, other):
        """ Not equals

        :param other: variable to compare to
        :return: If it is not equals
        """
        return not (self == other)

    def __abs__(self):
        """ Returns the absolute of the Bruch

        :return: a Bruch that is the absoloute
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __invert__(self):
        """ Invert the Bruch

        :return: The inverted Bruch
        """
        return Bruch(self.nenner, self.zaehler)

    def __neg__(self):
        """ Makes the negative of the Bruch

        :return: The negative
        """
        return Bruch(-self.zaehler, self.nenner)

    def __pow__(self, power, modulo=None):
        """ Pow function

        :param power: To the power off
        :param modulo: IDK
        :return: The raised Bruch
        """
        return Bruch(pow(self.zaehler, power, modulo), pow(self.nenner, power, modulo))


