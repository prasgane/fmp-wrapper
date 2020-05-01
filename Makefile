
clean:
	rm -rf build/ dist/ *.egg-info

build:
	python3 setup.py sdist bdist_wheel

dist:
	twine upload dist/*
