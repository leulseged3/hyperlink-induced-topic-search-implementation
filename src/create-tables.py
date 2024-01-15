from utils import db_connect, queries


# create tables for the first dataset "news-aggregate-dataset-1"
connection = db_connect.create_connection("news-aggregate-dataset-1")

if connection:
    cursor = connection.cursor()
    cursor.execute(queries.create_topics_table_query)

    cursor.execute(queries.insert_topics_query)
    connection.commit()

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
    cursor.execute(queries.create_topics_table_query)

    cursor.execute(queries.insert_topics_query)
    connection.commit()

    cursor.execute(queries.create_news_table_query)
    connection.commit()
    cursor.close()
    connection.close()
else:
    print("Error: Database connection not established.")