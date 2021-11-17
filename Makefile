.PHONY: build clean upload

build:
	python3 setup.py sdist bdist_wheel

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

upload:
	twine upload dist/*