VENV=env
BIN=$(VENV)/bin
ACTIVATE=source $(BIN)/activate

.PHONY: run
run: $(VENV)
	$(ACTIVATE); pypy3 -i -m photorepl

$(VENV): $(VENV)/bin/activate

$(BIN)/activate: requirements.txt
	test -d $(VENV) || virtualenv -p pypy3 $(VENV)
	$(ACTIVATE); pip install -r requirements.txt
	touch $(BIN)/activate

dist/*.whl: setup.py photorepl/*.py
	python setup.py bdist_wheel

dist/*.tar.gz: setup.py photorepl/*.py
	python setup.py sdist bdist

.PHONY: wheel
wheel: dist/*.whl

.PHONY: dist
dist: dist/*.tar.gz

.PHONY: upload
upload: clean
	python setup.py sdist bdist bdist_wheel upload

.PHONY: clean
clean:
	find . -iname '*.pyc' | xargs rm -f
	find . -iname '__pycache__' -type d | xargs rm -rf
	rm -rf build
	rm -rf dist
	rm -rf $(VENV)
	rm -rf *.egg-info
