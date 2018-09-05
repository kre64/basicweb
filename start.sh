#!/bin/bash
# Check for dependencies && start the flask app

if pip3 list | grep Flask; then
	echo All dependencies met!
	echo Starting the application.
	python init_db.py
	echo Database initialized with "python init_db.py"
	flask run
else
	pip3 install Flask
	echo Flask was not found and had to be installed, please try running ./start.sh again.
fi