develop: .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install flit
	.venv/bin/flit install --symlink

clean:
	rm -rf .venv dist

upload:
	.venv/bin/flit wheel --upload

wheel:
	.venv/bin/flit wheel

.venv:
	virtualenv -p python3 .venv

.PHONY: clean develop upload wheel
