SHELL:=/bin/bash


VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

venv: $(VENV_NAME)/bin/activate

# STRATEGY = i runs the iterative method
# STRATEGY = r runs the iterative method
STRATEGY:=i
test : venv
	for i in $$(seq 2 2 20);\
	do \
	   python jedi/generator.py $$i $$i > jedi/deck.txt 2> jedi/sol1.txt; \
	   python jedi/jedi_combo.py $(STRATEGY) jedi/deck.txt > jedi/sol2.txt; \
	   if $$(python jedi/checker.py jedi/deck.txt jedi/sol1.txt jedi/sol2.txt); then echo TEST max_size=$$i num_cards=$$i OK; else echo  TEST $$i KO; exit; fi \
	done

lint: venv
	${PYTHON} -m pylint jedi/jedi_combo.py

clean :
	rm -rf *.txt