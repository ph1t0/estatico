VENV_DIR = ./venv
REPO_NAME = estatico

.ONESHELL:

help:
	@echo "Help:"
	@echo "	make help 		-- print this help."
	@echo "	make setup 		-- create virtualenv, install package and run flask app."
	@echo "	make dev 		-- create virtualenv, install package with -e option and run flask app."
	@echo "	make run 		-- run flask application."
	@echo "	make pages 		-- create static folder."
	@echo "	make test 		-- execute tests."
	@echo "	make clean 		-- erase virtualenv and non repo data."
	@echo ""



pages: install pager


pager:
	@echo "Running pager application."
	export FLASK_ENV=development
	source $(VENV_DIR)/bin/activate
	pager


setup: install run


dev: dev_install run


run:
	@echo "Running application."
	export FLASK_ENV=development
	source $(VENV_DIR)/bin/activate
	runapp 


dev_install: venv
	@echo "Installing package in $(VENV_DIR)"
	source $(VENV_DIR)/bin/activate
	pip install -r requirements.txt
	pip install -e .


install: venv
	@echo "Installing package in $(VENV_DIR)"
	source $(VENV_DIR)/bin/activate
	pip install -r requirements.txt
	pip install .


venv:
ifneq ("$(wildcard $(VENV_DIR))","")
	@echo "$(VENV_DIR) already exists."
else
	@echo "creating $(VENV_DIR) directory"
	python -m venv venv
endif


test:
	@echo "Running tests."
	source $(VENV_DIR)/bin/activate
	pytest -v


clean:
	@echo "Deleting: virtualenv and unnecessary dirs."
	rm -rf $(VENV_DIR) __pycache__ .pytest_cache $(REPO_NAME).egg-info $(REPO_NAME)/__pycache__ $(REPO_NAME)/public
	@echo "Unsetting Flask environment variables."
	unset FLASK_ENV

.PHONY: clean
