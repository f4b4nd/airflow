import os, sys
from sqlalchemy import create_engine

username = os.getenv('USERNAME', '')
password = os.getenv('PASSWORD', '')

host = os.getenv('HOST', 'localhost')
sid = os.getenv('SID', '')
ip = "1521"

if __name__ == "__main__":
    url = f"jdbcapi+oraclejdbc://{host}:{ip}/{sid}"
    print(url)
    print(url.split("//", 1)[-1].replace("/",":"))
    #sys.exit()
    engine = create_engine(url)
    with engine.connect() as connection:
        result = connection.execute("select * from exemple")
        for row in result:
            print(row)


