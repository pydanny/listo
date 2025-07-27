# Contributing to Listo

## Development

Install the package in editable mode with test dependencies:

```bash
pip install -e '.[test]'
```

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

### Code quality

```bash 
make lint
```

### Testing

```bash
make test
```

### Releasing a New Version

Change the version number in `pyproject.toml`.

Regenerate the lockfile:

```bash
uv lock
```

Commit the changes:

```sh
git commit -am "Release version x.y.z"
```

Tag the release and push to github:

```sh
make tag
```

This will deploy the new package to PyPI. 

Check https://pypi.org/project/listo and confirm that the new version number shows there.

Finally, create a new release on GitHub:

* Create a new release on GitHub by clicking "Create a new release"
* From the tag dropdown, choose the tag you just created
* Click "Generate release notes" to auto-populate the release notes
* Copy in whatever notes you have from the `CHANGELOG.md` file
* Revise the notes as needed
* Click "Publish release"