#!/bin/bash
# usage: run "./start.sh" on a UNIX machine
# Check for dependencies && start the flask app
#
# Required installs on machine.
# Python3, pip3, pip install Flask
# 
# Incase script fails to work, run the following commands:
# python init_db.py
# flask run
#
# At this point the application should be running.
#
# python dbtest.py 
# to print the current tables in 'users.db'



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
