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
