import os, datetime, pendulum
import requests
 
from airflow.decorators import dag, task
from airflow import DAG
from airflow.providers.jdbc.operators.jdbc import JdbcOperator
from airflow.operators.bash import BashOperator

@dag(
	dag_id="sursaut_covid_2",
	schedule_interval="0 0 * * *",
	start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
	catchup=False,
	dagrun_timeout=datetime.timedelta(minutes=60),
)
def Process():

    sql1 = " select * from etlv2.sursaut_covid "
    sql2 = """ insert into etlv2.exemple values (3, 'b') """

    read_table_jdbc = JdbcOperator(
        task_id="read_exemple",
        jdbc_conn_id="etlv2_inpa",
        sql=sql1,
        autocommit=False,
    )
    
    insert_table_jdbc = JdbcOperator(
        task_id="insert_sursaut_covid",
        jdbc_conn_id="etlv2_inpa",
        sql=sql2,
        autocommit=False,
    )
    
    insert_sursaut_bash = BashOperator(
        task_id="insert_sursaut_bash",
        bash_command="bash /home/andria/Documents/DonneesCovid/sursaut_covid_insert_light/sursaut_covid_insert_light_run.sh ",
    )
    

    read_sursaut_bash = BashOperator(
        task_id="read_sursaut_bash",
        bash_command="bash /home/andria/Documents/DonneesCovid/sursaut_covid_read/sursaut_covid_read_run.sh ",
    )

    read_sursaut_bash
    # insert_sursaut_bash
    # read_table_jdbc
    # insert_table_jdbc

dag = Process()