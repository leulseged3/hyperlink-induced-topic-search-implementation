import networkx as nx
import matplotlib.pyplot as plt
import hits
from utils import db_connect, queries


def visualizeGraph(param):
    news = []
    # From dataset one
    conn1 = db_connect.create_connection('news-aggregate-dataset-1')

    if conn1:
        cursor = conn1.cursor()
        query1 = queries.fetchTopic(param)
        cursor.execute(query1)
        topic = cursor.fetchone()
        if topic:
            cursor.execute(queries.fetchNews(topic[0]))
            fetchedNews = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            result_list = [dict(zip(column_names, row)) for row in fetchedNews]

            news.extend(result_list)
        cursor.close()
        conn1.close()

    # From dataset two
    conn2 = db_connect.create_connection('news-aggregate-dataset-2')

    if conn2:
        cursor = conn2.cursor()
        query2 = queries.fetchTopic(param)
        cursor.execute(query2)
        topic = cursor.fetchone()
        if topic:
            cursor.execute(queries.fetchNews(topic[0]))
            fetchedNews = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            result_list = [dict(zip(column_names, row)) for row in fetchedNews]

            news.extend(result_list)
        cursor.close()
        conn2.close()

    graph = hits.createNetwork(news[:50])

    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(graph, seed=42)  # Set a seed for reproducibility
    nx.draw(graph, pos, with_labels=True, node_size=800, node_color='skyblue', font_size=10, font_weight='bold')
    plt.title("Graph of Articles based on Keyword Similarity")
    plt.show()

visualizeGraph('business')


