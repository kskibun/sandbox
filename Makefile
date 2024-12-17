.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: migrate
migrate:
	poetry run python -m djangopro.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m djangopro.manage makemigrations

.PHONY: run-server
run-server:
	 poetry run python -m djangopro.manage runserver

.PHONY: superuser
superuser:
	poetry run python -m djangopro.manage createsuperuser

.PHONY: update
update: install migrate install-pre-commit;
