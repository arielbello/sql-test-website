import psycopg2.pool
from flask import current_app


cnxpool = None


def setup_engine():
    global cnxpool
    if not cnxpool:
        db_config = {
            'user': current_app.config["DB_USER"],
            'password': current_app.config["DB_PASSWORD"],
            'database': current_app.config["DB_NAME"],
            'host': current_app.config["DB_HOST"]
        }
        if current_app.config.get("ENV") == "development":
            db_config["port"] = current_app.config["DB_PORT"]

        cnxpool = psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=3,
                                                       **db_config)
    return cnxpool


def write_entry(email, query, accepted, exec_time):
    cnx = setup_engine().getconn()
    with cnx.cursor() as cursor:
        try:
            cursor.execute("""
                INSERT INTO users (email, query, accepted, execution_time)
                VALUES (%s, %s, %s, %s);
                """,
                (email, query, accepted, exec_time)
            )
        except Exception as e:
            success = False
            print(f"Unable to run the query {e.args}")
        finally:
            success = True if cursor.rowcount == 1 else False

    cnx.commit()
    cnxpool.putconn(cnx)

    return success
