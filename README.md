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

## Maintenance  

### Code quality

```bash 
make lint
```

### Testing

```bash
make test
```

### Releasing on PyPI

1. Update the `version` in `pyproject.toml`. We use semantic versioning
2. At the command line, run `make tag`
3. Go to [releases page](https://github.com/pydanny/listo/releases) and click `Draft a new release`


### Building the project locally

Go to the project root

```bash
pip install --upgrade build
python -m build
```

Test the project, forcing reinstall if necessary

```bash
pip install dist/listo-0.1.0-py3-none-any.whl --force-reinstall
```

