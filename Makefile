start-db:
	docker-compose up -d

deps:
	pipenv install

api-gunicorn:
	pipenv run gunicorn --workers=10 --bind 0.0.0.0:5000 wsgi:app

api:
	pipenv run python3 -m wsgi

locust:
	pipenv run locust --host=http://localhost:5000 -f locust_test/locustfile.py