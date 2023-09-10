import collections
import functools
import random


class Listo(list):
    """
    Rules:
        1. Every method must return something
        2. Cached properties must call a function and be prefixed with '_'
    """

    def __init__(self, *args):
        # If the first argument is an iterable, unpack it
        if len(args) == 1 and isinstance(args[0], collections.abc.Iterable):
            args = args[0]
        self.extend(list(args))

    def first(self):
        return self[0]

    def last(self):
        return self[-1]

    def min(self):
        return min(self)

    def max(self):
        return max(self)

    def random_choice(self):
        return random.choice(self)

    @functools.cached_property
    def _length(self):
        return len(self)

    def len(self):
        return self._length

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
