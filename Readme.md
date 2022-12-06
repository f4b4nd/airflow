# 1. First time ?

## 1.1 install pipenv
pipenv install


## 1.1 set dag_folder inside ~/airflow/airflow.cfg
```
# open airflow.cfg
cd ~/airflow/airflow.cfg
```

```
# example of updated dag_folder
dags_folder = /home/fabien/Documents/dev/airflow/dags
```

## 1.2 create airflow user
airflow users  create --role Admin --username airflow --email airflow@ex.com --firstname airflow --lastname airflow --password airflow

## 1.3 create .env file
DRIVER_CLASS=...
USERNAME=...
PASSWORD=...
DRIVER_PATH=...
CONNECTION_URL=...



# 2 RUN airflow services
pipenv shell
(pipenv) python3 -m airflow webserver
(pipenv) python3 -m airflow scheduler
