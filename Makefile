SHELL:=/bin/bash

VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=python3
PIP=${VENV_NAME}/bin/pip3

install:
	${PYTHON} -m pip install virtualenv
	${PYTHON}  -m venv venv
	make venv
	${PIP} install -r requeriments.txt

venv:
	source ${VENV_ACTIVATE}

test-secretum:
	make -f secretum/Makefile test

lint-secretum:
	make -f secretum/Makefile lint

test-jedi:
	make -f jedi/Makefile test

lint-jedi:
	make -f jedi/Makefile lint

build: venv
	${PYTHON} setup.py install

zip:
	zip Prac1.zip Makefile jedi/* secretum/* setup.py README.md docs/* requeriments.txt
