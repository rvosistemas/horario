update:
	pip3-review --auto
	pip3 freeze > requirements.txt

coverage-application: 
	export COVERAGE_FILE=.coverage; pytest --cov=horario/app \
	tests/app/ --cov-report term-missing -x -s -W \
	ignore::DeprecationWarning