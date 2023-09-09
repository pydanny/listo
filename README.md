# listo

Description and usage coming soon

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
