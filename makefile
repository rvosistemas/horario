PROJECT = horario
COVFILE ?= .coverage

clean-cache:
	find . -name '__pycache__' -exec rm -fr {} +
	rm -rf ./.cache .mypy_cache ./schema/.mypy_cache .coverage

clean-pyc:
	find . -name "*.pyc" -exec rm -rf {} \;

test:
	pytest

update:
	pip3-review --auto
	pip3 freeze > requirements.txt

coverage-app: 
	export COVERAGE_FILE=$(COVFILE); pytest --cov=$(PROJECT)/app \
	tests/app/ --cov-report term-missing -x -s -W \
	ignore::DeprecationWarning -o cache_dir=/tmp/horario/cache

coverage-infrastructure: 
	export COVERAGE_FILE=$(COVFILE); pytest --cov=$(PROJECT)/infrastructure \
	tests/infrastructure/ --cov-report term-missing -x -s -W \
	ignore::DeprecationWarning -o cache_dir=/tmp/horario/cache

coverage: 
	export COVERAGE_FILE=$(COVFILE); pytest --cov=$(PROJECT) tests/ \
	--cov-report term-missing -x -s -vv -W ignore::DeprecationWarning \
	-o cache_dir=/tmp/horario/cache

serve:
	python -m $(PROJECT) serve

serve-dev:
	export horario_MODE=DEV; python -m $(PROJECT) serve

deploy:
	./setup/deploy.sh
	
PART ?= patch

version:
	bump2version $(PART) $(PROJECT)/__init__.py --tag --commit

dev-deploy:
	 bin/dev_deploy.sh