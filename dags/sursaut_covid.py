import os, datetime, pendulum
import requests
 
from airflow.decorators import dag, task

from airflow.providers.jdbc.operators.jdbc import JdbcOperator

@dag(
	dag_id="sursaut_covid_2",
	schedule_interval="0 0 * * *",
	start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
	catchup=False,
	dagrun_timeout=datetime.timedelta(minutes=60),
)
def Process():

    read_table_jdbc = JdbcOperator(
        task_id="jdbc_fetchall",
        jdbc_conn_id="jdbc_inpa_0",
        sql=" select * from etlv2.sursaut_covid ",
        autocommit=True,
    )


    read_table_jdbc

dag = Process()
