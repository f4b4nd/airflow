# First time ?
airflow users  create --role Admin --username airflow --email airflow@ex.com --firstname airflow --lastname airflow --password airflow


# RUN airflow services
pipenv run python3 -m airflow webserver

pipenv run python3 -m airflow scheduler
