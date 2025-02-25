create-venv: clean-venv
	@echo "Creating virtual environment"
	@python3 -m venv .venv

create-folder-contents:
	@echo "Creating folder contents"
	@mkdir -p contents
	@mkdir -p differences

clean-folder-contents:
	@echo "Removing folder contents"
	@rm -rf ./contents
	@rm -rf ./differences

install:
	@echo "Installing dependencies from the requirements.txt"
	@.venv/bin/pip3 install -r requirements.txt
	@.venv/bin/playwright install

run: create-venv clean-folder-contents create-folder-contents install
	@echo "Starting the script"
	@.venv/bin/python3 src/main.py

clean-venv:
	@rm -rf .venv