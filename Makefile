.PHONY: install virtualenv ipython clean

install:
	@echo "Installing for dev env"
	@.venv/Scripts/python -m pip install -e.['dev']
venv:
	@source .venv/Scripts/activate

virtualenv:
	@python -m pip -m venv .venv

ipython:
	@.venv/Scripts/ipython

test:
	@.venv/Scripts/pytest -vv -s tests/

watch:
	@.venv/Scripts/ptw -- -vv -s tests/

clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build