import jaydebeapi

driver_class = "oracle.jdbc.OracleDriver"
driver_path = "/home/andria/Documents/airflow/ojdbc8-21.1.0.0.jar"
driver_path2 = "/opt/DbVisualizer/resources/dbinfo/templates/driverTypes/oracle_thin/maven/com/oracle/database/jdbc/ojdbc8/21.1.0.0/ojdbc8-21.1.0.0.jar"
connection_url = "jdbc:oracle:thin:@egp-sdlbinpa2.egp.aphp.fr:1521:INPA"
credentials = ["etlv2", "etl--1428"]

conn = jaydebeapi.connect(
    driver_class,
    connection_url,
    credentials,
    driver_path2,
)
curs = conn.cursor()
sql = """
    create table example2 (ex1 varchar(400), ex2 integer)
"""
sql2 = "select * from etlv2.sursaut_covid "


curs.execute(sql2)
res = curs.fetchall()
print(res)

curs.close()
conn.close()