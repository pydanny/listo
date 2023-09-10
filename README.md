# listo

Listo is an enhanced version of the `list` type that aims to do the following:

- Make behavior more consistent. No more methods with "in-place" changes. Every method call returns a value
- Adds methods that are missing from the `list` type. For example, `listo` has a `first` method that returns `self[0]`

## Usage

First install it via pip, poetry, or whatever you use

```bash
pip install listo
```

Then use it in your code

```python
from listo import listo

lst = listo(1, 2, 3)
lst.first() # 1
lst.last() # 3
```

## Code quality stuff

```bash 
black .
ruff check . --fix
```


## Building the project

Go to the project root

```bash
pip install --upgrade build
python -m build
```

Test the project, forcing reinstall if necessary

```bash
pip install dist/listo-0.1.0-py3-none-any.whl --force-reinstall
```

## Uploading releases to PyPI

```bash
pip install --upgrade twine
python -m twine upload  dist/*
```
