# listo

Listo is an enhanced version of the `list` type that aims to do the following:

- Make behavior more consistent. No more methods with "in-place" changes. Every method call returns a value
- Adds methods that are missing from the `list` type. For example, `listo` has a `first` method that returns `self[0]`
- A list of arguments passed in will be converted to a `listo` object, but a single argument that is an iterator will be unpacked into a `listo` object. This is useful for when you want to pass in a generator or other iterator into a function that expects a list

## Usage

First install it via pip, poetry, or whatever you use

```bash
pip install listo
```

Then use it in your code

```python
from listo import listo

lst = listo(1, 2, 3)
assert lst.first() == 1
assert lst.last() == 2
```

### Usage: How listo handles initial arguments

For arguments passed in, it just converts them to a `listo` object

```python
lst = listo(1, 2, 3)
assert lst == [1, 2, 3]

lst2 = listo([1, 2, 3]) # list is unpacked
assert lst2 == [1, 2, 3]

lst3 = listo((1, 2, 3)) # tuple is converted and unpacked
assert lst3 == [1, 2, 3]

lst4 = listo([1, 2, 3], (1, 2))  # Two args mean nothing is unpacked
assert lst4 == [[1, 2, 3], (1, 2)]
```

This is different from standard Python iterator behavior.

### Contributing to Listo

Have you tried using Listo and found it useful? Do you have ideas for how to make it better? 

We welcome contributions from the community!

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to set up your development environment to contribute to this project, run tests, check code quality, release new versions, and more.
