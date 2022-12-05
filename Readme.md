# 1. First time ?

## 1.0 set dag_folder inside ~/airflow/airflow.cfg
```
# open airflow.cfg
cd ~/airflow/airflow.cfg
```

```
# example of updated dag_folder
dags_folder = /home/fabien/Documents/dev/airflow/dags
```

## 1.1 create airflow user
airflow users  create --role Admin --username airflow --email airflow@ex.com --firstname airflow --lastname airflow --password airflow

## 1.2 create .env file
DRIVER_CLASS=...
USERNAME=...
PASSWORD=...
DRIVER_PATH=...
CONNECTION_URL=...

## 1.2 install pipenv
pipenv shell
pip install -r requirements.txt


# RUN airflow services
pipenv shell
(pipenv) python3 -m airflow webserver
(pipenv) python3 -m airflow scheduler
