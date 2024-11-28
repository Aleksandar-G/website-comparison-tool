start-venv:
	python -m venv .venv

activate-venv:
	source env/bin/activate

install:
	pip install -r requirements.txt