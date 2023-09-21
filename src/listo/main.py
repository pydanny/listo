import collections
import functools
import random
import typing


class Listo(list):  # type: ignore [type-arg]
    """
    Rules:
        1. Every method must return something
        2. Cached properties must call a function and be prefixed with '_'
    """

    def __init__(self, *args: typing.Any) -> None:
        # If the first argument is an iterable, unpack it
        if len(args) == 1 and isinstance(args[0], collections.abc.Iterable):
            self.extend(list(args[0]))
        else:
            self.extend(list(args))

    @functools.cached_property
    def _length(self) -> int:
        # Returns caached length of the listo
        return len(self)

    def first(self) -> typing.Any:
        return self[0]

    def join(self, seperator: str = " ") -> str:
        # Replicates str.join()
        return seperator.join([str(x) for x in self])

    def last(self) -> typing.Any:
        return self[-1]

    def len(self) -> int:
        # Returns the length of the listo
        return self._length

    def max(self) -> typing.Any:
        return max(self)

    def median(self) -> typing.Any:
        # Provides the median value, rounding up
        index = round((self._length - 1) / 2)
        return self[index]

    def min(self) -> typing.Any:
        return min(self)

    def random_choice(self) -> typing.Any:
        # Randomly returns a value from the listo
        return random.choice(self)

    def reverse(self) -> typing.Any:
        # Overwrites the built-in reverse method so a value is returned
        return self[::-1]

    def shuffle(self) -> list[typing.Any]:
        # Shuffles and resits the listo
        return random.sample(self, self._length)

    reverse.__doc__ = "Overwrites the built-in reverse method so a value is returned"


listo = Listo
