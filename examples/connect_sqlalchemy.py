import os, sys
from sqlalchemy import create_engine, text

username = os.getenv('USERNAME', '')
password = os.getenv('PASSWORD', '')

host = "egp-sdlbinpa2.egp.aphp.fr"
ip = "1521"
sid = "INPA" 

if __name__ == "__main__":
    url = f"jdbcapi+oraclejdbc://{username}/{password}@{host}:{ip}/{sid}"
    print(url)
    print(url.split("//", 1)[-1])
    sys.exit()
    engine = create_engine(url)
    with engine.connect() as connection:
        result = connection.execute("select * from exemple")
        for row in result:
            print(row)