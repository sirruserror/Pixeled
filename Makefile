prog=Pixeled

all: build
build:
	python -m PyInstaller --onefile src/main.py -D -n Pixeled
clean:
	rm -rf build dist __pycache__ Pixeled.spec

