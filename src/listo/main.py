import collections
import functools
import random
import typing
from typing import TYPE_CHECKING, Callable, TypeVar

if TYPE_CHECKING:
    pass

T = TypeVar("T")
U = TypeVar("U")


class Listo(list):  # type: ignore [type-arg]
    """A list subclass that allows method chaining by returning Listo instances."""

    def __init__(self, *args: typing.Any) -> None:
        # If the first argument is an iterable, unpack it
        if len(args) == 1 and isinstance(args[0], collections.abc.Iterable):  # ty: ignore [unresolved-attribute]
            self.extend(list(args[0]))
        else:
            self.extend(list(args))

    @functools.cached_property
    def _length(self) -> int:
        # Returns cached length of the listo
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

    def shuffle(self) -> "Listo[T]":
        # Shuffles and returns the listo
        return random.sample(self, self._length)

    def map(self, func: Callable[[T], U]) -> "Listo[U]":
        """Apply a function to each element and return a new Listo."""
        return Listo(map(func, self))

    def filter(self, func: Callable[[T], bool]) -> "Listo[T]":
        """Filter elements based on a predicate function and return a new Listo."""
        return Listo(filter(func, self))

    def unique(self) -> "Listo[T]":
        """Return a new Listo with unique elements (preserving order)."""
        seen = set()
        result = []
        for item in self:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return Listo(result)

    reverse.__doc__ = "Overwrites the built-in reverse method so a value is returned"

    def __repr__(self):
        return 'I am a listo'


listo = Listo
