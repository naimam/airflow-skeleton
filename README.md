# Initializing Environment

- fetch the docker-compose.yaml in the terminal: 
	`curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.4.2/docker-compose.yaml'`

- `mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env`


- Initialize the database: 
	`docker-compose up airflow-init`

	username: airflow, password: airflow

Run airflow: `docker-compose up -d`

Open webserver in: http://localhost:8080

# Building Image
- `docker build . --tag extending_airflow:latest'
- open docker-compose.yaml and change image name from: `image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.4.2}`
-rebuild airflow web server and scheduler service since the airflow image was modified:
	`docker-compose up -d --no-deps --build airflow-webserver airflow-scheduler`

- port in use error
	`docker container ls
	docker rm -f <container-name>`

- stop all containers: `docker-compose down`
