.PHONY: test
test:
	cd service && python -m pytest ../tests

.PHONY: mypy
mypy:
	mypy service

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
ci: mypy black isort flake8 test
