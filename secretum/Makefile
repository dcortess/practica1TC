.PHONY: prepare-dev test lint install run

VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

venv: $(VENV_NAME)/bin/activate

lint: venv
	${PYTHON} -m pylint secretum/secretum.py
	${PYTHON} -m mypy secretum/secretum.py

test: venv
	${PYTHON} secretum/test_secretum.py

n:=123
k:=4
run: venv
	${PYTHON} secretum/secretum.py $n $k


# Si voleu utiltizar-lo des de dins la carpeta com a Makefile independent.

# .PHONY: prepare-dev test lint install run
#
# VENV_NAME?=../venv
# VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
# PYTHON=${VENV_NAME}/bin/python3
#
# venv: $(VENV_NAME)/bin/activate
#
# lint: venv
# 	${PYTHON} -m pylint test_secretum.py
# 	${PYTHON} -m mypy test_secretum.py
#
# test: venv
# 	${PYTHON} test_secretum.py
#
# n:=123
# k:=4
# run: venv
# 	${PYTHON} secretum.py $n $k
