create-venv: clean-venv
	@echo "Creating virtual environment"
	@python3 -m venv .venv

create-folder-screenshots:
	@echo "Creating folder screenshots"
	@mkdir -p screenshots

clean-folder-screenshots:
	@echo "Removing folder screenshots"
	@rm -rf ./screenshots

install:
	@echo "Installing dependencies from the requirements.txt"
	@.venv/bin/pip3 install -r requirements.txt
	@.venv/bin/playwright install

run: create-venv create-folder-screenshots install
	@echo "Starting the script"
	@.venv/bin/python3 src/main.py

clean-venv:
	@rm -rf .venv