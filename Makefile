test:
		nosetests tests

coverage:
		nosetests --with-coverage --cover-html --cover-html-dir=html_cover --cover-package=firebat-console

release:
		python setup.py sdist

upload:
		python setup.py sdist upload
