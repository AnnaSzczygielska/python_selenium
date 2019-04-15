.PHONY: test

deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt

lint:
	flake8 wizzair_test.py

test:
	PYTHONPATH=. py.test wizzair_test.py  --verbose -s
