import os, sys
from sqlalchemy import create_engine

username = os.getenv('USERNAME', '')
password = os.getenv('PASSWORD', '')

host = "egp-sdlbinpa2.egp.aphp.fr"
ip = "1521"
sid = "INPA" 

if __name__ == "__main__":
    url = f"jdbcapi+oraclejdbc://{'localhost'}:{ip}/{'xe'}"
    print(url)
    print(url.split("//", 1)[-1].replace("/",":"))
    #sys.exit()
    engine = create_engine(url)
    with engine.connect() as connection:
        result = connection.execute("select * from exemple")
        for row in result:
            print(row)


# working with :
url = f"jdbcapi+oraclejdbc://{host}:{ip}/{sid}"
# "url" : "jdbc:oracle:thin:@egp-sdlbinpa2.egp.aphp.fr:1521:INPA",
# "driver_args": ['username', 'pwd']
# jdbc_url: str = s.split("//", 1)[-1].replace("/",":")
# sqlalchemy = "/sid" VS jdbcapi = ":sid"