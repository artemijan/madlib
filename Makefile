install:
	pip install -r requirements.txt

pylint:
	pylint --load-plugins pylint_django --django-settings-module=shop.settings madlib/*

black:
	black madlib/*
