.PHONY: mypy
mypy:
	mypy .

.PHONY: black
black:
	black .

.PHONY: flake8
flake8:
	flake8 .

.PHONY: isort
isort:
	isort .

.PHONY: ci
ci: mypy black isort flake8
