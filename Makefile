db:
	@touch db/db.sqlite
	sqlite3 db/db.sqlite < db/create.sql

.PHONY: db
