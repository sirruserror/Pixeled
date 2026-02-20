prog=Pixeled

all: build
build:
	python3 -m PyInstaller --onefile src/main.py -D -n pixeled
clean:
	rm -rf build dist __pycache__ Pixeled.spec

