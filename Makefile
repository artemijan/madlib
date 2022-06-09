install:
	pip install -r requirements.txt

pylint:
	pylint ./*/**.py

black:
	black .
