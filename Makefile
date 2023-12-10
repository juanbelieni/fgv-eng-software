db:
	@touch db/db.sqlite
	sqlite3 db/db.sqlite < db/create.sql

test:
	python -m pytest --import-mode importlib tests/*.py

run:
	python src/main.py

coverage:
	coverage run --omit="tests/*.py" -m pytest --import-mode importlib tests/*.py
	coverage report -m

.PHONY: db test run coverage
