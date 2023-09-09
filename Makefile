lint:
	black .
	ruff check . --fix

test:
	pytest .
