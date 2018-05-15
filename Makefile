lint:
	flake8
	pydocstyle src

install-dev-requirements:
	pip install -r py-requirements/dev.txt

run-migrations:
	python3.6 ./src/manage.py migrate

tests-python:
	pytest --cov=.

docker-lint-flake8:
	docker exec backend_1 flake8

docker-lint-pydocstyle:
	docker exec backend_1 pydocstyle .

docker-install-dev-requirements:
	docker exec backend_1 pip3.6 install -r py-requirements/dev.txt

docker-start-db:
	docker-compose up -d --build postgres

docker-start-bg:
	docker-compose up -d --build backend

docker-start-redis:
	docker-compose up -d --build redis

docker-start-frontend:
	docker-compose up -d --build frontend

docker-dev-start-all:
	docker-compose -f docker-compose.yml up

docker-test:
	@make docker-test-backend
	@make docker-test-frontend

docker-test-backend:
	docker exec backend_1 pytest --cov=.

docker-test-frontend:
	docker exec frontend_1 npm run mocha

docker-makemigrations:
	docker exec backend_1 python3.6 ./src/manage.py makemigrations

docker-migrations:
	docker exec backend_1 python3.6 ./src/manage.py migrate

docker-reset-db:
	docker stop postgres_1
	docker rm postgres_1
	docker-compose up -d --build postgres

docker-add-admin:
	docker exec backend_1 python3.6 ./src/manage.py loaddata src/fixtures/admin_fixtures.json
