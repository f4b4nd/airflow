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

    sql1 = " select * from etlv2.sursaut_covid "
    sql2 = """ insert into etlv2.example values ('b', 3) """

    read_table_jdbc = JdbcOperator(
        task_id="jdbc_fetchall",
        jdbc_conn_id="etlv2_inpa",
        sql=sql2,
        autocommit=True,
    )

    read_table_jdbc

dag = Process()
