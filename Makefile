develop: .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install flit
	.venv/bin/flit install --symlink

clean:
	rm -rf .venv dist

test:
	.venv/bin/python -m unittest

upload:
	.venv/bin/flit wheel --upload

wheel:
	.venv/bin/flit wheel

.venv:
	python3 -m venv .venv

.PHONY: clean develop test upload wheel
