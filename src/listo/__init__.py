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

    def first(self) -> typing.Any:
        return self[0]

    def last(self) -> typing.Any:
        return self[-1]

    def min(self) -> typing.Any:
        return min(self)

    def max(self) -> typing.Any:
        return max(self)

    def random_choice(self) -> typing.Any:
        return random.choice(self)

    @functools.cached_property
    def _length(self) -> int:
        return len(self)

    def len(self) -> int:
        return self._length

    def median(self) -> typing.Any:
        index = round((self._length - 1) / 2)
        return self[index]

    def join(self, seperator: str = " ") -> str:
        return seperator.join([str(x) for x in self])

    def shuffle(self) -> list[typing.Any]:
        return random.sample(self, self._length)

    def reverse(self) -> typing.Any:
        # Overwrite the built-in reverse method so a value is returned
        return self[::-1]


listo = Listo
