install:
	pip install -r requirements.txt

pylint:
	find . -type d \( -path ./venv -o -path ./virtualenv -o -path ./lib \) -prune -o -iname '*.py' -print | xargs pylint

black:
	black .
test:
	pytest

docker-build:
	docker build . -t fastapi:latest
