import functools
import random


class Listo(list):
    """
    Rules:
        1. Every method must return something
        2. Cached properties must call a function and be prefixed with '_'
    """

    def __init__(self, *args):
        self.extend(list(args))

    def first(self):
        return self[0]

    def last(self):
        return self[-1]

    def min(self):
        return min(self)

    def max(self):
        return max(self)

    def random(self):
        return random.choice(self)

    @functools.cached_property
    def _length(self):
        return len(self)

    def len(self):
        return self.length

    def median(self):
        index = round((self._length - 1) / 2)
        return self[index]

    def join(self, seperator: str = " "):
        return seperator.join([str(x) for x in self])

    def shuffle(self):
        return random.sample(self, self._length)

    def reverse(self):
        # Overwrite the built-in reverse method so a value is returned
        return self[::-1]


listo = Listo

if __name__ == "__main__":
    lst = listo(1, 2, 3, 4)
    print(lst.first())
    print(lst.last())
    print(lst.min())
    print("random", lst.random())
    print("median", lst.median())
    print("Join", lst.join("-"))
    print("shuffle", lst.shuffle())

    lst2 = listo("two", "one", "three", "four")
    print("random2", lst2.random())
    print("median2", lst2.median())
    print("join2", lst2.join("+"))
    print("shuffle", lst2.shuffle())

    print("type", type(lst))
    print("type", type(lst2))
