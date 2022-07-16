import psycopg2
from psycopg2 import Error
from config import host, user, password, database_name, port

connection = None
try:
    # connect database
    connection = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        dbname=database_name,
    )

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT VERSION()"
        )
        print(cursor.fetchone())

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

finally:
    if connection:
        connection.close()
