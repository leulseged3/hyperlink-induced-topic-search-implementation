from utils import queries
from utils import db_connect

connection = db_connect.create_connection()

def createDBWithTables():
  if connection:
    cursor = connection.cursor()
    cursor.execute(queries.create_topics_table_query)

    cursor.execute(queries.insert_topics_query)
    connection.commit()

    cursor.execute(queries.create_news_table_query)
    connection.commit()
    cursor.close()
    connection.close()