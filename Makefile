# Makefile for CSC3022F
# Mahir Moodaley (MDLMAH007)
# 11 May 2024

install: venv
	. venv/bin/activate; python3 -m pip3 install --upgrade pip;pip3 install -Ur requirements.txt
venv:
	test -d venv || python3 -m venv venv
clean:
	rm -rf venv
runSkeleton:
	. venv/bin/activate; python3 src/ExecutionSkeleton.py	
run1:
	. venv/bin/activate; python3 src/Scenario1.py
run2:
	. venv/bin/activate; python3 src/Scenario2.py
