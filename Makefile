VENV=env
BIN=$(VENV)/bin
ACTIVATE=source $(BIN)/activate

.PHONY: run
run: $(VENV)
	$(ACTIVATE); python -i -m photorepl

$(VENV): $(VENV)/bin/activate

$(BIN)/activate: requirements.txt
	test -d $(VENV) || virtualenv -p /usr/bin/python3 --system-site-packages $(VENV)
	$(ACTIVATE); pip install -r requirements.txt
	touch $(BIN)/activate
