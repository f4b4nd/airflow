import os
import jaydebeapi

#DRIVER_PATH = "/opt/DbVisualizer/resources/dbinfo/templates/driverTypes/oracle_thin/maven/com/oracle/database/jdbc/ojdbc8/21.1.0.0/ojdbc8-21.1.0.0.jar"
#CONNECTION_URL = "jdbc:oracle:thin:@egp-sdlbinpa2.egp.aphp.fr:1521:INPA"
DRIVER_CLASS = os.getenv('DRIVER_CLASS', '')
DRIVER_PATH = os.getenv('DRIVER_PATH', '')
CONNECTION_URL = os.getenv('CONNECTION_URL', '')
CREDENTIALS = [os.getenv('USERNAME', ''), os.getenv('PASSWORD', '')]

def sql_execute(sql, cursor):
    cursor.execute(sql)

def sql_fetchall(sql, cursor):
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res)


if __name__ == "__main__":

    conn = jaydebeapi.connect(
        DRIVER_CLASS,
        CONNECTION_URL,
        CREDENTIALS,
        DRIVER_PATH,
    )

    curs = conn.cursor()

    sql1 = """
        create table example2 (ex1 varchar(400), ex2 integer, ex3 integer)
    """
    sql2 = "select * from etlv2.example "
    sql3 =""" insert into etlv2.example values ('a', 1)"""

    sql_execute(sql3, curs)
    sql_fetchall(sql2, curs)

    curs.close()
    conn.close()

