# listo

Description and usage coming soon

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

