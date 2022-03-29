# -include .env
# export

# MESSAGE ?= mlportal-local

alembic.makemigrations:
	alembic revision --autogenerate -m "$(M)"

alembic.upgrade:
	alembic upgrade head
