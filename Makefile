RUN=pipenv run

.PHONY: run
run:
	$(RUN) python -i -m photorepl

dist/*.whl: setup.py photorepl/*.py Pipfile Pipfile.lock
	$(RUN) python setup.py bdist_wheel

dist/*.tar.gz: setup.py photorepl/*.py Pipfile Pipfile.lock
	$(RUN) python setup.py sdist bdist

.PHONY: wheel
wheel: dist/*.whl

.PHONY: dist
dist: dist/*.tar.gz

.PHONY: upload
upload: clean
	$(RUN) python setup.py sdist bdist bdist_wheel upload

.PHONY: clean
clean:
	find . -iname '*.pyc' | xargs rm -f
	find . -iname '__pycache__' -type d | xargs rm -rf
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
