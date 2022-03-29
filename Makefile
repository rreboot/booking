# -include .env
# export

# MESSAGE ?= mlportal-local

alembic.makemigrations:
	alembic revision --autogenerate -m "$(M)"

alemgic.upgrade:
	alembic upgrade head
