from psycopg2 import sql
from utils import db_connect, queries
    
def table_exists(cursor, table_name):
    query = sql.SQL("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = {});").format(
        sql.Literal(table_name)
    )
    cursor.execute(query)
    return cursor.fetchone()[0]

# create tables for the first dataset "news-aggregate-dataset-1"
connection = db_connect.create_connection("news-aggregate-dataset-1")

if connection:
    cursor = connection.cursor()
    if not table_exists(cursor, "topics"):
        cursor.execute(queries.create_topics_table_query)

        cursor.execute(queries.insert_first_topics_query)
        connection.commit()
    if not table_exists(cursor, "news"):
        cursor.execute(queries.create_news_table_query)
        connection.commit()
        cursor.close()
        connection.close()
else:
    print("Error: Database connection not established.")


# create tables for the second dataset "news-aggregate-dataset-2"
connection = db_connect.create_connection("news-aggregate-dataset-2")

if connection:
    cursor = connection.cursor()
    if not table_exists(cursor, "topics"):
        cursor.execute(queries.create_topics_table_query)

        cursor.execute(queries.insert_second_topics_query)
        connection.commit()
    if not table_exists(cursor, "news"):
        cursor.execute(queries.create_news_table_query)
        connection.commit()
        cursor.close()
        connection.close()
else:
    print("Error: Database connection not established.")