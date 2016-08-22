{{ if eq PythonVersion "3.x" }}
PYTHON=python3
{{ else if eq PythonVersion "2.x" }}
PYTHON=python2
{{ else }}
PYTHON=python
{{ end }}


# Run main package
all:
	$(PYTHON) -m {{PackageName}}


# Unit testing
t: test
test:
	py.test {{PackageName}} --doctest-modules


# Pypi related recipes
#  dedicated to package distribution on both pypi and testpypi
TESTPYPI=https://testpypi.python.org/pypi
test_register:
	python setup.py register -r $(TESTPYPI)
test_upload:
	python setup.py sdist upload -r $(TESTPYPI)
test_install:
	pip install -U -i $(TESTPYPI) {{PackageName}}

pypi_register:
	python setup.py register
pypi_upload:
	python setup.py sdist upload
pypi_install:
	pip install -U {{PackageName}}
