# Makefile for CSC3022F
# Mahir Moodaley (MDLMAH007)
# 11 May 2024

install: venv
	. venv/bin/activate; python -m pip install --upgrade pip;pip install -Ur requirements.txt
venv:
	test -d venv || python3 -m venv venv
clean:
	rm -rf venv
runSkeleton:
	. venv/bin/activate; python src/ExecutionSkeleton.py	
run1:
	. venv/bin/activate; python3 src/Scenario1.py
