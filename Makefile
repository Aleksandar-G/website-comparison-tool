create-venv: clean-venv
	@echo "Creating virtual environment"
	@python3 -m venv .venv

install:
	@echo "Installing dependencies from the requirements.txt"
	@.venv/bin/pip3 install -r requirements.txt

run: create-venv install
	@echo "Starting the script"
	@.venv/bin/python3 src/main.py

clean-venv:
	@rm -rf .venv