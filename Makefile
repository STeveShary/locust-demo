start-db:
	docker-compose up -d

deps:
	pipenv install

api:
	pipenv run python3 -m api_demo.api

locust:
	pipenv run locust --host=http://localhost:5000 -f locust_test/locustfile.py