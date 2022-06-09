install:
	pip install -r requirements.txt

pylint:
	pylint ./*/**.py --ignore-paths=venv/ --extension-pkg-whitelist='pydantic'

black:
	black .
