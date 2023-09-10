lint:
	black .
	ruff check . --fix

VERSION=$(shell grep -m 1 version pyproject.toml | tr -s ' ' | tr -d '"' | tr -d "'" | cut -d' ' -f3)

tag:
	echo "Tagging version $(VERSION)"
	git tag -a $(VERSION) -m "Creating version $(VERSION)"
	git push origin $(VERSION)


test:
	coverage run -m pytest .
	coverage report -m
	coverage html
